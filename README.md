# Readme

Prompt AI Voice Assistant (mix from groq and Deepgram Free APIs) to create a blazing fast voice assistant that can answer questions and do some basic tasks, all from the browser or cli.

## Available models

- Meta : llama2-70b-4096
- Google : gemma-7b-it
- Mistral AI : mixtral-8x7b-32738

This is a simple project to demonstrate how to use AI Api's and mix them to create new interesting stuff.

## Installation

### Clone the repository

```bash
git clone https://github.com/meliani/groq-deepgram-cli.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add your API keys

Add your API keys to the `.sh` file.

```bash
export GROQ_API_KEY="your-groq-api-key"
export DG_API_KEY="your-deepgram-api-key"
```

### Quick Run

#### From sh or bat file

This will register the API keys and run the app.

```bash
./run.sh
```

### Or Run with python internpreter

#### For CLI

Register the API keys as environment variables and run the code.

```bash
python cli/app.py
```

#### For Web

```bash
python web/app.py
```

# Contribute

Contributons are always welcome : fork -> create branch ->push to your repo -> open PR on the main repo ([https://github.com/meliani/ai-voice-cli])
