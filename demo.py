"""
Demo script for WordSalad API - works without API keys
Simulates the API functionality for demonstration
"""

import re


def parse_input(input_str):
    """Parse input string like 'moon30' into topic and word count"""
    match = re.match(r'^([a-zA-Z\s]+?)(\d+)$', input_str)
    if match:
        topic = match.group(1).strip()
        word_count = int(match.group(2))
        return topic, word_count
    return None, None


def generate_demo_paragraph(topic, word_count):
    """Generate a demo paragraph (simulates LLM output)"""
    # This is just a demonstration - real app uses OpenAI
    template = f"This is a demonstration paragraph about {topic}. " * 10
    words = template.split()[:word_count]
    return ' '.join(words)


def main():
    print("=" * 70)
    print("WordSalad API - Demo Mode (No API keys required)")
    print("=" * 70)
    print()
    
    # Demo examples
    examples = [
        "moon30",
        "python50",
        "artificial intelligence100",
        "ocean25"
    ]
    
    for example in examples:
        print(f"Input: '{example}'")
        topic, word_count = parse_input(example)
        
        if topic and word_count:
            print(f"  ✓ Parsed: topic='{topic}', word_count={word_count}")
            paragraph = generate_demo_paragraph(topic, word_count)
            print(f"  Generated paragraph ({len(paragraph.split())} words):")
            print(f"  {paragraph}")
        else:
            print(f"  ✗ Invalid input format")
        
        print()
    
    print("=" * 70)
    print("This is a demo. The actual API uses:")
    print("  • Wikipedia API to fetch real information about topics")
    print("  • OpenAI GPT-3.5 to generate coherent, factual paragraphs")
    print()
    print("To use the real API:")
    print("  1. Set OPENAI_API_KEY in .env file")
    print("  2. Run: python app.py")
    print("  3. Send POST request to http://localhost:5000/generate")
    print("=" * 70)


if __name__ == "__main__":
    main()
