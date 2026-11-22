import json
import os
import time
import math
import urllib.request

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data",
    "storage"
)

TEST_FILE = os.path.join(
    BASE_DIR,
    "experiments",
    "tp6-test-cases.json"
)

RESULT_FILE = os.path.join(
    BASE_DIR,
    "experiments",
    "tp6-results.json"
)

MODEL = "embeddinggemma"
OLLAMA_URL = "http://localhost:11434/api/embed"


def get_embedding(text):
    data = json.dumps({
        "model": MODEL,
        "input": text
    }).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={
            "Content-Type": "application/json"
        }
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(
            response.read().decode("utf-8")
        )

    return result["embeddings"][0]


def cosine_similarity(a, b):

    dot = sum(
        x * y for x, y in zip(a, b)
    )

    norm_a = math.sqrt(
        sum(x * x for x in a)
    )

    norm_b = math.sqrt(
        sum(y * y for y in b)
    )

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot / (norm_a * norm_b)


def load_documents():

    documents = []

    for filename in os.listdir(DATA_DIR):

        if filename.lower().endswith(".txt"):

            path = os.path.join(
                DATA_DIR,
                filename
            )

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            documents.append({
                "filename": filename,
                "content": content
            })

    return documents


def main():

    print("=" * 60)
    print("TP6 - SEMANTIC SEARCH EXPERIMENT")
    print("=" * 60)

    print()
    print("Model :", MODEL)
    print("Data  :", DATA_DIR)

    documents = load_documents()

    if not documents:

        print()
        print("ERROR: Tidak ada file TXT di data/storage")

        return

    print()
    print("Jumlah dokumen:", len(documents))

    print()
    print("Membuat embedding dokumen...")

    for document in documents:

        start = time.perf_counter()

        document["embedding"] = get_embedding(
            document["content"]
        )

        elapsed = (
            time.perf_counter() - start
        )

        print(
            "-",
            document["filename"],
            "(",
            round(elapsed, 3),
            "detik)"
        )

    with open(
        TEST_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        test_cases = json.load(file)

    results = []

    print()
    print("=" * 60)
    print("HASIL PENGUJIAN")
    print("=" * 60)

    for test in test_cases:

        query = test["query"]

        start = time.perf_counter()

        query_embedding = get_embedding(
            query
        )

        ranked = []

        for document in documents:

            score = cosine_similarity(
                query_embedding,
                document["embedding"]
            )

            ranked.append({
                "filename": document["filename"],
                "score": score
            })

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        elapsed = (
            time.perf_counter() - start
        )

        top_result = ranked[0]

        result = {
            "id": test["id"],
            "query": query,
            "expected": test["expected"],
            "top_result": top_result,
            "latency_seconds": round(
                elapsed,
                4
            ),
            "all_results": ranked
        }

        results.append(result)

        print()
        print(test["id"])
        print("Query:", query)
        print(
            "Dokumen teratas:",
            top_result["filename"]
        )
        print(
            "Similarity:",
            round(
                top_result["score"],
                4
            )
        )
        print(
            "Latency:",
            round(
                elapsed,
                4
            ),
            "detik"
        )

    output = {
        "experiment": "TP6 Semantic Search",
        "model": MODEL,
        "document_count": len(documents),
        "test_count": len(test_cases),
        "results": results
    }

    with open(
        RESULT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=2,
            ensure_ascii=False
        )

    print()
    print("=" * 60)
    print("Eksperimen selesai.")
    print("Hasil disimpan di:")
    print(RESULT_FILE)
    print("=" * 60)


if __name__ == "__main__":
    main()