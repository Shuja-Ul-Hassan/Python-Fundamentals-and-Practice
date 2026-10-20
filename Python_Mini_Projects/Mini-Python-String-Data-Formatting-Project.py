# String Formatting in user Profile system

print("\tUser Profile System\t")

fullname=input("Enter Your Full name: ")
age=input("Enter Your Age: ")
city=input("Enter Your City: ")
skillsraw=input("Enter Your skills separated by commas: ")

name=fullname.strip().title()
age=age.strip().title()
city=city.strip().title()
skillslist=[skill.strip().title()
            for skill in skillsraw.split(",")]

profile=f"""\t--------------------\t
\t\tUser Profile\t
\t--------------------\t
\tName: {name}\t
\tAge: {age}\t
\tCity: {city}\t
\tSkills: {", ".join(skillslist)}
"""
print(profile)
