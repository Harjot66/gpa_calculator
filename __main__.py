#this function calculates the gpa of the grades entered by the user and returns a result

def the_calculator(num_courses, gpa_scheme):
    
    global gpa_sum
    
    gpa_sum = 0

    course_num = 1
    
    global ordinal

    ordinal = ""
    
#this loop iterates over each course and requests the GPA of each course from the user as well as determines 
#which ordinal to use in the input statements asked to the user
    
    for i in range(1, int(num_courses) + 1):
        
        def ordinate_funct():
        
            if str(course_num)[-1] == '1':
                
                ordinal = "st"
                
            elif str(course_num)[-1] == '2':
                
                ordinal = "nd"
                
            elif str(course_num)[-1] == '3':
                
                ordinal = "rd"
                
            else:
                
                ordinal = "th"
                
            try:
                
                global gpa_sum_temp
                
                gpa_sum_temp = 0
            
                gpa_sum_temp += float(input("\nPlease input the GPA for your " + str(course_num) + str(ordinal) + " course: "))
            
            except ValueError:
                
                print("\nError, please enter a valid number")
                
                ordinate_funct()
                
        ordinate_funct()
        
        gpa_sum += gpa_sum_temp
        
        course_num += 1
        
#this code prints the gpa result to the user
        
    average_gpa = gpa_sum/num_courses
        
    input("\nPress enter to see your GPA")
        
    print("\nYour GPA is " + str(round(average_gpa, 2)) + " out of " + str(round(gpa_scheme, 2)))

#this code calls the above functions to initiate the code

print("""
      \nThis program is a Grade Point Average (GPA) calculator, which works
for any number of courses and GPA grading scheme\n

Procedure:
1. Enter the number of courses you would like to calculate the GPA for
2. Enter the GPA for each course line-by-line as the prompts ask you to
3. Get the result
""")

print("This GPA calculator has been programmed by https://github.com/Harjot66\n")

def check_if_number_1(val_to_check_1):

    try:
        
        global user_num_courses
        
        user_num_courses = float(val_to_check_1)
        
    except ValueError:
        
        print("\nError, please enter a valid number")
        
        check_if_number_1(input("\nHow many courses are you calculating for? "))
        
check_if_number_1(input("\nHow many courses are you calculating for? "))

def check_if_number_2(val_to_check_2):

    try:
        
        global user_gpa_scheme
        
        user_gpa_scheme = float(val_to_check_2)
        
    except ValueError:
        
        print("\nError, please enter a valid number")
        
        check_if_number_2(input("\nWhat is your GPA grading scheme out of? "))

check_if_number_2(input("\nWhat is your GPA grading scheme out of? "))

the_calculator(user_num_courses, user_gpa_scheme)
