from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def main(prompt: str):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model="gpt-3.5-turbo",
        temperature=0,
    )

    return response.choices[0].message.content


def se():
    prompt = """
    Q: Where was Idris Elba born:
    A: Hackney, Longdon

    Q: How confident are you in that answer? What probability would you give it?
    """
    print(main(prompt))


def self_refine():
    prompt = """
    Brainstorm an idea for a YouTube thumbnail to a video about prompt engineering with large language models. After you've created the idea, critique it. Finally, use the critiques to refine the initial idea.
    """
    print(main(prompt))


if __name__ == "__main__":
    prompt = "What is the meaning of life?"
    self_refine()
