
def collect_scores(Students):
    scoreList=[]

    for i in range(Students):
        score = int(input("Enter Score #" + str(i + 1) + ": "))

        while score < 0 or score > 100:
            print('INVALID ENTRY!!!')
            print('Should have entered between 0 and 100' )
            score = int(input('Score should be between 0 and 100?: '))

        scoreList.append(score)


    return scoreList

Students_No = int(input('Enter the number of scores:  '))
scoreList = collect_scores(Students_No)


def evaluate_scores(scoreList):
    lowest_Score = min(scoreList)
    scoreList.remove(lowest_Score)
    average = sum(scoreList) / (Students_No - 1)


    print(scoreList)                             #output score list
    print('Lowest score: ' + str(lowest_Score))   #output lowest score
    print('modified list: ' + str(scoreList))     # output lowest score after removing the lowest score
    print('Scores average: ' + str(average))

    # system uses 10-point grading scale
    if average>=90 and average<=100:
        print('Grade = A')
    elif average>=80 and average<90:
        print('Grade = B')
    elif average>=70 and average<80:
        print('Grade = C')
    elif average>=60 and average<70:
        print('Grade = D')
    elif average>=50 and average<60:
        print('Grade = E')
    else:
        print('Grade = F')


evaluate_scores(scoreList)

#Menu Display
print('----------MENU-------------')
print('(1) Create score List')
print('(2) Display results')
print('(3) Exit')
print('---------------------------')

Choice = int(input('Enter the choice between (1,2 and 3): '))

# Program 1 creates the score list
def program_1():
    def collect_scores(Students):
        scoreList=[]

        for i in range(Students):
            score = int(input("Enter Score #" + str(i + 1) + ": "))

            while score < 0 or score > 100:
                print('INVALID ENTRY!!!')
                print('Should have entered between 0 and 100' )
                score = int(input('Score should be between 0 and 100?: '))

            scoreList.append(score)

        return scoreList

    Students_No = int(input('Enter the number of scores:  '))
    scoreList = collect_scores(Students_No)
    return scoreList

Choice = int(input('Enter the choice between (1,2 and 3): '))

if Choice==1:
    result_1=program_1()
    print(result_1)


#Choice = int(input('Enter the choice between (1,2 and 3): '))

#Display Results

def program_2():
    def evaluate_scores(scoreList):
        lowest_Score = min(scoreList)
        scoreList.remove(lowest_Score)
        average = sum(scoreList) / (Students_No - 1)
        print(scoreList)                             #output score list
        print('Lowest score: ' + str(lowest_Score))   #output lowest score
        print('modified list: ' + str(scoreList))     # output lowest score after removing the lowest score
        print('Scores average: ' + str(average))
    average = sum(scoreList) / (Students_No - 1)
    # system uses 10-point grading scale
    if average>=90 and average<=100:
        print('Grade = A')
    elif average>=80 and average<90:
        print('Grade = B')
    elif average>=70 and average<80:
        print('Grade = C')
    elif average>=60 and average<70:
        print('Grade = D')
    elif average>=50 and average<60:
        print('Grade = E')
    else:
        print('Grade = F')
    return scoreList


evaluate_scores(scoreList)

Choice = int(input('Enter the choice between (1,2 and 3): '))
if Choice==2:
    result_2=program_2()
    print(result_2)



# If else statement to exit the program
while Choice !=3:
    if Choice==1:
        result_1=program_1()
        print(result_1)
        Choice = int(input('Enter the choice between (1,2 and 3): '))
    elif Choice==2:
        pass
        Choice = int(input('Enter the choice between (1,2 and 3): '))
    else:
        print('Error Input')
        Choice = int(input('Enter the choice between (1,2 and 3): '))






