# APS1

## Authors
João Kouznetz Bresser

## Como Instalar o Projeto:
- clonar o repositório no seu computador.
- Instalar bibliotecas necessárias rodando: ``` pip install -r ```
- Colocar a base de dados receitas.json na raiz do projeto

## Como rodar o projeto
- No arquivo app/main.py defina qual é a porta que você deseja rodar localmente o seu sistema de pesquisa.
- Em seguinda rode no terminal o arquivo main.py ``` python app/main.py```
- Por fim acesse no seu browser com a seguinte url: `http://0.0.0.0:7654/query?query=oque%20voce%20deseja%20pesquisar ` (substitua o `7654` pela porta que você escolheu no arquivo `main.py` e o `oque%20voce%20deseja%20pesquisar` por palavras chaves que você deseja encontrar receitas que se tem mais relevancias)


## Como funciona:
O principal objetivo do projeto é ter uma maneira para encontrar receitas que se pode fazer com base nos ingredientes que você tem na sua casa.

A **relevancia** dele é pessoal porque nunca tenho ideia do que se fazer com base nas comidas que e tenho em casa.

### Como funciona o sistema de pesquisa:
- 1. **Carregamento dos dados** Os dados são carregados para um DataFrame, e uma nova coluna chamada content é criada, contendo os ingredientes e o método de preparo das receitas.
- 2. **Vetorização de Dados**: Utilizamos a técnica TF-IDF (Term Frequency-Inverse Document Frequency) para vetorizar os dados da base de dados. Isso transforma o texto em representações numéricas que refletem a importância das palavras dentro do contexto de todos os documentos. Sendo esse valor valculado pela divisão do TF(term frequency) pelo DF(document frequency)

- 3. **Busca e Relevancia**: Multiplica-se essa matriz( que contem a importancia da palavra dentro do contexto de todos os documentos) por um vetor que contem a relevancia de cada palavra da query. O que se resulta em um vetor com a revelancia de cada documento. No caso sendo cada receita. Por fim se ordena esse vetor com o dado mais relevante para o menos relevante.

- 4. **Formatação da Resposta**: : Definim uma função que formata a resposta, definindo uma quantidade mínima e máxima de relevância para devolver os documentos e fornecendo o formato correto para retornar o documento.


## Como testar:
- Para testar ele é só estar conectado no internet do insper pesquisar no seu navegador a seguinte url: `http://10.103.0.28:7654/hello` ele deve devolver um hello world mostando que a api esta funcionado
- para testar a pesquisa voce pode na internet do insper pesquisar com a seguinte url: `http://10.103.0.28:7654/query?query=beans` ele deve devolver um json mostrando as receitas mais relevantes com a sua query, ela sendo beans.


## De onde consegui os dados:
A maioria das receitas foram obtidas do seguinte link:
`https://eightportions.com/datasets/Recipes/#fn:1`
