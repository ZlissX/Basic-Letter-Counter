while True:
    passs=str(input('Please enter your passage here:'))
    letinpass=0#letinpass is the total number of letters
    let=0#to check if the letter is a number and deduct from the letter count
    amountofint=0
    Total_Numbers=0#the amount of integers
    Total_letters=0#the amount of letters
    punctuationmarks=0#the amount of punctuation marks in the passage
    notanumber=0
    

    for letterss in passs:
        
        if letterss in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?", "/", "<", ">","(",")","`","~","$",'#',"@","#","%","^","*","-","_","+","=","|","&","=","[","]","{","}"): #if the letters in the loop matches this it will deduct one from the totoal count
            letinpass=letinpass-1
        

        try:
            if let==int(letterss):
                letinpass=letinpass-1
                amountofint=amountofint+1


        except:
                if letterss != ' ':
                    letinpass = letinpass+1

    print('The Total amount of Letters:\n',letinpass)


    

    Letter=(input('what letter do you want to find ?'))
    print("you want to  find :" ,Letter)
    count=0
    

    for letters in passs:
        if letters==Letter:
            count += 1
    print(count)

    askint=((input('Type yes if you want to know the amount of integers,punctuation marks and letters in the passage:')).lower())#.lower() will convert all of them to lower case letters
    
    if askint == 'yes':
        for lett in passs:
            
            #the line below will count the amount of punctuaion marks in the passage
            if lett in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
                punctuationmarks+=1
            if lett in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?", "/", "<", ">","(",")","`","~","$",'#',"@","#","%","^","*","-","_","+","=","|","&","=","[","]","{","}"): #if the letters in the loop matches this it will deduct one from the totoal count
                Total_letters-=1
                
            try:
                spare=int(lett)
                if spare==int(lett):
                    Total_Numbers+=1
            except:
                if lett != ' ':
                    Total_letters=Total_letters+1
                
                
            #Total_letters is the letter count

    
                
        print('The amount of letters:\n',Total_letters)
        print('The amount of integers:\n',Total_Numbers)
        print('The amount of punctuation marks:\n',punctuationmarks)

    programexit=((input('do you want to exit the program ? if yes type yes or press enter:')).lower())#.lower() will convert all of them to lower case letters
    if programexit!='yes':
        print('restarting')
        continue
    if programexit=='yes':
        exit()#this  will exit out of the program


