# You are given a string .
#  contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format

# A single line of input contains the string .

# Constraints

# Output Format

# Output the sorted string .

# Sample Input

# Sorting1234
# Sample Output

# ginortS1324
a=input()
low=''
upp=''
en=[]
on=[]
for i in a:
    if i.islower():
        low+=i
    elif i.isupper():
        upp+=i
    elif (i).isnumeric():
        if int(i)%2==0:
            en.append(int(i))
        else:
            on.append(int(i))
low=''.join(sorted(low))
upp=''.join(sorted(upp))
on=''.join(map(str,sorted(on)))
en=''.join(map(str,sorted(en)))
print(low+upp+on+en)
