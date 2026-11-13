def count_substring(string, sub_string):
    
    string_list = list(string)
    substring_list = list(sub_string)
    
    string_length = len(string_list)
    substring_length = len(substring_list)
    
    count = 0
    
    left = 0
    right = (left + substring_length) - 1
    while right < string_length:
        if string_list[left] == substring_list[0] and string_list[right] == substring_list[substring_length - 1]:
            match = True
            for j in range(1,substring_length-1):
                if string_list[left + j] != substring_list[j]:
                    match = False
                    break
            if match:
                count +=1
        left += 1
        right = (left + substring_length) - 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)