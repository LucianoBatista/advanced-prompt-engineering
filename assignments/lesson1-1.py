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
    # prompt = "Eu quero exemplos de FAQ para um produto específico, um splited keyboard"
    prompt = """
        Aqui estão alguns exemplos de perguntas frequentes para um produto específico, um teclado dividido:
        ### 1. O que é um teclado dividido (split keyboard)?

    **Resposta:** Um teclado dividido é um tipo de teclado ergonomicamente projetado para reduzir a tensão nos braços e pulsos
    durante a digitação. Ele é dividido em duas partes, permitindo que cada metade seja posicionada de acordo com a postura
    natural das mãos e dos braços do usuário.

### 2. Para quem é recomendado o uso de um teclado dividido?

    **Resposta:** É recomendado para qualquer pessoa que passe longos períodos digitando, especialmente para aqueles que já
    experimentam desconforto ou dor nos pulsos, braços ou ombros. Também é ideal para usuários que desejam uma postura mais
    ergonômica ao trabalhar.

### 3. Posso ajustar o ângulo e a distância entre as duas metades do teclado?

    **Resposta:** Sim, a maioria dos teclados divididos permite ajustes de ângulo e distância entre as duas metades, para que
    você possa encontrar a configuração mais confortável e ergonômica para a sua postura de digitação.

### 4. O teclado dividido é compatível com todos os sistemas operacionais?

    **Resposta:** Geralmente, sim. A maioria dos teclados divididos é compatível com os principais sistemas operacionais, como
    Windows, MacOS, Linux, entre outros. No entanto, é sempre bom verificar as especificações do produto para garantir a
    compatibilidade.

### 5. Posso usar o teclado dividido para jogos?

    **Resposta:** Sim, embora seja projetado com foco na ergonomia para digitação, muitos usuários encontram benefícios ao
    usar teclados divididos para jogos, especialmente aqueles que permitem programação de macros e têm teclas de resposta
    rápida.

### 6. Como faço para limpar o meu teclado dividido?

    **Resposta:** Recomenda-se desligar o teclado e usar ar comprimido para remover detritos entre as teclas. Para limpeza
    mais profunda, use um pano levemente umedecido com água ou álcool isopropílico. Evite que líquidos entrem no teclado.

### 7. O teclado dividido é sem fio?

    **Resposta:** Existem modelos tanto com fio quanto sem fio. A escolha entre um modelo com fio ou sem fio depende das suas
    necessidades específicas de mobilidade e da preferência por evitar ou não o gerenciamento de baterias.

### 8. É difícil se acostumar a digitar em um teclado dividido?

    **Resposta:** Pode haver um período de adaptação, pois a disposição das teclas e a separação podem ser diferentes do que
    você está acostumado. No entanto, muitos usuários relatam uma melhora significativa no conforto e na redução da fadiga
    após se acostumarem com o layout.

### 9. O teclado dividido tem todas as teclas de um teclado tradicional?

    **Resposta:** Sim, a maioria dos teclados divididos possui todas as teclas encontradas em um teclado tradicional,
    incluindo teclas de função, teclado numérico (em alguns modelos) e teclas de atalho. A disposição pode variar, então é bom
    verificar as especificações.

### 10. Onde posso comprar um teclado dividido?

    **Resposta:** Teclados divididos podem ser encontrados em lojas de eletrônicos, lojas especializadas em produtos de
    informática e ergonomia, e também em diversas plataformas de venda online. Certifique-se de comprar de um vendedor
    confiável e verificar as avaliações do produto.

        Com base nesses exemplos responda a seguinte pergunta: "Porque eu deveria comprar um teclado dividido?"
    """

    rich.print(main(prompt))
