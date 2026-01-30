# WordSalad 🥗
Cook your words instantly

WordSalad is a Flask API that generates coherent paragraphs based on a topic and word count. Just like lorem ipsum, but with actual meaningful content! 

Say "moon30" - and a paragraph about the Moon in exactly 30 words will be generated instantly using Wikipedia APIs and LLM technology.

## Features

- 🚀 **Simple Input Format**: Just combine topic and word count (e.g., "moon30")
- 📚 **Wikipedia Integration**: Fetches relevant context from Wikipedia
- 🤖 **LLM-Powered**: Uses GPT-3.5 to generate coherent, meaningful paragraphs
- ⚡ **Fast Response**: Instant paragraph generation
- 🔧 **RESTful API**: Easy to integrate with any application

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sri-nivas1227/WordSalad.git
cd WordSalad
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

4. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Usage

### API Endpoints

#### 1. Generate Paragraph - `POST /generate`

Generate a paragraph based on topic and word count.

**Request:**
```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "moon30"}'
```

**Response:**
```json
{
  "success": true,
  "input": "moon30",
  "topic": "moon",
  "word_count": 30,
  "paragraph": "The Moon is Earth's only natural satellite...",
  "used_wikipedia": true
}
```

**Input Format:**
- Combine the topic (letters) with the desired word count (numbers)
- Examples: 
  - `"moon30"` - 30 words about the Moon
  - `"python50"` - 50 words about Python
  - `"artificial intelligence100"` - 100 words about Artificial Intelligence

**Word Count Range:** 10-500 words

#### 2. Health Check - `GET /health`

Check if the API is running.

```bash
curl http://localhost:5000/health
```

#### 3. API Info - `GET /`

Get information about the API.

```bash
curl http://localhost:5000/
```

## Examples

### Generate a 30-word paragraph about the Moon:
```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "moon30"}'
```

### Generate a 50-word paragraph about Python:
```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "python50"}'
```

### Generate a 100-word paragraph about Artificial Intelligence:
```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "artificial intelligence100"}'
```

## How It Works

1. **Input Parsing**: The API parses your input (e.g., "moon30") to extract the topic and word count
2. **Wikipedia Lookup**: Fetches relevant information from Wikipedia about the topic
3. **LLM Generation**: Uses GPT-3.5 with the Wikipedia context to generate a coherent paragraph
4. **Response**: Returns a well-structured paragraph with the exact word count

## Error Handling

The API provides clear error messages for:
- Invalid input format
- Missing topic on Wikipedia
- Word count out of range (10-500)
- API key issues
- Internal server errors

## Technology Stack

- **Flask**: Web framework
- **Wikipedia-API**: For fetching topic information
- **OpenAI GPT-3.5**: For generating coherent paragraphs
- **Python-dotenv**: For environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

[@sri-nivas1227](https://github.com/sri-nivas1227)
