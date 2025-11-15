import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt_tab")

documents = [
    "Machine learning é um campo da inteligência artificial que permite que computadores aprendam padrões a partir de dados.",
    "O aprendizado de máquina dá aos sistemas a capacidade de melhorar seu desempenho sem serem explicitamente programados.",
    "Em vez de seguir apenas regras fixas, o machine learning descobre relações escondidas nos dados.",
    "Esse campo combina estatística, algoritmos e poder computacional para extrair conhecimento.",
    "O objetivo é criar modelos capazes de generalizar além dos exemplos vistos no treinamento.",
    "Aplicações de machine learning vão desde recomendações de filmes até diagnósticos médicos.",
    "Os algoritmos de aprendizado de máquina transformam dados brutos em previsões úteis.",
    "Diferente de um software tradicional, o ML adapta-se conforme novos dados chegam.",
    "O aprendizado pode ser supervisionado, não supervisionado ou por reforço, dependendo do tipo de problema.",
    "Na prática, machine learning é o motor que impulsiona muitos avanços em visão computacional e processamento de linguagem natural.",
    "Mais do que encontrar padrões, o machine learning ajuda a tomar decisões baseadas em evidências.",
]

def preprocessor(text):
  text_lower = text.lower()
  tokens = nltk.word_tokenize(text_lower)
  
  return [word for word in tokens if word.isalnum()]
  
preprocessed_docs = [" ".join(preprocessor(doc)) for doc in documents]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_docs)

query = "machine learning"

def search_tfidf(query, vectorizer, tfidf_matrix): 
  query_vector = vectorizer.transform([query])
  similarities = cosine_similarity(tfidf_matrix, query_vector).flatten()
  sorted_similarities = list(enumerate(similarities))
  results = sorted(sorted_similarities, key=lambda x: x[1], reverse=True)
  
  return results

search_similarities = search_tfidf(query, vectorizer, tfidf_matrix)

print(f"10 document scores by similarity score {query}:")

for doc_index, score in search_similarities[:10]:
  print(f"document {doc_index}: {documents[doc_index]}")
