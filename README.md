# Hambot
### The intellectual hamster you never knew you needed.

Hambot is a simple agent where the LLM is running within Ollama. It isn't using any tools or anything fancy. This demonstrates
how to load a model with a custom system prompt, maintain conversational context, and make minor tweaks to the model behavior via its supported options with Ollama.

This is currently running on llama3.2 3b so it's easy to run locally. I'm running it on an M3 Macbook with 64GB of memory.

### How to run:
1. You'll need to install [uv](https://docs.astral.sh/uv/guides/install-python/) if you aren't using it already.
2. You also need [ollama](https://ollama.com) with [llama3.2](https://ollama.com/library/llama3.2) downloaded.
3. Build the venv with `uv venv`
4. Run the bot with `uv run main.py`
5. When you want to quit, just type `exit`

### And for fun:

- Say hi and occasionally offer a grape or other tasty treat.
- I rather enjoy letting Hambot lead the conversation as it is fun to see where it takes things.
- It does BS a little so take some of his more advanced concepts with a grain of salt.
- While hamsters are indeed pretty cute, it does get a little offended when not taken seriously. Try it.