
#call in the packages we  need
import os
import csv

#create path to the csv
csvpath = os.path.join('Resources', 'election_data.csv')

#variables used later for totaling votes
Khanv=0 
Correyv=0
Liv=0
Tolleyv=0

with open(csvpath) as csvfile:

    
        csv_reader = csv.reader(csvfile, delimiter=',')
        #removes header
        header=next(csv_reader)
        vote=[]
        canidates=[]
        #creates a list  out of the  canidate data
        for lines in csv_reader:
                vote.append(str(lines[2]))
        total=(len(vote))
        #finds  all unique  canidates
        for lines  in vote:
                if lines not in canidates:
                        canidates.append(str(lines))
        #counts  the number of votes for each canidate
        for lines in vote:
                if lines=="Khan":
                        Khanv=Khanv+1
                elif lines=="Correy":
                        Correyv=Correyv+1
                elif lines=="Li":
                        Liv=Liv+1
                elif lines=="O\'Tooley":
                        Tooleyv=Tolleyv+1

     
        #calculates vote percantages
        Kp=Khanv/total
        Cp=Correyv/total
        Lp=Liv/total
        Tp=Tooleyv/total      
        #prints voting information 
        print("Total Votes:"+str(total))
        print(f"Khan: {round(100*Kp,2)}% {Khanv}")
        print(f"Correy: {round(100*Cp,2)}% {Correyv}")
        print(f"Li: {round(100*Lp,2)}% {Liv}")
        print(f"O'Tooley: {round(100*Tp,2)}% {Tooleyv}")
        #calcultates and  then ptints winner
        if Khanv > Correyv and Khanv > Liv and Khanv > Tooleyv:
                print("Winner: Khan")
        elif Correyv > Khanv and Correyv > Liv and Correyv > Tooleyv:
                print("Winner: Correy")
        elif Liv > Khanv and Liv > Correyv  and Liv > Tooleyv:
                print("Winner: Li")
        else:
                print("Winner: O'tooley")
        #creates text file
        file=open("Poll.txt","w+")
        file.write(f"Total Votes:{total}  Khan: {round(100*Kp,2)}% {Khanv}  Correy: {round(100*Cp,2)}% {Correyv}  Li: {round(100*Lp,2)}% {Liv}  O'Tooley: {round(100*Tp,2)}% {Tooleyv}")

        

        