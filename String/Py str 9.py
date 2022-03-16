st = "English = 78 Science = 83 Math = 68 History = 65"
sum = 0
count = 0
for a in st.split():
    if a.isnumeric():
        sum = sum+int(a)
        count = count+1
avg = sum/count
print("Total Sum =",sum)
print("Average =",avg)