#number = 6

def factorial(number):
    division = 2
    count = 1
    while number > 1:
        number = number/division
        print("n",number)
        division += 1
        count += 1
    if number == 1.0:
        print("c",count)
        ans=count
    else:
        #print("NONE")
        ans="NONE"
    return ans
print(factorial(3))
