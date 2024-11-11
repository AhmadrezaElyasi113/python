# Barname Karname Daneshjoo

# Daryaft naam daneshjoo
student_name = input("Naam Daneshjoo ra vared konid: ")

# Daryaft tedad dars-ha
num_courses = int(input("Tedad dars-ha ra vared konid: "))

# List baraye zakhire etelaat doros
courses = []

# Motaghayer-ha baraye jam kol nomarat va tedad kol vahed-ha baraye mohasebe moadel
total_points = 0
total_units = 0

# Daryaft etelaat har dars
for i in range(num_courses):
    while True:
        try:
            print(f"Moshakhasat dars {i+1} ra be soorat (naam dars, tedad vahed, nomreh) vared konid:")
            course_info = input(f"Dars {i+1}: ")
            course_name, course_units, course_grade = course_info.strip("()").split(',')
            
            course_units = int(course_units.strip()) # Tabdil tedad vahed be adad sahih
            course_grade = float(course_grade.strip()) # Tabdil nomreh be adad ashari
            
            # Zakhire etelaat dars be soorat dictionary
            course = {
                "Naam Dars": course_name.strip(),
                "Tedad Vahed": course_units,
                "Nomreh": course_grade
            }
            
            # Afzoodan dars be list doros
            courses.append(course)
            
            # Mohasebe majmooe nomarat va vahed-ha
            total_points += course_units * course_grade
            total_units += course_units
            
            break
        except ValueError:
            print("Lotfan voroodi ra be shakl sahih vared konid: (naam dars, tedad vahed, nomreh)")

# Mohasebe moadel
if total_units != 0:
    gpa = total_points / total_units
else:
    gpa = 0

# Chap karname
print("\nKarname Daneshjoo:")
print(f"Naam Daneshjoo: {student_name}")
print("Doros:")
print("{:<20} {:<10} {:<10}".format("Naam Dars", "Tedad Vahed", "Nomreh"))
for course in courses:
    print("{:<20} {:<10} {:<10}".format(course["Naam Dars"], course["Tedad Vahed"], course["Nomreh"]))

# Chap moadel
print(f"\nMoadel: {gpa:.2f}")
