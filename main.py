from steganography.steganography import Steganography
from default import Spy
from default import spy
from default import friend
import sys
import csv

#===================================load_friend funtion=========================================
def load_friend():
    with open('db.csv','rb')as frnd_data:
        reader = csv.reader(frnd_data)
        for row in reader:
            new_friend=Spy(row[0],row[1],row[2],row[3])
            friend.append(new_friend)

#======================================select a friend function===================================
def select_a_friend():
    item_num=0
    for frnd in friend:
        print('%d. %s'%(item_num+1,frnd.name))
        item_num=item_num+1
    friend_choice=int(input('Enter a Friend of your Choice:'))
    frnd_pos=friend_choice-1
    return frnd_pos

#===================================send a message========================================
def send_message():
    friend_choice = select_a_friend()
    original_img = raw_input('Enter the name of your image:\n')
    output_path = 'output.jpg'
    text = raw_input('Enter your Secret Message:')
#    Steganography.encode(original_img,output_path,text)
    print('Your Message has been send Successfully')
#================================read message==================================================
def read_msg():
    sender = select_a_friend()
    output_path = raw_input('What is the name of your File:')
    secret_text = Steganography.decode(output_path)
    print(friend[sender].name+':'+secret_text)
#======================================show friend============================================
def show():
    for ele in friend:
        print(ele.name)


#======================================Add friend================================================================
def add_friend():
    new_friend = Spy('','',0,0.0)
    new_friend.name= raw_input('Enter your Friend Name: ')
    new_friend.salutation=raw_input('Enter your Friend Salutation:')
    new_friend.age = int(input('Enter your Friend Age: '))
    new_friend.rating = float(input('Enter your Ratings: '))
#    present_status = True
    if len(new_friend.name) > 0 and new_friend.name.isalpha() and new_friend.age> 13 and new_friend.age< 90 :
        friend.append(new_friend)
        with open('db.csv','a') as frnd_data:
            writer = csv.writer(frnd_data)
            writer.writerow([new_friend.name,new_friend.salutation,new_friend.age,new_friend.rating])
    else:
        print("Your Entered Details dosen't match with your Friend ")


    return len(friend)

#======================================Start chat function===================================

def start_chat(spy):

    current_status_message = None

    show_menu = True
    load_friend()

    while show_menu == True:

        menu =""" **********MENU**********
    1. Status Update.
    2. Add Friend.
    3. Show Friend.
    4. Send a Message.
    5. Read a Message.
    0. Exit\nEnter your Choice :"""
        menu_choice=int(input(menu))
        if menu_choice==1:
          print('You select to Status Update.')
          spy.current_status_message = add_status(spy.current_status_message)
          print('You have Set %s as your Status'%spy.current_status_message)
        elif menu_choice==2:
          print('You selected to Add Friend')
          total = add_friend()
          print('%s Succesfully Added as your Friend'%friend[len(friend)-1].name)
          print('you have %d total friend now'%total)

        elif menu_choice==3:
          print('You have selected to Show Friend')
          a=show()

        elif menu_choice==4:
            send_message()

        elif menu_choice==5:
            read_msg()

        elif menu_choice==0:
            show_menu = False
            sys.exit()
        else:
            print('Invalid Choice\nplease try again...!!!')

#==================================Add status function===================================================
def add_status(current_status_message):

    if current_status_message != None:
        print(' your status is... \n %s'%current_status_message)
    else:
        print('You Don\'t have any Status.')
    default = raw_input('Do You want to Select from Older / Default Status(y/n) ?')
                                                                                #asking user choice
    if default.upper() == 'N':

        new_status_message = raw_input('Whats on your mind ?')                      #reading new status

        if len(new_status_message) > 0:                                         #validation
            updated_status_message = new_status_message
            STATUS_MSG.append(updated_status_message)                           #append status
        else:
            print('You have not Entered Anything\n please try again... ')

    elif default.upper() =='Y':

        item_pos=1
        for msg in STATUS_MSG:
            print(str(item_pos)+ '. ' + msg)
            item_pos= item_pos + 1

        status_sel = int(input('Enter the Status of your Choice :'))

        if status_sel <= len(STATUS_MSG):
            updated_status_message = STATUS_MSG[status_sel-1]
        else:
            print('You have Entered Invalid Choice.')
    else:
            print('Invalid Choice.')

    return updated_status_message
#==================================Main project===============================================================


question= 'Do you want to continue with your Default User (y/n) ?'
choice=raw_input(question)

STATUS_MSG = ["Available","Busy", "At GYM", "Can\'talk"]
if choice =='Y' or choice == 'y':

    start_chat(spy)

elif choice =='N' or choice =='n':

    print('Welcome to Spychat \n You must tell me your Name First')
    spy.name = raw_input('Enter your Name:')
    if len(spy.name)>0 and spy.name.isalpha():
        spy.salutation = raw_input('Hello ' + spy.name + ' What should I Call You (Mr/Miss?:')
        spy.name = spy.salutation + ' ' +     spy.name
        print('Welcome ' +  spy.name + ' I need some Details before you get Started.')
        spy.age =input('Enter your age: ')
        spy.age = int(spy.age)
        if spy.age>13 and spy.age<60:
            spy.rating = input('Enter your Ratings:')
            spy.rating = float(spy.rating)
            if spy.rating<5.0:
                print('Profile Created Succesfully. \nName: ' +spy.name + ' \nAge: ' +str(spy.age) +' \n Rating: '+str(spy.rating) )
                print('Proud to have You Onboard.')
                start_chat(spy)
            else:
                print("Invalid Ratings.")
        else:
            print("Sorry! Your Age are not able to Create Account.")
    else:
        print("Sorry!Please Enter a Valid Name.")

else:
        print('Sorry! Invalid choice.')
