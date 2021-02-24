# moduls
import os
import time


# sessions timing
def timer_config(round = 3, focus = 25, short_break = 5, long_break = 30,): # in the end change this value to sec
    ''' calculate's the sesions'''
    for r in range(round):
        os.system('>/dev/null 2>&1 play sounds/service-login.oga')
        timer_display(focus,'round{}.\'.FOCUS.\'.'.format(r+1))
        
        # logical error: the last cycle shoudn't show the short break and show long break
        os.system('>/dev/null 2>&1 play sounds/service-logout.oga')
        timer_display(short_break,'round{}: short BREAK'.format(r+1))
    
    # print('LONG BREAK BABY')
    os.system('>/dev/null 2>&1 play sounds/complete.oga')
    timer_display(long_break,'LONG BREAK BABY')
    os.system('>/dev/null 2>&1 play sounds/complete.oga')

# saving data
def save_log(type_activity= str, 
            description= str, 
            round = 3, 
            focus = 25, 
            short_break = 5,
            long_break = 30,):

    with open('data/data.csv', 'a') as datafile:
        timing = time.localtime()
        
        # type_activity
        datafile.write(type_activity)
        datafile.write(',')

        # description
        datafile.write(description)
        datafile.write(',')

        # round
        datafile.write(str(round))
        datafile.write(',')

        # focus time
        datafile.write(str(focus))
        datafile.write(',')

        # short break
        datafile.write(str(short_break))
        datafile.write(',')

        # long break
        datafile.write(str(long_break))
        datafile.write(',')

        # date
        datafile.write('{}/{}/{}'.format(timing[0],timing[1],timing[2]))
        datafile.write(',')

        # time
        datafile.write('{}:{}:{}'.format(timing[3],timing[4],timing[5]))
        datafile.write('\n')


# starting program
def start():
    ask = input('defualt setting?(y/n) ').lower()
    print('type of activity:\n\t- coding\n\t- study')
    type_act = input('what type of activity is your session? ')
    des = input('describe your activity? ')

    if ask == 'n':
        ro = int(input('how many round do you want to focus? '))
        fo = int(input('focus time: '))
        sb = int(input('short break: '))
        lb = int(input('long break: '))

        save_log(type_act,des,ro,fo,sb,lb)
        timer_config(round = ro, focus=fo, short_break= sb, long_break=lb)
    else:
        save_log(type_act,des)
        timer_config()


# count down timer
def timer_display(time_, session = str):
    i = 0
    j = 0
    k = 0
    l = 0
    for _ in range(time_ * 60): 
        os.system('clear')
        print(session)
        print("{3}{2}:{1}{0}".format(i,j,k,l))
        time.sleep(1)
        i += 1
        if i == 10:
            i = 0
            j += 1
            if j == 6:
                j = 0
                k += 1
                if k == 10:
                    k = 0
                    l += 1
        else:
            pass


    


if __name__ == "__main__":
    start()
    
    