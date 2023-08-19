import math 
user_inputX = input("Enter number x: ")
user_inputY = input("Enter number y: ")

exponent =  int(user_inputX)** int(user_inputY); 
print(exponent) 

base = 2 
log_base_2 = math.log(int(user_inputX), base)
rounded_log = round(log_base_2,3)
print(f"log({user_inputX}) = {rounded_log}")