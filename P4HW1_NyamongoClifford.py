#CTI-110
# P4HW1 - Score List
# NYamongo Clifford A
#2022/03/21
#
Students_No = int(input('Enter the number of scores you wish to enter?: '))


scoreList=[]
                               #Create a for loop that only validate the score between zero and 100
for i in range(Students_No):
    score = int(input("Enter Score #" + str(i + 1) + ": "))

    while score < 0 or score > 100:
        print('INVALID ENTRY!!!')
        print('Should have entered between 0 and 100' )
        score = int(input('Score should be between 0 and 100?: '))

    scoreList.append(score)

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








