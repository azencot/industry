"""O. Bagging — PROBLEM. Redo of the 23 Oct screen.

No solution file. Do not open the debrief until this file prints the example.

The platform gives DecisionTreeClassifier. You write bootstrap, fit, and predict.
solution() already seeds once and builds the trees. Leave it alone.

Bootstrap: n indices, n = len(train). Each index is randint with 0 <= i < n.
Repeats are allowed. Call seed only where solution already calls it.

Fit: each tree trains on its own bootstrap of x and y.
x and y are lists. A list of indices does not slice them.

Predict: for each test row, majority vote across trees.
A tie goes to the smaller class label.
Return a list of plain ints, one per test row.

Example (n_estimators = 3) must return [2, 2, 2, 1, 0].
The three trees on that example predict
[2, 2, 2, 1, 0], [2, 2, 2, 1, 0], and [1, 2, 1, 1, 0].

Time box: 20 minutes.
"""

from random import randint, seed

from sklearn.tree import DecisionTreeClassifier


def bootstrap(n: int) -> list[int]:
    """n indices into the training set, with replacement."""
    # implement this
    pass


def fit(classifiers: list[DecisionTreeClassifier], x: list[list[float]], y: list[int]):
    """Train each classifier on its own bootstrap sample."""
    # implement this
    pass


def predict(classifiers: list[DecisionTreeClassifier], x: list[list[float]]) -> list[int]:
    """Majority vote. Tie -> smaller label."""
    # implement this
    pass


def solution(x_train: list[list[float]], y_train: list[int], x_test: list[list[float]], n_estimators: int) -> list[int]:
    seed(42)
    classifiers = [DecisionTreeClassifier(random_state=0) for _ in range(n_estimators)]
    fit(classifiers, x_train, y_train)
    return predict(classifiers, x_test)


if __name__ == "__main__":
    x_train = [[-2.6, 1.9, 2.0, 1.0],
               [-2.8, 1.7, -1.2, 1.5],
               [2.0, -0.9, 0.3, 2.3],
               [-1.5, -0.1, -1.6, -1.1],
               [-1.0, -0.6, -1.2, -0.7],
               [-0.3, 1.2, 2.6, 0.2],
               [-1.8, -1.3, -0.1, -1.2],
               [0.2, 1.2, -0.6, -1.3],
               [-5.2, 0.3, 0.2, 2.2],
               [-0.8, -0.1, 1.5, -0.1],
               [-2.3, 0.3, 0.8, 0.7],
               [0.2, 3.0, 3.6, -0.9],
               [1.7, -0.8, -0.0, 2.0],
               [2.8, 0.8, 1.8, -0.7]]
    y_train = [1, 2, 0, 0, 0, 1, 0, 1, 2, 0, 2, 1, 0, 2]
    x_test = [[-0.1, 1.4, 0.4, -1.0],
              [-1.3, 0.2, -1.3, -0.8],
              [-1.1, 1.5, -2.3, -2.5],
              [0.2, 2.0, -0.1, -0.8],
              [-0.3, -1.6, -3.4, -1.4]]
    got = solution(x_train, y_train, x_test, 3)
    assert got == [2, 2, 2, 1, 0], got
    print("example ok", got)
