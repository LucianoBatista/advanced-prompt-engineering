from openai import OpenAI
import os
from dotenv import load_dotenv
import rich


load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def main(prompt: str):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model="gpt-4-0125-preview",
        temperature=0,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    prompt = """
    A user is saying that the following presidents was born in New York:
    1. Donald Trump
    2. Franklin D. Roosevelt
    3. Theodore Roosevelt
    4. John F. Kennedy
    5. Rudy Giuliani
    6. Michael Bloomberg

    Please, create a list of verification questions that could be used to guide a fact-checker on the previous response.
    """

    # answers from the model
    prompt1 = """
    1. **Donald Trump**: Was Donald Trump born in New York? Please provide the specific city and state of his birth.
    """
    prompt2 = """
    2. **Franklin D. Roosevelt**: Was Franklin D. Roosevelt born in New York? If so, can you specify the exact location of his birth within the
state?
    """
    prompt3 = """
    3. **Theodore Roosevelt**: Can you confirm if Theodore Roosevelt was born in New York? Please include the city or town and state of his
birth.
    """
    prompt4 = """
    4. **John F. Kennedy**: Was John F. Kennedy born in New York? If not, where was he born? Please provide the city and state of his birth.
    """
    prompt5 = """
    5. **Rudy Giuliani**: Is Rudy Giuliani a former president, and was he born in New York? Please clarify his political position and provide
the city and state of his birth.
    """
    prompt6 = """
    6. **Michael Bloomberg**: Is Michael Bloomberg a former president, and if not, what political or public positions has he held? Was he born
in New York? Please specify the city and state of his birth.
    """
    prompt7 = """
    7. **General Verification**: For each individual listed, can you verify their highest political office held and their birthdate?
    """
    prompt8 = """
    8. **Presidential Criteria**: Can you confirm the criteria used to classify someone as a president in the context of this list?
    """
    prompt9 = """
    9. **Accuracy of Information**: How reliable are the sources providing the birthplaces of these individuals? Please assess the credibility
of the sources used.
    """
    prompt10 = """
    10. **Contextual Clarification**: For any non-presidents listed, can you provide context as to why they were included in a list primarily
focused on presidents?
    """

    ans1 = main(prompt1)
    ans2 = main(prompt2)
    ans3 = main(prompt3)
    ans4 = main(prompt4)
    ans5 = main(prompt5)
    ans6 = main(prompt6)
    ans7 = main(prompt7)
    ans8 = main(prompt8)
    ans9 = main(prompt9)
    ans10 = main(prompt10)

    final = f"""
    A user is saying that the following presidents was born in New York:

    1. Donald Trump
    2. Franklin D. Roosevelt
    3. Theodore Roosevelt
    4. John F. Kennedy
    5. Rudy Giuliani
    6. Michael Bloomberg
    
    Consedering the following verification answers context, answer the user's question:

    {ans1}

    {ans2}

    {ans3}

    {ans4}

    {ans5}

    {ans6}

    {ans7}

    {ans8}

    {ans9}

    {ans10}
    """

    rich.print(main(final))

# final answer
# Based on the information provided:
#
# - **Donald Trump** was born in New York City, New York.
# - **Franklin D. Roosevelt** was born in Hyde Park, New York.
# - **Theodore Roosevelt** was born in New York City, New York.
# - **John F. Kennedy** was not born in New York; he was born in Brookline, Massachusetts.
# - **Rudy Giuliani** is not a former president, but he was born in Brooklyn, New York.
# - **Michael Bloomberg** is not a former president, and he was born in Boston, Massachusetts, not New York.
#
# Therefore, out of the list you provided, three individuals (Donald Trump, Franklin D. Roosevelt, and Theodore Roosevelt) were former presidents
# born in New York. John F. Kennedy was a former president but not born in New York. Rudy Giuliani and Michael Bloomberg, although significant
# political figures and born in New York and Boston respectively, were never presidents.
#
