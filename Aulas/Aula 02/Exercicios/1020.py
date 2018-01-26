age = int(input())
years, months, days = age // 365, age % 365 // 30, age % 365 % 30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(years, months, days))
