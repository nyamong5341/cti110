# A program used to find grades of students given their scored
# Nyamongo

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    # score = int(input('Enter grade: '))
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    E_score = 50
    # TO DO: define the rest of the scores
    score = int(input('Enter grade: '))

    if score >= A_score :
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')  # TO DO: finish this




if __name__ == "__main__":
    main()

