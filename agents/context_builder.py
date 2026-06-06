from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def build_context(go_files):

    chunks = []
    file_names = []

    for file in go_files:

        try:
            with open(
                file,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                text = f.read()

                chunks.append(text[:3000])
                file_names.append(file)

        except:
            pass

    embeddings = model.encode(chunks)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(
        np.array(embeddings)
    )

    return index, chunks, file_names


def search_context(
        query,
        index,
        chunks,
        file_names):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding),
        5
    )

    context = ""

    for idx in I[0]:

        context += (
            f"\nFILE:{file_names[idx]}\n"
            f"{chunks[idx]}\n"
        )

    return context