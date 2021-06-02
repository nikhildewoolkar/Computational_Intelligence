Honesty = {"Nikhil": 0.2, "Nancy": 0.3, "Ayush": 0.6, "Sahil": 0.6, "Akash": 0.5}
Sincerity = {"Nikhil": 0.9, "Nancy": 0.9, "Ayush": 0.4, "Sahil": 0.5, "Akash": 0.4}
print('The Honesty of Students is represented as :', Honesty)
print('The Sincerity of Students is represented as :', Sincerity)
# (ab)'=a'+b' or (a+b)'=a'b'
def compliment(num):
    return(1-num)
def union(num1,num2):
    return(max(num1,num2))
def intersection(num1,num2):
    return(min(num1,num2))
print("proving (A ∪ B)' = A' ∩ B' ")
for H, S in zip(Honesty, Sincerity):
    lhs=compliment(union(Honesty[H],Sincerity[S]))
    rhs=intersection(compliment(Honesty[H]),compliment(Sincerity[S]))
    if(lhs==rhs):
        print("Pass")
    else:
        print("Fail")
print("")
print("proving (A ∩ B)' = A' ∪ B' ")
for H, S in zip(Honesty, Sincerity):
    lhs=compliment(intersection(Honesty[H],Sincerity[S]))
    rhs=union(compliment(Honesty[H]),compliment(Sincerity[S]))
    if(lhs==rhs):
        print("Pass")
    else:
        print("Fail")