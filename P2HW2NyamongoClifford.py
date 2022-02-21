#CTI-110
#P2HW2-Score Avg
# Nyamongo Clifford
#February, 19 2022
studentScores = []

#print the 7 scores
x = input('Enter score: ')
x= float(x)
studentScores.append(x)
x1= input('Enter score: ')
x1= float(x1)
studentScores.append(x1)
x2= input('Enter score: ')
x2= float(x2)
studentScores.append(x2)
x3 = input('Enter score: ')
x3 = float(x3)
studentScores.append(x3)
x4 = input('Enter score: ')
x4 = float(x4)
studentScores.append(x4)
x5 = input('Enter score: ')
x5 = float(x5)
studentScores.append(x5)
x6 = input('Enter score: ')
x6 = float(x6)
studentScores.append(x6)
print('--------------Results--------------')
lowScore = min(studentScores)
print('Lowest score:' + str(lowScore))
studentScores.remove(lowScore)
print('modified list:' + str(studentScores))
#print(str(studentScores))
avgScore = sum(studentScores)/len(studentScores)
print('scores Average: ' + str(avgScore))
print('------------------------')



