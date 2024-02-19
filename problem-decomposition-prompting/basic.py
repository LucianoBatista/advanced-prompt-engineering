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


def ltm():
    prompt = """
    It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. The water slide closes in 15 minutes. How many times can she slide before it closes? To find the solution, first decompose the problem into separate sequential sub-problems. Then, iteratively solve each and use it to answer the next.
    """
    print(main(prompt))


def plan_and_solve():
    prompt = """
     "Let’s first understand the problem and devise a plan to solve it. Then, let’s carry out the plan and solve the problem step by step"
    """
    print(main(prompt))


def program_of_thoughts():
    prompt = """
    What sum results if you add up all the numbers from 1 to 100? Please write easily understandable code that could be used to answer this question.
    """
    print(main(prompt))


if __name__ == "__main__":
    prompt = "What is the meaning of life?"
    print(program_of_thoughts())
