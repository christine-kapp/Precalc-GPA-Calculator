# Precalc GPA Calculator

totalhwpts = int(input("Enter total possible homework points: "))
totalquizpts = int(input("Enter total possible quiz points: "))
totaltestpts = int(input("Enter total possible test points: "))
totalfinalpts = int(input("Enter total possible final exam points: "))
totalreviewpts = int(input("Enter total possible review quiz points: "))

hwpts = int(input("Enter total homework points earned: "))
quizpts = int(input("Enter total quiz points earned: "))
testpts = int(input("Enter total test points earned: "))
finalpts = int(input("Enter total final exam points earned: "))
reviewpts = int(input("Enter total review quiz points earned: "))

homework = (hwpts / totalhwpts)*0.05
quiz = (quizpts / totalquizpts)*0.12
test = (testpts / totaltestpts)*0.50
final = (finalpts / totalfinalpts)*0.32
review = (reviewpts / totalreviewpts)*0.01

total = homework + quiz + review + test + final
print(total)
