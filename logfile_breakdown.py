#
# Michael Winder
# SEC 290 Summer B2
# hwk6_step1.py
# August 15, 2020
#

user_count = {}

file_name = 'auth.log.1.txt'

# Open the file and read it
with open(file_name) as f:
#Now we need to iterate through the list to find lines we want
    for line in f:
        #Find just the lines with 'Failed password' issues
        if "Failed password" in line:
            #Now lets find the user name of the account with an issue
            begin_user_name = line.find('invalid user ')
            start_user_name = len('invalid user ') + begin_user_name
            end_user_name = line.find('from ')
            #Slice the user name out of the string
            user_name = line[start_user_name:end_user_name:]
            #See if user name is already in the dictionary, if it is increase value
            #if it isn't add it in.
            if user_name in user_count:
                user_count[user_name] += 1
            else:
                user_count[user_name] = 1
    #Let's print the dictionary as nice as possible
    #Would like to find a better way to do this, maybe multiple per line???
    for key, value in user_count.items():
        print(key, ' : ', value)
    
#Make sure to close the file        
f.close()
