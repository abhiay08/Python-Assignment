'''3.B.3: ASSIGNMENT
PROBLEM STATEMENT
1. Write a function that takes a variable number of lists as input, the lists will contain runs scored by players in
an over (i.e. 6 entries). The function should assume the first entry is for Player1, second entry is for Player 2 and
so on…
How to take a list from the user ?
User is supposed to enter scores like: 2,2,4,0,0,6 ‘Enter Key’
On enter ask if they want to add scores of another player (y/n), if the user responds with y, they should be able to
 add another entry.
If a user enters less than 6 scores, assume that other balls had no runs scored.
If a user enters more than 6 scores, consider only the first 6.
_ '''
# Code Created by Abhishek Yadav

while True:
      players_score=[]
      score=input("\n Enter the Player Score & it should be separated ',' :")
      players_score=score.split(",")
      score=[int( score)for score in players_score]
      while len(players_score)<6:
       players_score.append(0)
      players_score=players_score[:6]
      print(players_score)
      
      more=input("Do you want more players to add: ")
      if more.lower()!='y':
       break
      