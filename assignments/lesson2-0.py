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
    Think step by step, and calculate the total price of the following project:
    
    Lumber costs $15 per foot.
    You need 200 feet of lumber.
    Nails cost $5 per box.
    You need 10 boxes of nails per 100 feet of lumber.
    Labor costs are $50 per hour.
    Estimated labor time is 40 hours unless you use more than 10 boxes of nails, in which case it will be equal to the number of feet of lumber plus the cost of all boxes of nails.
    """

    rich.print(main(prompt))

# ans = To calculate the total price of the project, let's break it down step by step:
#
# 1. **Lumber Cost:**
#    - The cost of lumber is $15 per foot.
#    - You need 200 feet of lumber.
#    - Total lumber cost = $15 * 200 = $3000.
#
# 2. **Nail Cost:**
#    - Nails cost $5 per box.
#    - You need 10 boxes of nails per 100 feet of lumber. Since you have 200 feet of lumber, you need 20 boxes of nails.
#    - Total nail cost = $5 * 20 = $100.
#
# 3. **Labor Cost:**
#    - Labor costs are $50 per hour.
#    - Since you are using more than 10 boxes of nails (20 boxes in this case), the labor time will be equal to the number of feet of lumber (200)
# plus the cost of all boxes of nails ($100).
#    - Therefore, the labor cost will not be calculated based on the hourly rate but will instead be the sum of the number of feet of lumber and
# the cost of all boxes of nails.
#    - Total labor cost = 200 (feet of lumber) + $100 (cost of all boxes of nails) = $300.
#
# 4. **Total Project Cost:**
#    - Total project cost = Lumber cost + Nail cost + Labor cost
#    - Total project cost = $3000 (lumber) + $100 (nails) + $300 (labor) = $3400.
#
# Therefore, the total price of the project is $3400.
