num = int(input("Give me a number to analyse for factorial"));
div = 2

def factor(num):

    while num > 1:
        div +=1
        num = num/div
        
        if num == 1:
            print("Factorial of", div-1)
            break
        elif num > 1:
            continue
        else:
            print("Cannot be factorised")
            break
    return num

            
    
    
    
#for i in range(num):
        #,
        #print(div);
