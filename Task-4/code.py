
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0
max_total = 0
failed = False
grace_limit = 5

for i in range(n):
    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")
    maximum = int(input("Enter maximum marks: "))
    marks = int(input("Enter obtained marks: "))
    pass_marks = int(input("Enter minimum pass marks: "))

    if maximum <= 0 or marks < 0 or marks > maximum:
        print("Invalid marks!")
        failed = True
        break

    if pass_marks < 0 or pass_marks > maximum:
        print("Invalid pass marks!")
        failed = True
        break

    grace = 0

    if marks < pass_marks:
        required = pass_marks - marks

        if required <= grace_limit:
            grace = required
            marks = min(marks + grace, maximum)

    if marks < pass_marks:
        result = "Fail"
        failed = True
    else:
        result = "Pass"

    total += marks
    max_total += maximum

    print("Subject:", subject)
    print("Grace Marks:", grace)
    print("Final Marks:", marks)
    print("Result:", result)


if not failed and max_total > 0:
    percentage = (total / max_total) * 100

    if percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    elif percentage >= 35:
        classification = "Pass"
    else:
        classification = "Fail"

    print("\n----- EXAMINATION RESULT -----")
    print("Student Name:", name)
    print("Total Marks:", total, "/", max_total)
    print("Percentage:", round(percentage, 2), "%")
    print("Final Classification:", classification)

elif not failed:
    print("Invalid total marks.")

else:
    print("\nFinal Result: FAIL")
    print("Student failed or invalid marks entered.")

