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
    Artigo:
    Measuring the effectiveness of your search engine is hard. But you have an army of volunteers helping you: your customers. A great way to measure your search engine’s effectiveness is by analyzing searcher behavior.

How searchers interact with your search engine represents a collection of implicit relevance judgments. It can be tricky to derive insight from these implicit judgments, but it’s well worth the effort. In this post, we’ll explore ways to measure searcher behavior.

It’s about ROI — for the Searcher
Searching is a means, not an end in itself. Searchers invest effort in order to complete a task, their return being that they find what they’re looking for. We improve a searcher’s return on investment (ROI) by either increasing their return (the numerator) or decreasing their investment (the denominator).

Measuring Return
We can never be sure that a searcher found what he or she was looking for. But the two strongest indicators of searcher return are clicks and conversions — and conveniently the latter is also a strong measure of return for your business.

Since conversions represent task completion — the searcher not only found something but actually bought it — you might wonder why we even bother measuring clicks. There are at least two good reasons.

First, conversions are sparse. While conversions are a stronger signal of return for the searcher than clicks, learning from them requires a lot of data. More data means more time to collect it, and time is often your scarcest resource.

Second, there may be good reasons for someone to click on a result but not convert. The searcher may have decided to buy the product at a local store, or to take more time to think about the purchase. The outcome may not be good for your business, but the search experience could still have provided a positive return to the searcher.

That said, not all clicks are good for the searcher. The searcher may click on a result, only to find out after clicking that the product isn’t what he or she was looking for. Clicks tend to overestimate return, while conversions underestimate it. That’s why it’s important to look at both.

Measuring Investment
Searchers invest effort to find what they’re looking for. We can’t hope to make the process completely effortless — not unless we learn how to read their minds! But we should strive to minimize the effort they have to exert in order to achieve their desired return.

Click-Through Rate And Conversion Rate
We can think of the act of performing a search as a single unit of investment. It’s a coarse unit, but nonetheless a useful one that allows us to derive two ROI measures: the click-through rate (CTR) as the fraction of searches resulting in a click, and the conversion rate as the fraction of searches resulting in a conversion.

Mean Reciprocal Rank
Not all searches involve the same amount of effort. The searcher has to take time to scan through the results, looking for something relevant.

Hence, a more granular measure of searcher investment is position of the highest-ranked result that the searcher clicks on. In practice, this is inverted to obtain the reciprocal rank, e.g., if the searcher clicks on the 4th result, the reciprocal rank is 0.25. The average of these reciprocal ranks is called the mean reciprocal rank (MRR).

What about the reciprocal rank for searches that doesn’t receive a click? Here there are two options. One is to not consider those searchers for computing MRR. The other is to treat them as clicks at infinity, contributing a reciprocal rank of 0 (i.e., 1 divided by infinity). Both approaches work, but it’s important to know which one you are using — and very important to keep track of CTR if you’re only including searches that receive clicks when you compute MRR.

Characters Typed
Another source of effort is typing. Typing a long search query requires more effort than typing a short search query, especially when the searcher is typing on a phone. On the other hand, autocomplete can significantly reduce the searcher’s typing effort.

But don’t go overboard in your attempt to reduce effort. If the searcher has only typed in one or two characters, it’s unlikely that you’ll be able to come up with the best autocomplete suggestion. It’s better to let the searcher invest more effort than to disappoint the searcher with a suggestion that doesn’t provide a satisfactory return.

No Perfect Measure
We’ve discussed several ways to measure return and investment. Ideally, we’d have a single measure of each, so that we could compute ROI by dividing one by the other. Unfortunately, all of these measures are proxies, and it would be dangerous to rely on any single measure.

For example, we expect conversion to correlate to clicks. But they don’t always correlate. Sometimes searchers learn something after clicking that we might have told them before they clicked, such as whether the product is available or is eligible for free shipping. Sometimes the searcher is doing research and has no intention of buying anything.

As George Box said, “all models are wrong, but some are useful.” It’s a good idea to track a few measures of searcher return and searcher effort. In general, you want to increase the former and decrease the latter. Most of the time, they’ll move in tandem. But pay attention when they don’t, because that’s when you’re likely to obtain the most useful — and counterintuitive — insights.

    Resumo:
    Esse artigo ele já não traz mais aquele posicionamento de utilizar métricas supervisionadas como **precision** e **recall**. Segue uma linha mais onde a avaliação do seus search engine é feita por meio de feedbacks do seu usuário.

# It's about ROI - for the searcher
- Return on Investment
- Return = "*I find what I'm looking for!!*"
- Investment = "*I write a query, select the filters, enter the page, scroll the page...*"

Nosso principal papel aqui é maximizar o retorno, e minimizar o investimento que o usuário precisa fazer para encontrar uma questão.

## Measuring Return
- Clicks and conversions:
	- Clicou na questão, converteu criando uma prova. The ultimate indicator!
- Importante medir os dois, tanto o clique quanto a conversão. E também tentar entender o por que que um usuário pode clicar numa questão e não converter.

## Measuring Investiment
The effort the user put on finding what he or she want. And our role is to minimize this.

## CTR
É só o click-through rate, uma medida da fração de buscas que resultaram num click.

