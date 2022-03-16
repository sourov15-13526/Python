employees = ['kelly','Ema','John']
defaults = {"designation": 'Application Developer',"Salary": 80000}
result = dict.fromkeys(employees, defaults)
print(result)
print(result["kelly"])