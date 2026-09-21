#Write a  python code that takes input n and then print all the numbers starting from 1 till n.

def Print(n):
    if n == 1:
        return str(n)
    else:
        return str(Print(n - 1)) + str(n)


if __name__ == '__main__':
    n = int(input())
    print(Print(n))
    
    

# Here, the Print function is called with n - 1,
# and it is repeatedly called until n becomes 1.
# Then, we concatenate the returned value with the current n.

# Example:
# Print(5):
#     Print(4) + "5"
#     Print(3) + "4" + "5"
#     Print(2) + "3" + "4" + "5"
#     Print(1) + "2" + "3" + "4" + "5"
#     "1" + "2" + "3" + "4" + "5"

# Final Output: "12345"