## [[Mean Reciprocal Rank]] ([[MRR]])
É uma medida bem utilizada em alguns boards de modelos de embedding, não como eles calculam, mas pelo artigo pareceu algo do gênero:
- User faz uma busca
- Ele seleciona o 4 item retornado
- Com isso, nós calculamos o que eles chama de Reciprocal Rank. Onde basicamente pegamos a posição do item selecionar (segundo colocado por exemplo), e invertemos (1/2).
- Depois, esse processo se repete, e nós calculamos a média de todos os Reciprocal Rank.

Deixar umas figuras para ilustrar, de um outro artigo.
![](https://i.imgur.com/YSTF3hX.png)

![](https://i.imgur.com/DpWbA0J.png)

Quanto mais perto de 1, melhor.
ref: https://www.evidentlyai.com/ranking-metrics/mean-reciprocal-rank-mrr#:~:text=Mean%20Reciprocal%20Rank%20(MRR)%20is,item%20across%20all%20user%20lists.

> [!warning] The downside of this metric is that we're not looking for the rest of the results, just for those selected ones.

## Characters Typed
Basicamente fala sobre o tamanho da query, que queremos que seja o menor possível. Nesse processo podemos adicionar um autocomplete, mas para ser efetivo é preciso que esse autocomplete seja bem preciso em relação ao que o usuário quer. Ao contrário ele só vai ter mais trabalho.

Acho que aqui fica um questionamento:
- *Se o usuário digitar menos é um aumento do ROI (ele ta fazendo menos investimento), qual métrica leva isso em consideração?*
- *Ou é algo que a gente pode imputar como uma métrica a ser observada*.

    Artigo:
    In the previous post, we looked at measuring searcher behavior in order to evaluate search engine performance. Measuring searcher behavior is valuable, but a robust evaluation process also involves collecting explicit human judgments. In this post, we’ll look at the use of explicit human judgments for evaluation.

The premise of using human judgments for evaluation is simple. Human evaluators perform a set of tasks in which they’re given a search query and a search result, and asked whether the result is relevant to the query. The judgment can be binary (i.e., relevant vs. not relevant), or it can allow for varying gradations of relevance (e.g., a scale from 1 to 4). Using binary vs. graded relevance is a trade-off which we’ll discuss in a moment.

By collecting these judgments on search results for a representative sample of search queries, we can establish robust estimates of precision @ k or discounted cumulative gain (see previous post for explanations of these).

A key benefit of human judgments is that they are explicit relevance signals.

Benefits of Human Judgments
A key benefit of human judgments is that they are explicit relevance signals. When we measure clicks and conversions, we’re using these as proxies for relevance judgments. But sometimes those proxies mislead us. Searchers may click on irrelevant results out of curiosity, or they may decide not to click because they learn all they need to know from the search results page. Conversions have fewer false positives than a relevance signal, but they have many false negatives: a lack of conversion doesn’t mean the result was irrelevant.

Explicit judgments eliminate the noise introduced by using behaviors as proxies. Explicit judgments also make it possible to test a new search engine before releasing it, avoiding embarrassment or worse.

Another benefit of human judgments is that we can use them to evaluate individual parts of the search engine in isolation. For example, we can use human judgments to judge how well the search engine is understanding the query, separately from how well it ranks results. Or we can use human judgments to evaluate spelling correction. It’s much harder to perform this kind of fine-grained evaluation using behavior, since behavior tends to reflect the end-to-end relevance rather than any one part of the search process.

Disadvantages of Human Judgments
Given these advantages, it’s tempting to rely entirely on human judgments. But human judgments have their disadvantages.

While collecting data about search behavior is essentially free, human judgments cost money, whether the evaluators are in-house employees or crowdsourced workers on platforms like Crowdflower and Mechanical Turk. And there are costs associated with task design and quality assurance. Specifically, quality assurance requires assigning each task to multiple evaluators, which significantly increases costs.

The other problem with human judgments is that an evaluator may not be able to figure out what the searcher was looking for. For example, the evaluator’s understanding of “fancy shirt” might not match the searcher’s. Unless the evaluator knows more about the searcher, human judgment relies on the evaluator being able to make objective relevance judgments just by looking at the query.

Best Practices
Human judgments are useful, but using them effectively can be tricky. Here are some best practices:

Try to use binary relevance. In general, binary relevance minimize the cognitive load for evaluators and leads to a higher-quality signal. More granularity means more effort per task for evaluators and more opportunity for variance — which leads to more need for quality assurance and higher costs. If you really need graded relevance to capture differences, use as few grades as possible, and make sure your evaluators agree on them.
Keep the tasks objective. Don’t ask your evaluators to arbitrate matters of personal taste. There’s no such thing as pure objectivity, but a high variance among evaluators is usually a sign that you’re asking them a subjective question. One of the advantages of binary relevance is that it helps discourage subjectivity: it encourages evaluators to see the task as black or white.
Use human judgments to isolate components. As discussed earlier, human judgments are a great way to evaluate specific search engine components, like query understanding and spelling correction. Having regular access to such judgments can help prioritize investments in improving search quality.
It’s easier and cheaper to measure searcher behavior than to collect explicit human relevance judgments. But explicit human judgments serve more robust signals of relevance, and they’re especially useful for evaluating individual components of the search process in isolation.

So use both! A robust evaluation process combines measuring searcher behavior with collecting explicit human judgments.

    Resumo:
    """
    response = main(prompt)
    rich.print(response)
