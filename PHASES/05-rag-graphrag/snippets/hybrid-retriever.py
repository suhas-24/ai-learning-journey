from collections import defaultdict


def retrieve_dense(query: str) -> list[tuple[str, float]]:
    return [("chunk-a", 0.78), ("chunk-b", 0.74), ("chunk-c", 0.68)]


def retrieve_sparse(query: str) -> list[tuple[str, float]]:
    return [("chunk-b", 12.0), ("chunk-d", 11.5), ("chunk-e", 10.8)]


def reciprocal_rank_fusion(*result_sets: list[tuple[str, float]], k: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = defaultdict(float)
    for result_set in result_sets:
        for rank, (chunk_id, _) in enumerate(result_set, start=1):
            scores[chunk_id] += 1 / (k + rank)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    query = "Which service owns ERR-BILL-402 remediation?"
    fused = reciprocal_rank_fusion(retrieve_dense(query), retrieve_sparse(query))
    for chunk_id, score in fused[:5]:
        print(chunk_id, round(score, 5))
