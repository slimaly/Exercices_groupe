nb_grades =  []

def grade_entry():
    while True:
        user_input = input ("Enter grade")
        
        if user_input == "":
             break
                
        grades = int(user_input)
        
        if 0 <= grades <= 20:
            nb_grades.append(grades)
            
        
        else: 
            return "Invalid grade. Must be between 0 and 20"

        if nb_grades:
            
            nb_grades_count = len(nb_grades)
            highest_grade = max(nb_grades)
            lowest_grade = min(nb_grades)
            average_grade = sum(nb_grades)/nb_grades_count
            print(f"You have submitted the following grade:{grades}")
            print(f"The highest grade is {highest_grade}")
            print(f"The lowest grade is {lowest_grade}")
            print(f"The average grade is {average_grade}")

        else:
            print("no grades entered")