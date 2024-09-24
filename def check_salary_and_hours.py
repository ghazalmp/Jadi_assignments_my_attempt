# function
# check salary and hours of working



# ask user for their base salary per hour and convert input to float
base_salary = float(input("Enter your base salary per hour: "))
# ask user for their base salary per hour and convert input to float
hours_worked = float(input("Enter the number of hours worked per day: "))

def check_salary_and_hours(base_salary, hours_worked ):
    # check user's conditin of working

    if base_salary < 10 and hours_worked > 8:
        return "Why do you work here? "
    
    if base_salary < 10 and hours_worked < 8 : 
        return "that is probably a general work but be aware that might be undocumented work. "
    
    if hours_worked > 8 and base_salary >= 10:
        return "You're working too much. More than 8 hours is too much work. "

    if hours_worked < 8 and base_salary >= 10:
        return "You have a good life_work balance, congratulation! "
    
    # calculate total salary for hours worked and return the calculated total salary
    sum_salary = base_salary * hours_worked
    return sum_salary


# call the function and print the result
print(check_salary_and_hours(base_salary, hours_worked))


def salary_amount(base_salary,hours_worked):
    total_salary = base_salary * hours_worked
    return total_salary

print(f"If you work 20 days per month, your earnings would be: {salary_amount(base_salary, hours_worked) * 20}")
