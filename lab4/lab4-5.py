print(type(("element",)))
[1,2,3]*len([1,2,3])
people = [x for x in range(5)]
for x in range(5):
    people[x] = ({
    'name': input(),
    'surname' : input(),
    'sec_name' : input(),
    'birthday' : input(),
    'illness': input()
    })
print(f"Имя {11 * ' '} Фамилия {12 * ' '} Отчество {11 * ' '} Год рождения Болезни ")
for p in  people:
    print(f"{p['name']:<15} {p['surname']:<20} {p['sec_name']:<20} {p['birthday']:<12} {p['illness']}")
