# Suppose a genetic algorithm uses chromosomes of the form x = abcdefgh
# with a fixed length of eight genes. Each gene can be any digit between 0
# and 9. Let the fitness of individual x be calculated as:
# f(x) = (a + b) − (c + d) + (e + f) − (g + h)

# ii) Cross the first and third fittest individuals (ranked 1st and 3rd)
# using a uniform crossover.BIS3226 4
# Answer: In the simplest case uniform crossover means just a
# random exchange of genes between two parents. For example, we
# may swap genes at positions a, d and f of parents x2 and x3:
# x2 = 8 7 1 2 6 6 0 1
# x3 = 2 3 9 2 1 2 8 5 ⇒
# O5 = 2 7 1 2 6 2 0 1
# O6 = 8 3 9 2 1 6 8 5
# ) Evaluate the fitness of each individual, showing all your workings, and
# arrange them in order with the fittest first and the least fit last.
# Answer:
# f(x1) = (6 + 5) − (4 + 1) + (3 + 5) − (3 + 2) = 9
# f(x2) = (8 + 7) − (1 + 2) + (6 + 6) − (0 + 1) = 23
# f(x3) = (2 + 3) − (9 + 2) + (1 + 2) − (8 + 5) = −16
# f(x4) = (4 + 1) − (8 + 5) + (2 + 0) − (9 + 4) = −19
# The order is x2, x1, x3 and x4.

import string
import random
print("enter no. of problems to be solved :-")
n=int(input())
d=[]
for i in range(n):
    print("x",i,":- ")
    x=input()
    d.append(x)
out=[]
for i in range(len(d)):
    fx= (int(d[i][0])+int(d[i][1]))-(int(d[i][2])+int(d[i][3]))+(int(d[i][4])+int(d[i][5]))-(int(d[i][6])+int(d[i][7]))
    g=[fx,d[i]]
    out.append(g)
s=list(sorted(out,reverse=True))
for i in range(n):
    print("x",i,"=",s[i][0])
print("crossover function")
print("crossover of 2 data:-",s[0],s[2])
x1=list(s[0][1])
x2=list(s[2][1])
print("uniform crossover")
print("crossover of the same is:- ")
for j in range(2):
    s11=""
    for i in range(8):
        l1=random.choice(x1)
        l2=random.choice(x2)
        arr=[l1,l2]
        s11+=random.choice(arr)
    print("O",j,":- ",s11)
# 65413532        
# 87126601
# 23921285
# 41852094