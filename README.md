# Run a simple CLIP demo using the Hugging Face Transformers library

## Instructions / README
* [Lesson-20 / Exercise 3](https://github.com/Encode-Club-AI-Bootcamp/Generative-AI-Applications/tree/main/Lesson-20#multimodal-models-with-computer-vision)

## Setup

Install dependencies:

```bash
pip install clip-as-service
```

On Windows with `Python 3.12`, there are issues installing `clip-as-service 0.8.3`.
The workaround is as follows:

```bash
pip install --upgrade pip setuptools wheel
pip install jina>=3.12.0 --no-build-isolation --no-deps
```

Then, install the dependencies from `requirements.txt`.
After that, attempt to install the cas, ignoring dependencies and bypassing build isolation:

```bash
git clone https://github.com/jina-ai/clip-as-service.git
cd server
pip install . --no-build-isolation --no-deps
cd ../client
pip install . --no-build-isolation --no-deps
```

Copy `.env.sample` and create your `.env` file, replacing placeholder values with actual values.

## Running
Either run via VSCode / PyCharm / your IDE of choice, or use the command line.

For example, on windows, point to your `venv` and then run your file:

```bash
& /path/to/python.exe /path/to/script.py
```

## Resources

**Done as part of Encode_AI-and-GPT-Bootcamp-Q3-2024**

* [GitHub Repo - Encode-Club-AI-Bootcamp / Generative-AI-Applications](https://github.com/Encode-Club-AI-Bootcamp/Generative-AI-Applications)