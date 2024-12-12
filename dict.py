marks={
    "Karan": 100,
    "adi":90,
    "Rohan":98

}
print(marks)
print(type(marks))

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Karan":99})
print(marks)
print(marks.get("Karan")) #elemnt if absent it returns none
print(marks["Karan"])  #if element absent it givs error
