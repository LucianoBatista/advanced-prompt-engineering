from openai import OpenAI
import os
from dotenv import load_dotenv
import rich


load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def main(prompt: str, prompt_assistant: str, prompt_final: str):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prompt_assistant},
            {"role": "user", "content": prompt_final},
        ],
        model="gpt-4-0125-preview",
        temperature=0,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    prompt = """
    I'm creating a budget planning project for a small business.
    Break this into sub-tasks that will be executed sequentially:
    """
    prompt_assistant = """
    Creating a budget planning project for a small business involves several detailed steps. Breaking it down into manageable sub-tasks can help
ensure thorough planning and execution. Here's a sequential breakdown:

### 1. Define Business Goals and Objectives
    - **Identify short-term and long-term goals:** Understand what the business aims to achieve within the next year and in the next five years.
    - **Align budget with business objectives:** Ensure that the budget is designed to support these goals.

### 2. Gather Historical Financial Data
    - **Collect past financial statements:** Obtain income statements, balance sheets, and cash flow statements for the last 2-3 years.
    - **Analyze revenue trends and cost behavior:** Understand how revenues and expenses have changed over time.

### 3. Forecast Revenue
    - **Estimate future sales:** Based on historical data, market analysis, and industry trends, predict the sales for the upcoming period.
    - **Consider market conditions:** Adjust forecasts based on economic conditions, competition, and other external factors.

### 4. Plan Fixed and Variable Expenses
    - **Identify fixed expenses:** List expenses that remain constant regardless of business activity, such as rent, salaries, and insurance.
    - **Estimate variable expenses:** Determine costs that fluctuate with business volume, like raw materials, shipping, and utilities.

### 5. Determine Cash Flow Needs
    - **Project cash inflows and outflows:** Estimate when money will be received and when payments need to be made.
    - **Identify potential cash shortages:** Plan for periods when the business might need additional cash resources.

### 6. Allocate Budget for Investments
    - **Plan for capital expenditures:** Budget for purchasing assets like equipment or property that will benefit the business in the long term.
    - **Consider investment in growth opportunities:** Allocate funds for marketing, research and development, or expansion.

### 7. Create Contingency Plans
    - **Set aside a contingency fund:** Allocate a portion of the budget for unexpected expenses or emergencies.
    - **Develop strategies for potential challenges:** Plan for scenarios like a downturn in sales or sudden increases in costs.

### 8. Draft the Budget Document
    - **Compile all data into a comprehensive budget:** Use spreadsheets or budgeting software to organize revenue forecasts, expenses, cash flows,
    and investment plans.
    - **Review and adjust:** Ensure the budget is realistic and aligns with business goals. Make adjustments as necessary.

### 9. Obtain Approval and Buy-in
    - **Present the budget to stakeholders:** Share the budget with business owners, investors, or department heads for approval.
    - **Discuss and refine:** Be open to feedback and make necessary revisions to gain consensus.

### 10. Implement and Monitor the Budget
    - **Distribute the budget:** Ensure all relevant parties have access to the budget details.
    - **Set up a monitoring process:** Regularly compare actual financial performance against the budget. Use monthly or quarterly reviews.

### 11. Adjust Budget as Necessary
    - **Identify variances:** Determine where actual results differ from the budgeted figures.
    - **Make adjustments:** Update the budget to reflect changes in business conditions, objectives, or performance.

### 12. Review and Learn
    - **Analyze the budgeting process:** At the end of the budget period, review the effectiveness of the budget in achieving business goals.
    - **Gather insights for future budgeting:** Learn from the outcomes to improve the accuracy and effectiveness of future budgets.

    By following these sub-tasks sequentially, you can create a comprehensive and realistic budget that supports the strategic goals of the small
    business.
"""
    prompt_final = """
    Now considering that the business is a Gym, answer each of the sub-tasks.
    """
    rich.print(main(prompt, prompt_assistant, prompt_final))

