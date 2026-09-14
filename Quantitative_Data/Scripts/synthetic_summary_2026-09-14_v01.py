"""Demonstration using fictional values, not participant data."""

from statistics import mean


def summarise(scores):
    if not scores or any(type(score) is not int or not 1 <= score <= 5 for score in scores):
        raise ValueError("Provide integer scores from 1 to 5.")
    return len(scores), mean(scores)


if __name__ == "__main__":
    count, average = summarise([3, 4, 5])
    print("SYNTHETIC CLASSROOM EXAMPLE - not research findings")
    print(f"Count: {count}")
    print(f"Mean usefulness score: {average:.2f}")
