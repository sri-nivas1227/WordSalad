# WordSalad API Usage Guide

## Quick Start

### 1. Installation

```bash
# Clone repository
git clone https://github.com/sri-nivas1227/WordSalad.git
cd WordSalad

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 2. Running the API

```bash
python app.py
```

The API will start on `http://localhost:5000`

## API Endpoints

### Generate Paragraph - `POST /generate`

Generate a paragraph about a topic with a specific word count.

**Request Format:**
```json
{
  "input": "topic+wordcount"
}
```

**Examples:**

```bash
# Generate 30-word paragraph about the Moon
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "moon30"}'

# Generate 50-word paragraph about Python
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "python50"}'

# Generate 100-word paragraph about AI
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "artificial intelligence100"}'
```

**Response:**
```json
{
  "success": true,
  "input": "moon30",
  "topic": "moon",
  "word_count": 30,
  "paragraph": "The Moon is Earth's only natural satellite and the fifth largest satellite in the Solar System...",
  "used_wikipedia": true
}
```

### Health Check - `GET /health`

Check if the API is running.

```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "WordSalad API"
}
```

### API Info - `GET /`

Get information about available endpoints.

```bash
curl http://localhost:5000/
```

## Input Format

The input format is `topic` + `word_count`:

- **Topic**: Letters and spaces (e.g., "moon", "artificial intelligence")
- **Word Count**: Number between 10 and 500

**Valid Examples:**
- `moon30` ✓
- `python50` ✓
- `artificial intelligence100` ✓
- `quantum computing75` ✓

**Invalid Examples:**
- `moon` ✗ (missing word count)
- `30` ✗ (missing topic)
- `moon-30` ✗ (wrong separator)
- `moon5` ✗ (word count too low)
- `moon1000` ✗ (word count too high)

## How It Works

1. **Input Parsing**: Extracts topic and word count from input string
2. **Wikipedia Lookup**: Fetches relevant information from Wikipedia
3. **LLM Generation**: Uses GPT-3.5 with Wikipedia context to generate paragraph
4. **Response**: Returns coherent paragraph with exact word count

## Error Handling

The API provides clear error messages:

```json
{
  "error": "Invalid input format. Use format: topic + number (e.g., \"moon30\")",
  "input_received": "moon-30"
}
```

Common errors:
- `400 Bad Request`: Invalid input format or missing fields
- `500 Internal Server Error`: API key issues or generation errors

## Testing

### Run Unit Tests
```bash
python test_app.py
```

### Run Demo (No API Key Required)
```bash
python demo.py
```

## Configuration

### Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=sk-your-api-key-here
```

### Customization

You can modify the following in `app.py`:

- **LLM Model**: Change `model="gpt-3.5-turbo"` to other OpenAI models
- **Temperature**: Adjust `temperature=0.7` for creativity (0.0-2.0)
- **Word Count Limits**: Modify min/max validation (currently 10-500)

## Deployment

### Local Development
```bash
python app.py
```

### Production (with Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Troubleshooting

### "OpenAI API key not configured"
- Make sure `.env` file exists with `OPENAI_API_KEY=your-key`
- Check that the key is valid

### Wikipedia returns None
- The topic might not exist on Wikipedia
- Check spelling and try alternative topic names
- The API will still work, just without Wikipedia context

### Word count doesn't match exactly
- GPT models approximate word counts
- Usually within ±5 words of target
- Consider adjusting prompt if precision is critical

## Support

For issues or questions:
- GitHub Issues: https://github.com/sri-nivas1227/WordSalad/issues
- Author: [@sri-nivas1227](https://github.com/sri-nivas1227)
