# APS1

## Authors
João Kouznetz Bresser

## Como Instalar o Projeto:
- clonar o repositório no seu computador.
- Instalar bibliotecas necessárias rodando pip install -r 
- Colocar a base de dados receitas.json

## Como rodar o projeto
- No arquivo app/main.py defina qual é a porta que você deseja rodar localmente o seu sistema de pesquisa.
- Em seguinda rode no terminal o arquivo main.py 
- Por fim acesse no seu browser com a seguinte url: http://0.0.0.0:7654/query?query=oque%20voce%20deseja%20pesquisar  (substitua o 7654 pela porta que você escolheu no arquivo main.py e o oque%20voce%20deseja%20pesquisar por palavras chaves que você deseja encontrar receitas que se tem mais relevancias)


## Como funciona:
O principal objetivo do projeto é ter uma maneira para encontrar receitas que se pode fazer com base principalmente nos ingredientes que você tem na sua casa.

A principal lógica de funcionamento é você tem o seu banco de dados com as receitas. Nesse caso estou utilizando um arquivo json. Dentro do app/main.py tem o código que define  a lógica de funcionamento da API  e o sistema de pesquisa.

### Como funciona o sistema de pesquisa:
primeiro os dados são carregados para um dataframe e é criado uma coluna chamada content que vai conter os ingredientes e o método de preparo. Em seguinda com a query que for recebida da requisição da api query elee vai fazer uma busca  ordenando do mais releavante para o mesno relevante.
Para fazer esse busca primeiro se vetorizar os dados da sua base de dados vetorizas os dados da sua pesquisa.
Mas o que é esse vetorização? 
A vetorização realiza uma tecnica: TF-IDF (Term Frequency-Inverse Document Frequency) na qual transforma o texto dos documentos em representações numéricas que refletem a importância das palavras dentro do contexto de todos os documentos. Isso permite, por exemplo, comparar a relevância de palavras específicas entre diferentes documentos. Sendo esse valor de relevancia calculado pelo divisão do TF(term frequency) pelo DF(document frequency)
Em seguida multiplica-se essa matriz( que contem a importancia da palavra dentro do contexto de todos os documentos) por um vetor que contem a relevancia de cada palavra da query. O que se resulta em um vetor com a revelancia de cada documento. No caso sendo cada receita. Por fim se ordena esse vetor com o dado mais relevante para o menos relevante.

Agora para definir o que se vai ser devolvido e qunato vai ser devolvido for feito a função formatando resposta que define uma quantidade minima de relevancia para devolver os documentos e uma quantidade maximas de documentos que ele pode retornar. Além fornecer um formato certo para retornar o documento.


### Como funciona a api:



A **relevancia** dele é pessoal porque nunca tenho ideia do que se fazer com base nas comidas que e tenho em casa.

## Como testar:


## De onde consegui os dados:
A maioria das receitas foram obtidas do seguinte link:
https://eightportions.com/datasets/Recipes/#fn:1