from default import Spy
from default import spy
from default import friend
import sys

#======================================select a friend function===================================
def select_a_friend():
    item_num=0
    for frnd in friend:
        print('%d. %s'%(item_num+1,frnd.name))
        item_num=item_num+1
    friend_choice=int(input('Enter a Friend of your choice:'))
    frnd_pos=friend_choice-1
    return frnd_pos
#======================================show friend============================================
def show():
    for ele in friend:
        print(ele.name)


#======================================Add friend================================================================
def add_friend():
    new_friend = Spy('','',0,0.0)
    new_friend.name= raw_input('Enter your friend name: ')
    new_friend.salutation=raw_input('Enter your friend salutation:')
    new_friend.age = int(input('Enter your friend age: '))
    new_friend.rating = float(input('Enter your ratings: '))
#    present_status = True
    if len(new_friend.name) > 0 and new_friend.name.isalpha() and new_friend.age> 13 and new_friend.age< 90 :
        friend.append(new_friend)
    else:
        print("your entered details dosen't match with ur friend ")


    return len(friend)

#======================================Start chat function===================================

def start_chat(spy):

    current_status_message = None

    show_menu = True

    while show_menu == True:

        menu =""" **********MENU**********
        1.Status Update.
        2.Add Friend.
        3.Show Friend.
        4.Send a Message.
        0.exit\nEnter your choice :"""
        menu_choice=int(input(menu))
        if menu_choice==1:
          print('You select to status update')
          spy.current_status_message = add_status(spy.current_status_message)
          print('you have set %s as your status'%spy.current_status_message)
        elif menu_choice==2:
          print('you selected to Add Friend')
          total = add_friend()
          print('%s succesfully added as your friend'%friend[len(friend)-1].name)
          print('you have %d total friend now'%total)

        elif menu_choice==3:
          print('you have selected to show friend')
          a=show()

        elif menu_choice==4:
            print('Your select to send message')
            a=select_a_friend()

        elif menu_choice==0:
            show_menu = False
            sys.exit()
        else:
            print('Invalid choice\nplease try again...!!!')

#==================================Add status function===================================================
def add_status(current_status_message):

    if current_status_message != None:
        print(' your status is \n %s'%current_status_message)
    else:
        print('you don\'t have any status')
    default = raw_input('do u want to select from older/ default status(y/n)?')
                                                                                #asking user choice
    if default.upper() == 'N':

        new_status_message = raw_input('Whats on your mind ?')                      #reading new status

        if len(new_status_message) > 0:                                         #validation
            updated_status_message = new_status_message
            STATUS_MSG.append(updated_status_message)                           #append status
        else:
            print('u have not entered anything\n please try again ')

    elif default.upper() =='Y':

        item_pos=1
        for msg in STATUS_MSG:
            print(str(item_pos)+ '. ' + msg)
            item_pos= item_pos + 1

        status_sel = int(input('enter the status of your choice :'))

        if status_sel <= len(STATUS_MSG):
            updated_status_message = STATUS_MSG[status_sel-1]
        else:
            print('u have entered invalid choice')
    else:
            print('invalid choice')

    return updated_status_message
#==================================Main project===============================================================


question= 'Do you want to continue with your default user(y/n)?'
choice=raw_input(question)

STATUS_MSG = ["Busy", "At GYM", "Can\'talk"]
if choice =='Y' or choice == 'y':

    start_chat(spy)

elif choice =='N' or choice =='n':

    print('Welcome to spychat \n you must tell me your name first')
    spy.name = raw_input('Enter your name:')
    if len(spy.name)>0 and spy.name.isalpha():
        spy.salutation = raw_input('Hello ' + spy.name + ' what should i call you (Mr/Miss?:')
        spy.name = spy.salutation + ' ' +     spy.name
        print('Welcome ' +  spy.name + ' I need some details before you get started')
        spy.age =input('Enter your age: ')
        spy.age = int(spy.age)
        if spy.age>13 and spy.age<60:
            spy.rating = input('Enter ur Ratings:')
            spy.rating = float(spy.rating)
            if spy.rating<5.0:
                print('Profile created succesfully \nName: ' +spy.name + ' \nAge: ' +str(spy.age) +' \n Rating: '+str(spy.rating) )
                print('Proud to have you onboard')
                start_chat(spy)
            else:
                print("Invalid Ratings")
        else:
            print("Sorry! you age are not able to create account")
    else:
        print("Sorry!Please enter a valid name")

else:
        print('Sorry! Invalid choice')
