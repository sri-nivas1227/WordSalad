# WordSalad Docker Deployment

## Build the image
```bash
docker build -t wordsalad:latest .
```

## Run the container
```bash
docker run -d \
  -p 5000:5000 \
  -e OPENAI_API_KEY=your_api_key_here \
  --name wordsalad \
  wordsalad:latest
```

## Run with .env file
```bash
docker run -d \
  -p 5000:5000 \
  --env-file .env \
  --name wordsalad \
  wordsalad:latest
```

## Test the API
```bash
curl http://localhost:5000/health
```

## View logs
```bash
docker logs wordsalad
```

## Stop the container
```bash
docker stop wordsalad
docker rm wordsalad
```
