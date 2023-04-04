# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:

# banana.png

# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# Constraints



# Sample Input

# BANANA
# Sample Output

# Stuart 12
# Note :
# Vowels are only defined as . In this problem,  is not considered a vowel.


def minion_game(s):
    # i=1;j=0;x='';c=[];vow='aAeEiIoOuU'
    # while i<len(s)+1:
    #     while j<len(s)-i+1:
    #         t=j+i-1
    #         k=j
    #         while k<t+1:
    #             x=x+(str(s[k]))
    #             k+=1
    #         c.append(x)
    #         x=''
    #         j+=1
    #     j=0
    #     i+=1
    # cv=0;cnv=0;
    # for i in c:
    #     if i[0] in vow:cv=cv+1 
    #     else: cnv+=1
    # if cnv>cv:
    #     print('Stuart '+str(cnv))
    # elif cnv<cv:
    #     print('Kevin '+str(cv))
    # else:
    #     print('DRAW')
    # x='';vow='AEIOU';cv=0;cnv=0;
    # for i in range (1,len(s)+1):
    #     for j in range (len(s)-i+1):
    #         t=j+i-1
    #         for k in range(j,t+1):
    #             x+=str(s[k])
    #         if x[0] in vow: cv+=1
    #         else: cnv+=1
    #         x=''
    # if cv==cnv:print('Draw')
    # elif cv<cnv:print('Stuart '+str(cnv))
    # else:print('Kevin '+str(cv))
    l=len(s)
    vowel = 0
    consonant = 0
     
    for i in range(l):
        if s[i] in 'AEIOU':
           vowel+=(l-i)
        else:
           consonant+=(l-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)