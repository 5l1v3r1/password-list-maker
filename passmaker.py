import os

data_list = []
word_list = []
characters = []

def add(word, met):
    if word == 's':
        pass
    elif word == 'S':
        pass
    else:
        if met == 'data':
            data_list.append(word)
        elif met == 'word':
            word_list.append(word)
        elif met == 'characters':
            characters.append(word)

def get_data():
    print ("\033[1;35m  skip and next =>  S+Enter \033[1;m"+'\n')

    add(input("\033[1;32mName: "), 'data')
    
    add(input("Last Name: "), 'data')
    
    add(input("Age : "), 'data')
    
    job = input("Nick name & name page : ")
    
    if len(job) == 10:
        add(job, 'word')
        
        add(job, 'data')
        
    elif len(job) > 10:
        add(job, 'word')
        
        add(job, 'data')
    else:
        add(job, 'data')
    birthday = input("Birthday (1371/01/01) : ")
    if birthday == 's':
        pass
    elif birthday == 'S':
        pass
    else:
        if '/' in birthday:
            birthday_s = birthday.split("/")
            if len(birthday_s) == 3:
                add(birthday_s[0]+birthday_s[0], 'word')
                add(birthday_s[2], 'data')
            else:
                pass
        else:
            pass
    while True:
        x = input("Phone Number ( Next: N+Enter ): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 10:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 10:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 10:
                add(x, 'data')
    while True:
        x = input("add name page ( Next: N+Enter ): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 10:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 10:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 10:
                add(x, 'data')
    while True:
        x = input("More add name ( Next: N+Enter ): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            add(x, 'characters')
banner = '''
\033[1;31m     Name
        Age
       name page     \033[1;m  \033[1;34m 
                    ●
                    ● ●
                     | |
        ___          | |
     (_______)  _____| |__
     \       /  |  Password  |
      \     /   |    List    |
       \   /____|  Generator |_______
       |__________________________   |
                                  |  |
                             _||||______
                            |■■■■■■■■■■■■■■■|\033[1;m
\033[1;m
 \033[1;33m  Telegram: t.me/Hackgm   \033[1;m  \033[1;31m | 1234510  |
\033[1;33m   https://github.com/HACKGM \033[1;31m | abcd123  | 
                         \033[1;31m     | 13701370 | \033[1;m
                         \033[1;31m     | •••••••  | \033[1;m
                          \033[1;31m    | •••••••  | \033[1;m
                          \033[1;31m    |__________| \033[1;m

'''
def generat_save():
    f = open('passwords.txt', 'a')
    for wr in word_list:
        f.write(wr+'\n')
    for da1 in data_list:
        for da2 in data_list:
            for chra in characters:
                f.write(da1+da2+'\n')
                f.write(da1+chra+da2+'\n')
    f.close()
    print ("\033[1;35m  Password List saved in  passwords.txt \033[1;m"+'\n')

if __name__ == '__main__':
    os.system('clear')
    print (banner)
    get_data()
    generat_save()

