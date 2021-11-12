class LargestValue():


    def __init__(self,number1,number2,number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3


    def maxValue(number1,number2,number3):
        list = [number1,number2,number3]
        list.sort()
        x = list[2]
        return x




number1 = input("Please Enter in your first Number:")
number2 = input("Please Enter in your second Number:")
number3 = input("Please Enter in your third Number:")

check = LargestValue.maxValue(number1,number2,number3)
print("The largest number Entered was:", check)

print ("Press ENTER to exit")