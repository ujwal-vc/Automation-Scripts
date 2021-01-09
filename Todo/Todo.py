#!/usr/bin/env python3

import sys
import datetime as dt

with open('todo.txt','a')as f:
    f.close()
with open('done.txt','a') as f:
    f.close()

if len(sys.argv) ==1 or sys.argv[1]=='help':
    print('Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics`;')
    
elif sys.argv[1] == 'add':
    str1=' '
    if len(sys.argv)== 2:
        print('Error: Missing todo string. Nothing added!')
    else:
        with open('todo.txt', 'a') as filep:
            filep.write(sys.argv[2]+'\n')
        print('Added todo: '+'\"'+sys.argv[2]+'\"')
        

elif sys.argv[1]=='ls':
    with open('todo.txt','r') as filep:
        readfile=filep.readlines()
        sno=len(readfile)
        if sno!=0:
            for x in readfile[::-1]:
                print('['+str(sno)+ '] '+x,end='')
                sno-=1
        else:
            print("There are no pending todos!")

elif sys.argv[1]=='del':
    if len(sys.argv)==2:
        print("Error: Missing NUMBER for deleting todo.")
    elif int(sys.argv[2])>0 and int(sys.argv[2])<=len(sys.argv):
        print('hell at the night')
        with open('todo.txt','r') as filep:
            readfile=filep.readlines()
        done=readfile.pop(int(sys.argv[2])-1)
        with open('todo.txt','w')as filep:
            for x in readfile:
                filep.write(x)
        print('Deleted todo #'+str(sys.argv[2]))
    else:
        print('Error: todo #'+str(sys.argv[2])+' does not exist. Nothing deleted.') 
        
elif sys.argv[1]=='done':
    if len(sys.argv)==2:
        print("Error: Missing NUMBER for marking todo as done.")
    elif int(sys.argv[2])>0 and int(sys.argv[2])<=len(sys.argv):
        with open('todo.txt','r') as filep:
            readfile=filep.readlines()
        done=readfile.pop(int(sys.argv[2])-1)
        with open('todo.txt','w')as filep:
            for x in readfile:
                filep.write(x)
        today=dt.datetime.utcnow().strftime("%Y-%m-%d")
        with open('done.txt','a') as filep:
            filep.write('x '+str(today)+' '+done)
        print('Marked todo #'+str(sys.argv[2])+' as done.')
    else:
        print('Error: todo #'+str(sys.argv[2])+' does not exist.')             

elif sys.argv[1]=='report':
    with open('todo.txt','r') as f:
        pending=len(f.readlines())
    with open('done.txt','r') as f:
        completed=len(f.readlines())
    print(str(dt.datetime.utcnow().strftime("%Y-%m-%d"))+' Pending : '+str(pending)+' Completed : '+str(completed))
