#Average class grade

def calAverage(Score1,Score2, Score3, Score4, Score5, Score6, Score7, Score8,Score9,Score10 ):
    Average = (Score1 + Score2 + Score3 + Score4 + Score5 + Score6 + Score7 + Score8 + Score9 + Score10)
#Name of Students in class


#How grades are calculated
def determineGrades(StudentScore):
    if (StudentScore < 60):
        return "F"
    elif(StudentScore < 70):
        return "D"
    elif(StudentScore < 80):
        return "C"
    elif(StudentScore < 90):
        return "B"
    elif(StudentScore < 101):
        return "A"
#Get student test/grades score form user
def askforscores() -> object:
    Score1 = float ( input ( "Please enter score one" ) )
    Score2 = float ( input ( "Please enter score two" ) )
    Score3 = float ( input ( "Please enter score three" ) )
    Score4 = float ( input ( "Please enter score four" ) )
    Score5 = float ( input ( "Please enter score five" ) )
    Score6 = float ( input ( "Please enter score six" ) )
    Score7 = float ( input ( "Please enter score seven" ) )
    Score8 = float ( input ( "Please enter score eight" ) )
    Score9 = float ( input ( "Please enter score nine" ) )
    Score10 = float ( input ( "Please enter score ten" ) )

#Get student names from user
def Askfornames():
    name1 = float ( input ( "Please enter name one" ) )
    name2 = float ( input ( "Please enter name two" ) )
    name3 = float ( input ( "Please enter name three" ) )
    name4 = float ( input ( "Please enter name four" ) )
    name5 = float ( input ( "Please enter name five" ) )
    name6 = float ( input ( "Please enter name six" ) )
    name7 = float ( input ( "Please enter name seven" ) )
    name8 = float ( input ( "Please enter name eight" ) )
    name9 = float ( input ( "Please enter name nine" ) )
    name10 = float ( input ( "Please enter name ten" ) )



def printTableofResults( Score1 ,Score2, Score3 , Score4, Score5, Score6, Score7, Score8,Score9,Score10):
    print("\nScore\t Letter Grade", Askfornames())
    print(str(Score1)+"\t"+determineGrades(Score1),str(Score2)+"\t"+determineGrades(Score2),\
          str (Score3) + "\t" + determineGrades (Score3),str(Score4)+"\t"+determineGrades(Score4),\
          str (Score5) + "\t" + determineGrades (Score5),str(Score6)+"\t"+determineGrades(Score6),\
          str (Score7) + "\t" + determineGrades (Score7),str(Score8)+"\t"+determineGrades(Score8),\
          str (Score9) + "\t" + determineGrades (Score9),str(Score10)+"\t"+determineGrades(Score10))


def main():
    Score1 , Score2 , Score3 , Score4 , Score5 , Score6 , Score7 , Score8 , Score9 , Score10 = askforscores()
    printTableofResults()

main()







