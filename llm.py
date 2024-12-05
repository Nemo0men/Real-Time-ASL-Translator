import argparse
from groqcloud import GroqLLM
import os

api_key = os.getenv("API_KEY")

PROMPT_TEMPLATE = """
Take the following list of words and create a grammatically correct and meaningful sentence:

Words: {words}

Sentence:
"""

def main():
    # Create CLI to accept a string of words as input.
    parser = argparse.ArgumentParser()
    parser.add_argument("word_list", type=str, help="A string of words to turn into a sentence.")
    args = parser.parse_args()
    word_list = args.word_list

    # Format the prompt with the input words.
    prompt = PROMPT_TEMPLATE.format(words=word_list)

    # Use GroqCloud's LLM to generate the response.
    model = GroqLLM(api_key)  
    response_text = model.predict(prompt)

    # Print the generated sentence.
    print(f"Generated Sentence: {response_text}")


if __name__ == "__main__":
    main()
