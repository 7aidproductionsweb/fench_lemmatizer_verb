from fastapi import FastAPI
import spacy

app = FastAPI()
nlp = spacy.load("fr_core_news_md")

@app.get("/lemmatize")
def lemmatize(word: str):
    doc = nlp(word)
    lemmas = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    return {"input": word, "lemma": lemmas[0] if lemmas else None}
