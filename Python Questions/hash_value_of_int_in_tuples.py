
#Note : This is only valid for Python 2 not for above versions
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))
    
#if __name__ == '__main__':
 #   n = int(input())
  #  t = tuple(map(int, input().split()))
   # print(hash(t))
   
#Use this for above python 3 versions