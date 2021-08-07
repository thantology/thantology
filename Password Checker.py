#Author: Jonathan Anthony Hernandez
#Password Checker Program
#Description: Easy Password Checker using list, if-else, and for loop


Lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Upper_letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','_']

systemrequirement = int(input("How long should the password will be?"));
userpassword = str(input("Type your password "));

lower_letter_password = 0;
upper_letter_password = 0;
number_password=0;
symbols_password=0;

if len(userpassword) >= systemrequirement:
    for values in userpassword:
        if values in Lower_letters:
            lower_letter_password+=1;
        elif values in Upper_letters:
            upper_letter_password+=1;
        elif values in numbers:
            number_password+=1;
        elif values in symbols:
            symbols_password+=1;
    print (f"Your password has {upper_letter_password} upper case letters, {lower_letter_password} lower letters, {number_password} numbers, {symbols_password} symbols")

else:
    print ("You password is not sufficient for our system")
