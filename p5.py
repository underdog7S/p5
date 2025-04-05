#T1

student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Eve": 95
}


student_name = input("Enter the student's name: ")


if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student not found")



#T2


numbers = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


first_five = numbers[:5]


reversed_list = first_five[::-1]

print("Original List:", numbers)
print("Extracted List:", first_five)
print("Reversed List:", reversed_list)