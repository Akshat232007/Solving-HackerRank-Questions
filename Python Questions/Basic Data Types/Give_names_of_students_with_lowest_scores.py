# Problem: Find students with the second lowest score
# and print their names in alphabetical order.

def lowest_grades(students_List):
    length = len(students_List)
    swapped = True
        
    while swapped:
        swapped = False
            
        left = 0
        right = 1
        
        score = 1
                    
        while right < length:
            if students_List[left][score] > students_List[right][score]:
                students_List[left], students_List[right] = students_List[right], students_List[left]
                swapped = True
                    
            left += 1
            right += 1
                
    lowest = students_List[0][score]
    sec_lowest = 1
    
    while students_List[sec_lowest][score] == lowest:
        sec_lowest += 1
    
    second_lowest = students_List[sec_lowest][score]
    
    lowest_grades = []
    
    while sec_lowest < length and students_List[sec_lowest][score] == second_lowest:
        lowest_grades.append(students_List[sec_lowest])
        sec_lowest += 1
                
    return lowest_grades


def sort_names(lg):
    length = len(lg)
    
    swapped = True
    
    while swapped:
        swapped = False
        
        left = 0
        right = 1
        
        name = 0
        
        while right < length:
            if lg[left][name] > lg[right][name]:
                lg[left], lg[right] = lg[right], lg[left]
                swapped = True
                
            left += 1
            right += 1
    
    return lg
        

if __name__ == '__main__':
    
    students_List = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students_List.append([name, score])
        
    lg = lowest_grades(students_List)
    a = sort_names(lg)
    
    for i in range(0, len(a)):
        print(a[i][0])