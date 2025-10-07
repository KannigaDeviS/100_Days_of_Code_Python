def life_in_weeks(age):
    weeks = age * 52
    total_weeks= 90 * 52
    weeks_left = total_weeks - weeks
    print(f"You have {weeks_left} weeks left.")


age = int(input("How old are you?"))
life_in_weeks(age)

