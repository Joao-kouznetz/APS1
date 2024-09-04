import os
from fastapi import FastAPI, Query
import uvicorn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re


app = FastAPI()


# Carregar o DataFrame e pré-processar
df_invertido = pd.read_json("receitas.json")
df = df_invertido.T
df = df.drop(columns=["picture_link"])
df["content"] = df["ingredients"].astype(str) + " " + df["instructions"].astype(str)



def buscando_relevancia(query, df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["content"])
    Q = vectorizer.transform([query])
    relevance_scores = X.dot(Q.T).toarray().flatten()
    sorted_indices = np.argsort(relevance_scores)[::-1]
    return sorted_indices, relevance_scores


def formatando_resposta(sorted_indices, relevance_scores, df, max_docs=10, min_relevance=0.5):
    resposta_formatada = []
    for i in range(min(max_docs, len(sorted_indices))):
        index = sorted_indices[i]
        relevance = relevance_scores[index]
        if relevance >= min_relevance:
            document = {
                "title": df.iloc[index]["title"],
                "content": df.iloc[index]["content"],
                "relevance": relevance,
            }
            resposta_formatada.append(document)
    return resposta_formatada


@app.get("/hello")
def read_hello():
    print("entrou aqui")
    return {"message": "hello world"}




@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):
    sorted_indices, relevance_scores = buscando_relevancia(query, df)
    resposta = formatando_resposta(sorted_indices, relevance_scores, df, min_relevance=0.5)
    return {"results": resposta, "message": "OK"}


def run():
    uvicorn.run("main:app", host="0.0.0.0", port=7654, reload=True)


if __name__ == "__main__":

    run()
