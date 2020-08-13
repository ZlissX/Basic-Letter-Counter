while True:
    passs=str(input('Please enter your passage here:'))
    letinpass=0#letinpass is the total number of letters
    let=0#to check if the letter is a number and deduct from the letter count
    amountofint=0
    lmfaoo=0#the amount of integers
    lmfaooo=0#the amount of letters

    for letterss in passs:
        try:
            if let==int(letterss):
                letinpass=letinpass-1
                amountofint=amountofint+1


        except:
                if letterss != ' ':
                    letinpass = letinpass+1

    print('the amount of letters in your passage:\n',letinpass)


    print(passs)

    Letter=(input('what letter do you want to find'))
    count=0
    for letters in passs:
        if letters==Letter:
            count += 1
    print(count)

    askint=((input('Type yes if you want to know the amount of integers and letters in the pass')).lower())#.lower() will convert all of them to lower case letters
    if askint == 'yes':
        for lett in passs:
            try:
                spare=int(lett)
                if spare==int(lett):
                    lmfaoo+=1
            except:
            #lmfaooo is the letter count
                lmfaooo+=1

        print('the amount of integers\n',lmfaoo)
        print('the amount of letters\n',lmfaooo)

    programexit=((input('do you want to exit the program ? if yes type yes or press enter:')).lower())#.lower() will convert all of them to lower case letters
    if programexit=='yes':
        exit()#this  will exit out of the program
