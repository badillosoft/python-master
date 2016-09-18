from sklearn import tree

features = [
    [140, 1],
    [130, 1],
    [150, 0],
    [170, 0]
]

labesls = [
    0,
    0,
    1,
    1
]

clf = tree.DecisionTreeClassifier()

clf.fit(features, labesls)

print clf.predict([[158, 1]])