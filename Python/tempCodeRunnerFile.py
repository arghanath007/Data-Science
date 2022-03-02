family_members={}
for i in range(3):
    name=input("Enter the name of family member: ")
    age=input("Enter the age of age member: ")

    family_members[name]=age

for name, age in family_members.items():
    print("\nName: ", name, "Age: ", age)

find=input("Enter the name")
print(family_members[find])
