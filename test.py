from langchain_community.embeddings import HuggingFaceBgeEmbeddings

embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en-v1.5")
vector = embeddings.embed_query("What is blood pressure?")
print(vector[:5])