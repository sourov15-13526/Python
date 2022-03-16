sampleDict = {"Name": "Kelly", "Age": 20, "Salary": 80000, "City": "Dhaka"}
keystoRemove = {"Name": "Kelly", "Salary": 80000}
result = {k: sampleDict[k] for k in sampleDict.keys()-keystoRemove}
print(result)