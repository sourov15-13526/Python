"""sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}"""
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75}
t=min(sampleDict.values())
for i in sampleDict.keys():
     if(sampleDict[i]==t):
         print(i)