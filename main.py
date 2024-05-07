import sys
input_str=input("Enter string:")

try:
    index1=int(input("Enter 1st Index:"))
except ValueError:
    print("Please input an integer for the first index")
    sys.exit(1)

try:
    index2=int(input("Enter 2nd Index;"))
except ValueError:
    print("Please input an integer for the second index")
    sys.exit(1)

def same_chars(str,i1,i2):
    
    try:
        if str[i1] == str[i2]:
            return True
        else:
            return False
    except IndexError:
        return False

print (same_chars(input_str,index1,index2))
