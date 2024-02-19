from openai import OpenAI
import os
from dotenv import load_dotenv
import rich
from rich import markdown


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


def cot():
    prompt = """
    Virma has three bags, each of which fits five shirts. How many shirts can Virma fit in her bags? Let's think step-by-step.
    """
    return main(prompt)


def thot():
    prompt = """
    Long and complicated context...
    “Walk me through this context in manageable parts step by step, summarizing and analyzing as we go”
    """
    return main(prompt)


def ccot():
    prompt = """
    Q: James writes a 3-page letter to 2 different friends twice a week. How many pages does he write a year?
    Correct Explanation: He writes each friend 3 pages twice a week, totaling 6 pages per friend per week. So, he writes 12 pages every week. Therefore, in a year (52 weeks), he writes 12*52 = 624 pages.
    Incorrect Explanation: He writes each friend 12*52 = 624 pages a week. So, he writes 3*2 = 6 pages every week. Thus, he writes 6*2 = 12 pages a year.

    Q: Chelsea has 30 teeth. Her dentist drills 4 of them and caps 7 more teeth than he drills. What percentage of Chelsea's teeth does the dentist fix?
    """
    return main(prompt)


def sa():
    prompt = """
    Question: Who lived longer, Theodor Haecker or Harry Vaughan Watkins?
    Are follow up questions needed here: Yes.
    Follow up: How old was Theodor Haecker when he died?
    Intermediate answer: Theodor Haecker was 65 years old when he died.
    Follow up: How old was Harry Vaughan Watkins when he died? Intermediate answer: Harry Vaughan Watkins was 69 years old when he died.
    So the final answer is: Harry Vaughan Watkins

    Question: Who was president of the U.S. when superconductivity was discovered?
    Are follow up questions needed here: Yes.
    """
    return main(prompt)


def tabular_cot():
    prompt = """
    Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant?
    |step|subquestion|procedure|result|
    """
    return main(prompt)


if __name__ == "__main__":
    prompt = """
    "I have been ordering from this online store for months now and I am extremely satisfied with their service."
    [Positive]
    """
    # print(main(prompt))
    rich.print(markdown.Markdown(tabular_cot()))
