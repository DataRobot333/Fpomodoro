# moduls
import os
import time



# count down timer
def timer_display(time_, session = str, round= None):
    '''display a simple timer in screen for time_ period'''
    i = 0 # --:-i
    j = 0 # --:j-
    k = 0 # -k:--
    l = 0 # l-:--
    _ , column_terminal = os.popen('stty size').read().split()
    for _ in range(time_ * 60): # minute to second (*60)
        os.system('clear')

        if round:
            print(round)

        print(session.center(int(column_terminal), "~"))
        print()
        print("(( {3}{2}:{1}{0} ))".format(i,j,k,l).center(int(column_terminal))) #actual timer view
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


# sessions timing
def timer_config(round = 3, focus = 25, short_break = 5, long_break = 30,): # in the end change this value to sec
    ''' calculate's the sesions'''
    for r in range(round):
        os.system('>/dev/null 2>&1 play sounds/service-login.oga') # play sound without showing output
        timer_display(focus,
                      round = 'round {}'.format(r+1),
                      session = '.\'.FOCUS.\'.')
        
        if r == round-1: # last cycle don't need the short break
            os.system('>/dev/null 2>&1 play sounds/service-logout.oga')
            timer_display(short_break,
                         round = 'round {}'.format(r+1),
                         session = 'SHORT BREAK')
    
    os.system('>/dev/null 2>&1 play sounds/complete.oga')
    timer_display(long_break,session='LONG BREAK')
    os.system('>/dev/null 2>&1 play sounds/complete.oga') 


# saving data
def save_log(type_activity= str, 
            description= str, 
            round = 3, 
            focus = 25, 
            short_break = 5,
            long_break = 30,):
    '''save pomodoro session configuration in your data.csv file

    type_activity: description of what the general session is
    description: describe in detail what you do!
    round: how many fragment do you want to focus
    focus: focus time
    short_break: short break session time
    long_break: long break time
    '''
# future development:
# check if the file doesn't exist open a data.csv file with right headers
# if data.csv exist do the recording like below
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
    ask4setting = input('use defualt setting?(y/n) ').lower()
    print('Activity:\n\t- Project\n\t- Study\n\t- Code Puzzle\n\t- Course') # you can add your own personal session part
    type_act = input('What type of activity is your session? ')
    des = input('Describe your Activity? ')

    if ask4setting == 'n':  
        ro = int(input('How many round do you want to focus? '))
        fo = int(input('Focus Time: '))
        sb = int(input('Short Break: '))
        lb = int(input('Long Break: '))

        save_log(type_activity = type_act,
                 description = des,
                 round = ro,
                 focus = fo,
                 short_break = sb,
                 long_break = lb)
        timer_config(round = ro, focus=fo, short_break= sb, long_break=lb)
    else:
        save_log(type_act,des)
        timer_config()



if __name__ == "__main__":
    start()
    
    