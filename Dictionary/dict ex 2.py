"""dict1 = {'ten': 10, 'twenty': 20, 'thirty': 30}
dict2 = {'thirty': 30, 'fourty': 40, 'fifty': 50}
dict1.update(dict2)
print(dict1)"""
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)