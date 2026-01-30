"""
WordSalad Flask API
Generates paragraphs based on topic and word count using Wikipedia and LLM
"""

import os
import re
from flask import Flask, jsonify, request
import wikipediaapi
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='WordSalad/1.0 (https://github.com/sri-nivas1227/WordSalad)'
)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def parse_input(input_str):
    """
    Parse input string like 'moon30' into topic and word count
    
    Args:
        input_str: String in format 'topic<number>' e.g., 'moon30'
    
    Returns:
        tuple: (topic, word_count) or (None, None) if invalid
    """
    # Match pattern: letters followed by digits
    match = re.match(r'^([a-zA-Z\s]+?)(\d+)$', input_str)
    if match:
        topic = match.group(1).strip()
        word_count = int(match.group(2))
        return topic, word_count
    return None, None


def get_wikipedia_summary(topic):
    """
    Fetch summary information from Wikipedia for the given topic
    
    Args:
        topic: Topic to search for
    
    Returns:
        str: Wikipedia summary or None if not found
    """
    try:
        page = wiki_wiki.page(topic)
        if page.exists():
            # Get first few sentences (up to 500 chars for context)
            summary = page.summary[:500]
            return summary
        return None
    except Exception as e:
        print(f"Wikipedia API error: {e}")
        return None


def generate_paragraph_with_llm(topic, word_count, context=None):
    """
    Generate a coherent paragraph using LLM
    
    Args:
        topic: Topic of the paragraph
        word_count: Target number of words
        context: Optional Wikipedia context
    
    Returns:
        str: Generated paragraph
    """
    try:
        # Build prompt based on whether we have Wikipedia context
        if context:
            prompt = f"""Based on the following information about {topic}:

{context}

Write a coherent, informative paragraph about {topic} in exactly {word_count} words. 
The paragraph should be factual, well-written, and maintain the word count precisely."""
        else:
            prompt = f"""Write a coherent, informative paragraph about {topic} in exactly {word_count} words. 
The paragraph should be factual and well-written."""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes precise, factual paragraphs with exact word counts."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=word_count * 3  # Allow some buffer for generation
        )
        
        paragraph = response.choices[0].message.content.strip()
        return paragraph
    
    except Exception as e:
        print(f"LLM generation error: {e}")
        raise


@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate a paragraph based on topic and word count
    
    Request body:
        {
            "input": "moon30"  # Format: topic + word_count
        }
    
    Returns:
        JSON response with generated paragraph
    """
    try:
        data = request.get_json()
        
        if not data or 'input' not in data:
            return jsonify({
                'error': 'Missing input field in request body',
                'example': {'input': 'moon30'}
            }), 400
        
        input_str = data['input']
        topic, word_count = parse_input(input_str)
        
        if not topic or not word_count:
            return jsonify({
                'error': 'Invalid input format. Use format: topic + number (e.g., "moon30")',
                'input_received': input_str
            }), 400
        
        if word_count < 10 or word_count > 500:
            return jsonify({
                'error': 'Word count must be between 10 and 500',
                'word_count_received': word_count
            }), 400
        
        # Fetch Wikipedia context
        wiki_context = get_wikipedia_summary(topic)
        
        # Generate paragraph using LLM
        paragraph = generate_paragraph_with_llm(topic, word_count, wiki_context)
        
        return jsonify({
            'success': True,
            'input': input_str,
            'topic': topic,
            'word_count': word_count,
            'paragraph': paragraph,
            'used_wikipedia': wiki_context is not None
        }), 200
    
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'WordSalad API'
    }), 200


@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information"""
    return jsonify({
        'service': 'WordSalad API',
        'version': '1.0',
        'description': 'Generate paragraphs based on topic and word count',
        'endpoints': {
            '/': 'This information page',
            '/health': 'Health check endpoint',
            '/generate': 'POST endpoint to generate paragraphs'
        },
        'usage': {
            'endpoint': '/generate',
            'method': 'POST',
            'body': {
                'input': 'moon30'
            },
            'example': 'curl -X POST http://localhost:5000/generate -H "Content-Type: application/json" -d \'{"input":"moon30"}\''
        }
    }), 200


if __name__ == '__main__':
    # Check if OpenAI API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("WARNING: OPENAI_API_KEY not set in environment variables")
        print("Please create a .env file with your OpenAI API key")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
