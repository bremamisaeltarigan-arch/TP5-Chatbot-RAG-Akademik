import json
import os
import re
import time

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
    "tp6-keyword-results.json"
)


def tokenize(text):
    return set(
        re.findall(
            r"\b[a-zA-ZÀ-ÿ]+\b",
            text.lower()
        )
    )


def keyword_score(query, document):
    query_words = tokenize(query)
    document_words = tokenize(document)

    if not query_words:
        return 0

    matched_words = query_words.intersection(
        document_words
    )

    return len(matched_words) / len(query_words)


def main():

    documents = []

    for filename in sorted(os.listdir(DATA_DIR)):

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

                documents.append({
                    "filename": filename,
                    "content": file.read()
                })

    with open(
        TEST_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        tests = json.load(file)

    results = []

    print("=" * 60)
    print("TP6 - KEYWORD SEARCH BASELINE")
    print("=" * 60)

    print()
    print("Jumlah dokumen:", len(documents))
    print("Jumlah test:", len(tests))

    for test in tests:

        start = time.perf_counter()

        ranked = []

        for document in documents:

            score = keyword_score(
                test["query"],
                document["content"]
            )

            ranked.append({
                "filename": document["filename"],
                "score": score
            })

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        elapsed = time.perf_counter() - start

        best = ranked[0]

        result = {
            "id": test["id"],
            "query": test["query"],
            "expected": test["expected"],
            "top_result": best,
            "latency_seconds": round(elapsed, 4),
            "all_results": ranked
        }

        results.append(result)

        print()
        print(test["id"])
        print("Query:", test["query"])
        print(
            "Dokumen teratas:",
            best["filename"]
        )
        print(
            "Keyword score:",
            round(best["score"], 4)
        )
        print(
            "Latency:",
            round(elapsed, 4),
            "detik"
        )

    output = {
        "experiment": "TP6 Keyword Search Baseline",
        "method": "Keyword Search",
        "document_count": len(documents),
        "test_count": len(tests),
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
    print("Baseline selesai.")
    print("Hasil disimpan di:")
    print(RESULT_FILE)
    print("=" * 60)


if __name__ == "__main__":
    main()