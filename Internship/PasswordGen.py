#Importing the random library inbuilt in Python
import random


#Taking the user input for the desired password lenght
lenght = int(input("Enter the desired password lenght : "))


#Function to initiate the password creation script
def createpass(lenght):


    #All possible Upper,Lowercase along with some special characters
    lc = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    uc = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    sp = "! @ # $ % ^ & * ( )"


    #Initializing the List that will contain the shuffled characters
    finallist = []

    #Initializing an empty character that can later use the final list to append the elements onto itself
    password = ""


    #Splitting the Upper,Lower and special character strings and converting each character into an object in a list
    lcpool, ucpool, sppool = lc.split(" "), uc.split(" "), sp.split(" ")


    #Looping to append random characters into a list
    for i in range(0,lenght):

        #Picking Lowercase characters
        finallist.append(random.choice(lcpool))

        #Picking Uppercase characters
        finallist.append(random.choice(ucpool))

        #Picking Special characters
        finallist.append(random.choice(sppool))


    #Shuffling the characters in the list
    random.shuffle(finallist)


    #Appending all the elements of the list into the empty string
    for i in range(lenght):
        password += finallist[i]

    #Returning the password as a string
    return password


#Creating an object for the method
password = createpass(lenght)


#Outputting the password
print("Your password is : "+password)