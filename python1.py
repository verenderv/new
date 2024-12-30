def check_eligibility(marks):
    # Define eligibility threshold
    eligibility_threshold = 40
    
    # Check if all marks are above the threshold
    return all(mark >= eligibility_threshold for mark in marks)

def main():
    # Get student name and marks
    name = input("Enter student's name: ")
    marks = []
    
    # List of subjects
    subjects = ["Math", "Science", "English", "History"]
    
    # Input marks for each subject
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)
    
    # Calculate average
    avg = sum(marks) / len(marks)
    
    # Display student information
    print(f"\n{name}'s Marks:")
    for i, subject in enumerate(subjects):
        print(f"{subject}: {marks[i]}")
    
    print(f"Average Marks: {avg:.2f}")
    
    # Check if eligible for exams
    if check_eligibility(marks):
        print("Eligible for exams.")
    else:
        print("Not eligible for exams.")

# Run the main function
if _name_ == "_main_":
    main()