# answer!
# Certainly! Let's tailor the budget planning project specifically for a gym business, considering each of the previously mentioned sub-tasks:
#
# ### 1. Define Business Goals and Objectives
# - **Short-term goals:** Increase membership by 20% in the next year, introduce 3 new fitness classes, and reduce member churn by 10%.
# - **Long-term goals:** Expand gym facilities within five years, launch a branded fitness app, and establish partnerships with local health
# businesses.
#
# ### 2. Gather Historical Financial Data
# - **Past financial statements:** Collect income statements and cash flow statements focusing on membership fees, personal training sessions, and
# merchandise sales.
# - **Analyze trends:** Look at how seasonal changes affect gym attendance and revenue, and assess the profitability of different services
# offered.
#
# ### 3. Forecast Revenue
# - **Estimate future sales:** Based on past growth rates, current membership trends, and the introduction of new services or classes.
# - **Consider market conditions:** Factor in local competition, economic trends affecting disposable income, and potential for online fitness
# offerings.
#
# ### 4. Plan Fixed and Variable Expenses
# - **Fixed expenses:** Rent for the gym space, salaries for full-time staff, insurance, and equipment leases.
# - **Variable expenses:** Utilities (which can vary with usage), maintenance costs for gym equipment, salaries for part-time trainers, and costs
# for new class materials.
#
# ### 5. Determine Cash Flow Needs
# - **Project cash inflows and outflows:** Membership fees are primary inflows, typically steady, but may see spikes in January (New Year
# resolutions) and summer. Outflows include monthly fixed expenses and variable costs that may peak with new class launches or equipment
# purchases.
# - **Identify potential cash shortages:** Plan for slower months, like late summer and end-of-year holidays, ensuring enough cash reserve to
# cover fixed expenses.
#
# ### 6. Allocate Budget for Investments
# - **Capital expenditures:** Budget for new gym equipment, technology upgrades for the gym (e.g., a new booking system), and any facility
# expansion plans.
# - **Growth opportunities:** Allocate funds for marketing campaigns, developing the fitness app, and staff training to offer specialized classes.
#
# ### 7. Create Contingency Plans
# - **Contingency fund:** Set aside funds for unexpected repairs, sudden increases in rent or insurance costs, or economic downturns affecting
# membership.
# - **Strategies for challenges:** Develop plans for engaging members during low-attendance months, and strategies for quick adaptation to health
# trends or restrictions.
#
# ### 8. Draft the Budget Document
# - **Compile data:** Use budgeting software to organize and visualize revenue forecasts, categorized expenses, cash flow projections, and
# investment plans.
# - **Review and adjust:** Ensure the budget is realistic, aligns with gym goals, and is flexible enough to adjust for unforeseen changes.
#
# ### 9. Obtain Approval and Buy-in
# - **Present the budget to stakeholders:** This may include business partners, investors, or a board if applicable. Highlight how the budget
# supports growth and sustainability.
# - **Discuss and refine:** Be open to feedback, especially from staff who may offer insights into cost-saving measures or revenue opportunities.
#
# ### 10. Implement and Monitor the Budget
# - **Distribute the budget:** Ensure all department heads and key staff understand their parts of the budget.
# - **Set up a monitoring process:** Regularly review financial performance, especially after launching new classes or marketing campaigns, to
# adjust forecasts and spending as needed.
#
# ### 11. Adjust Budget as Necessary
# - **Identify variances:** Regularly compare actual revenues and expenses against budgeted figures, especially after major events or changes in
# the business.
# - **Make adjustments:** Update the budget to reflect new business opportunities, changes in membership trends, or unexpected expenses.
#
# ### 12. Review and Learn
# - **Analyze the budgeting process:** At the end of the budget period, evaluate how well the budget helped achieve the gym's goals, what worked
# well, and what didn’t.
# - **Gather insights for future budgeting:** Use this analysis to improve budget accuracy, cost management, and revenue forecasting for future
# periods.
#
# By following these tailored steps, a gym can create a dynamic and effective budget that supports its growth, adapts to changes in the fitness
# industry, and meets the needs of its members.
