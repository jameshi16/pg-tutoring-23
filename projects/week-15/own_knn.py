import csv
import random
from typing import Generator, List, Tuple


def read_rows() -> Generator[List[str], None, None]:
    with open('mnist_784.arff', 'r') as file:
        for row in csv.reader(file):
            yield row


def convert_and_normalize(row: List[str]) -> Tuple[List[float], str]:
    as_int = [int(x) for x in row[:-1]]
    full_sum = sum(as_int)
    return [float(x) / full_sum for x in as_int], row[-1]


def get_all_as_vectors() -> List[Tuple[List[float], str]]:
    # skip header
    iter = read_rows()
    next(iter)

    all_vectors = []
    for row in iter:
        all_vectors.append(convert_and_normalize(row))
    iter.close()
    return all_vectors


def knn(k: int, vector: List[float],
        all_vectors: List[Tuple[List[float], str]]) -> str:
    distances = []
    for v in all_vectors:
        dist = 0
        for i in range(len(v[0])):
            # euclidean distance
            dist += (v[0][i] - vector[i]) ** 2
        distances.append((dist, v[1]))

    distances.sort(key=lambda x: x[0])
    nearest_k = distances[:k]
    class_mappings = {}
    for vec in nearest_k:
        class_mappings[vec[1]] = class_mappings.get(vec[1], 0) + 1
    return sorted(class_mappings.items(), key=lambda x: x[1])[-1][0]


if __name__ == '__main__':
    a_buncha_vectors_and_classes = get_all_as_vectors()
    training_set = a_buncha_vectors_and_classes[:10000]
    test_set = random.sample(a_buncha_vectors_and_classes[10000:], 10)

    correct = 0
    for v in test_set:
        if knn(5, v[0], training_set) == v[1]:
            correct += 1
    print(f'Out of {len(test_set)} cases, {correct} were correct.')
