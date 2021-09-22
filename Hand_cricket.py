import random

class Hand_cricket():
     def intro(self):
          print('''     *** Lets play hand cricket with satish ***
we think you were familiar with RULES
This is just like t20 you only get 20 balls

lets go for toss  >>>''')
          
     def toss(self,p1,eo):
          
          s1=random.randint(0,9)
          print('My number is : ',s1)
          if ((p1+s1)%2 ==0 and eo=='even') or ((p1+s1)%2 != 0 and eo=='odd'):
               print('You win the toss')
               c=input("choose bat or bowl ")
          else:
               print('You lose the toss')
               print('And I choose bat first')
               c='bowl'
          return c

     
class first_innings(Hand_cricket):
     def batting(self):
          score=0
          i=1
          while(i<=20):
               bowl_runs=random.randint(0,9)
               print("no. of balls: ",i)
               bat_runs=int(input('enter a number for batting : '))
               if bat_runs>9 or bat_runs<0:
                    print('enter a valid number between 0-9')
                    bat_runs=int(input('enter a number for batting : '))
               if bat_runs == bowl_runs:
                    print("Wicket")
                    return score
               
               else:
                    score += bat_runs
               i += 1
               
          print('Match over')
          return score
    
     def bowling(self):
          score =0
          i=1
          while(i<=20):
               print("no. of balls: ",i)
               bowl_runs=int(input('enter a number for bowling : '))
               if bowl_runs>9 or bowl_runs<0:
                    print('enter a valid number between 0-9')
                    bat_runs=int(input('enter a number for bowling : '))
                    
               bat_runs=random.randint(0,9)
               if bat_runs == bowl_runs:
                    print("Wicket")
                    return score
               
               else:
                    score += bat_runs
               i += 1
          return score

     
class second_innings(first_innings):
     def batting(self,s):
          score=0
          i=1
          while(i<=20 and score <= s):
               print(s-score+1," runs to win in ",21-i," balls")
               bat_runs=int(input('enter a number for batting : '))
               if bat_runs>9 or bat_runs<0:
                    print('enter a valid number between 0-9')
                    bat_runs=int(input('enter a number for batting : '))
                    
               bowl_runs=random.randint(0,9)
               if bat_runs == bowl_runs:
                    print("Wicket")
                    print("you lost the match")
                    return
               
               else:
                    score += bat_runs
               i += 1
          if (score <= s):
               print("you lost the match by",s-score+1,"runs")
          else:
               print("You won the match")
          return

     
     def bowling(self,s):
          score=0
          i=1
          while(i<=20 and score <= s):
               print(s-score+1," runs to win in ",21-i," balls")
               bowl_runs=int(input('enter a number for bowling : '))
               if bowl_runs>9 or bowl_runs<0:
                    print('enter a valid number between 0-9')
                    bowl_runs=int(input('enter a number for bowling : '))
                    
               bat_runs=random.randint(0,9)
               print("my number is :",bat_runs)
               if bat_runs == bowl_runs:
                    print("Wicket")
                    print("you lost the match with Satish")
                    return
               
               else:
                    score += bat_runs
               i += 1
          if (score <= s):
               print("you lost the match by",s-score+1,"runs")
          else:
               print("You won the match")
          return

     

          

if __name__ == "__main__":
     a=1
     while(a==1):
          p1=first_innings()
          p2=second_innings()
          p2.intro()
          eo=input("choose one from even or odd : ")
          p=int(input("choose a number between 0 to 9 for toss: "))
          choice=p1.toss(p,eo)
          if choice == 'bat':
               print('1st innings starts.   Lets play')
               score1=p1.batting()
               print('score is :',score1,"\n")
               print("Score ",score1+1," runs to win in 20 balls")
               print()
               print('2nd innings starts')
               p2.bowling(score1)
          
          else:
               print("You choose bowl first.   Lets play")
               score1=p1.bowling()
               print("Score is : ",score1,"\n")
               print("Score ",score1+1," runs to win in 20 balls")
               p2.batting(score1)

          a=int(input("Enter 1 to play again with satish or any other number to exit:"))
          print("\n")



