name = input("Имя ")
sec_name = input("Фамилия ")
group = input("Группа ")
email = input("Email ")
print(f"{sec_name[:5].lower()}{name[:5].lower()*2}{email[:5]*3}")