def factorial(self):
    l = 0
    while  l != (inp+1):

        print (l, end = " x ")
        if l == inp:
            break
        l += 1
    if l == inp:
        return 1
    else: 
        return inp * factorial    
        

  





print ("Please enter in a number")
inp = int(input())
factorial(inp)



