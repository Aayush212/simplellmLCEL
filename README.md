# LangChain Server with Groq Integration

This repository contains a simple FastAPI server that integrates with LangChain and Groq for language translation. The server uses a Groq-powered model to translate input text into a specified language. This project demonstrates how to set up and use LangChain with FastAPI, while also integrating external models like Groq.

## Features

- FastAPI-based server for serving LangChain models.
- Integration with Groq API for language model execution.
- Translation functionality via LangChain prompts.
- Environment variable-based configuration for sensitive data (e.g., API keys).

## Requirements

To run this project, you need the following dependencies:

- Python 3.8+
- FastAPI
- LangChain
- Groq API
- dotenv (for environment variables)

You can install the required dependencies using the following:

bash
```
pip install -r requirements.txt
```

Example  ```requirements.txt```
```
fastapi==0.95.0
uvicorn==0.18.3
langchain==0.0.1
langchain-groq==0.0.1
python-dotenv==0.21.0
```

# Setup

1. Clone the repository:
```
git clone https://github.com/Aayush212/simplellmLCEL.git
cd langchain-server
```

2. Create a .env file in the root directory to store your environment variables (such as the ```GROQ_API_KEY```):

Example ```.env``` file:
```
GROQ_API_KEY=your-groq-api-key
```

3. Install the dependencies:
```
   pip install -r requirements.txt
```

4. Run the FastAPI server:
```
python test.py
```

This will start the server at ```http://127.0.0.1:8000```

# API Endpoints

```POST /chain/invoke```

This endpoint accepts a translation request, where the input text will be translated into the specified language using the Groq model.

Request Body:

```{
  "input": {
    "language": "French",
    "text": "Hello"
  },
  "config": {},
  "kwargs": {}
}
```

```language```: The target language for translation (e.g., "French", "Spanish").
```text```: The text to be translated.

Example cURL Request:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/chain/invoke' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": {
    "language": "French",
    "text": "Hello"
  },
  "config": {},
  "kwargs": {}
}'
```

Response:
The response will contain the translated text in the specified language.

```POST /chain/batch```
This endpoint allows batch processing of translation requests.

Request Body:
```
{
  "inputs": [
    {
      "language": "Hindi",
      "text": "How are you?"
    }
  ],
  "config": {},
  "kwargs": {}
}
```

Example cURL Request:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/chain/batch' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "inputs": [
    {
      "language": "Hindi",
      "text": "How are you?"
    }
  ],
  "config": {},
  "kwargs": {}
}'
```

# Documentation

Once the server is running, you can access the auto-generated API documentation at:
```http://127.0.0.1:8000/docs```

# Troubleshooting

Missing Environment Variables: Ensure that the ```.env``` file contains the correct ```GROQ_API_KEY```.

API Errors: If you encounter an error, check the server logs for more details. Ensure that the required dependencies are installed and that your environment is set up correctly.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
```

### Key Sections:
1. **Project Description**: Provides a summary of what the project does.
2. **Requirements**: Lists dependencies that need to be installed.
3. **Setup**: Explains how to set up the project, including creating a `.env` file for API keys.
4. **API Endpoints**: Details on how to interact with the API, including request bodies and example `cURL` commands.
5. **Documentation**: Points to the auto-generated FastAPI documentation at `/docs`.
6. **Troubleshooting**: Offers advice on common issues and how to resolve them.

This `README.md` should provide a clear guide for anyone setting up or using the project. You can copy and paste this into your GitHub repository's `README.md` file.
```
