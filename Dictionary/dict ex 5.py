sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keys = ["name", "salary"]
result = {k: sampleDict[k] for k in keys}
print(result)
"""for k in keys:
    newdict={k:sampleDict[k]}
    print(newdict)"""