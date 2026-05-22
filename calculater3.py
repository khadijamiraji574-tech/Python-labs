# Student Grade Calculator

marks = int(input("Enter marks: "))

if 80 <= marks <= 100:
    print("Grade: A")
elif 70 <= marks <= 79:
    print("Grade: B")
elif 60 <= marks <= 69:
    print("Grade: C")
elif 50 <= marks <= 59:
    print("Grade: D")
elif 0 <= marks < 50:
    print("Grade: F")
else:
    print("Invalid marks! Please enter between 0 and 100.")