def rule_handling(number1, number2, operator):
    try:
        if (operator != '+' and operator != '-'):
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    
    try:
        if (int(number1) and int(number2) is False):
             raise BaseException           
    except:
        return "Error: Numbers must only contain digits."
    
    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    
    return ""


def arithmetic_arranger(problems, display=False):            
    start_problem = True
    split_side = '    '
    row1 = row2 = row3 = row4 = ''
    
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    
    for problem in problems:
        # split problem and save to problem
        problem = problem.split()
        #store problem index = 0 to number1
        number1 = problem[0]
        #store problem index = 1 to operator
        operator = problem[1]
        #store problem index = 2 to number2
        number2 = problem[2]
        
        space = max(len(number1), len(number2))
        rule = rule_handling(number1, number2, operator)
        
        if rule != "":
            return rule
        
        if (start_problem) :
            row1 += number1.rjust(space + 2)
            row2 += operator + ' ' + number2.rjust(space)
            row3 += '-' * (space + 2)
            if display:
                if operator == '+':
                    row4 += str(int(number1) + int(number2))
                elif operator == '-':
                     row4 += str(int(number1) - int(number2)) 
            start_problem = False
        else: 
            row1 += number1.rjust(space + 6)
            row2 += operator.rjust(5) + ' ' + number2.rjust(space)
            row3 += split_side + '-' * (space + 2)
            if display:
                if operator == '+':
                    row4 += split_side + str(int(number1) + int(number2)).rjust(space + 2)
                elif operator == '-':
                     row4 += split_side + str(int(number1) - int(number2)).rjust(space + 2)
                     
    if display == True:
        arranged_problems = row1 + '\n' + row2 + '\n' + row3 + '\n '+ row4
    else:
        arranged_problems = row1 + '\n' + row2 + '\n'  + row3

    return arranged_problems