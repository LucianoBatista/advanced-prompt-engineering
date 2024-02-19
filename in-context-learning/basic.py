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


def sg_icl_method():
    # generate examples
    prompt = """
    Generate 3 examples of customer reviews and then rate them as positive or negative. Use the following format:
    "[Customer feedback paragraph]\n[classifier]
    """
    examples = main(prompt)
    print(examples)

    # generate the answer
    prompt = f"""
    {examples}
    "Found a hair in my food and the waiter never refilled our drinks. Would not come back."
    """
    answer = main(prompt)
    return answer


if __name__ == "__main__":
    prompt = """
    "I have been ordering from this online store for months now and I am extremely satisfied with their service." 
    [Positive]

    "The food took forever to arrive, and when it finally did, it was cold. The staff was rude and unresponsive when I complained."
    [Negative]

    "Found a hair in my food and the waiter never refilled our drinks. Would not come back."
        """

    prompt_2 = """
        "The food arrives at your table within minutes of ordering, and the waitstaff wastes no time in taking your order and bringing your bill. The dim lighting and soft music create a relaxing ambiance, perfect for a romantic dinner or a night out with friends."
    [Speed][Atmosphere]

    "The flavors are bland, and the dishes lack creativity. It's a letdown, especially considering the high prices."
    [Food][Price]

    "It's tucked away in a remote area, making it difficult to access without a car. From the moment you walk in, you are greeted with friendly smiles and warm welcomes. The high-quality ingredients and expertly prepared dishes justify the cost."
    [Location][Staff][Food][Price]

    "Their cell service is terrible and when I bought expensive phone insurance through them and cracked my screen they somehow said that wasn't covered."
    """

    prompt_3 = """
        5+(10/2)
    5+5 = 10

    (8+3*4)/4
    (8+12)/4 = 20/4 = 5

    four plus ten divided by two
                  
    """
    # print(main(prompt_3))
    print(sg_icl_method())
