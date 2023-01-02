print("MCQ questions on UPSC Current Affairs")
playing = input("Do you want to play?\n")

if playing != "yes":
    quit()

print("Lets play \n")
score=0
while(True):
    answer=input("""1.Which is the first country to gather six of its astronauts in space?
    [A] USA
    [B] China
    [C] Russia
    [D] Israel\n""")
    if answer == "b":
        print("Correct Answer\n")
        score+=1
    else:
        print("Wrong Answer\n")
    loop=input("Do you want to keep playing?")
    if loop !="y":
        break
    answer=input("""Which cities are ranked at the top of the Economic Intelligence Unit releases Cost of Living Index 2022?
    [A] Singapore and Dubai
    [B] New York and Singapore
    [C] New York and Tokyo
    [D] Singapore and London\n""")
    if answer == "b":
        print("Correct Answer\n")
        score+=1
    else:
        print("Wrong Answer\n")
    loop=input("Do you want to keep playing?")
    if loop !="y":
        break
    answer=input("""Which Indian institution has been recently hit by an alleged ransomware attack?
    [A] SEBI
    [B] AIIMS
    [C] DRDO
    [D] UGC\n""")
    if answer == "b":
        print("Correct Answer\n")
        score+=1
    else:
        print("Wrong Answer\n")
    loop=input("Do you want to keep playing?")
    if loop !="y":
        break
    answer=input("""Beypore Uru is a flagship product of which state?
    [A] Odisha
    [B] Assam
    [C] Kerala
    [D] West Bengal\n""")
    if answer == "c":
        print("Correct Answer\n")
        score+=1
    else:
        print("Wrong Answer\n")
    loop=input("Do you want to keep playing?")
    if loop !="y":
        break
    answer=input("""G-7 approved USD 15.5 billion deal with which country to help tackle climate-damaging pollution?
    [A] India
    [B] Sri Lanka
    [C] Vietnam
    [D] Thailand\n""")
    if answer == "c":
        print("Correct Answer\n")
        score+=1
    else:
        print("Wrong Answer\n")
    loop=input("Do you want to keep playing?")
    if loop !="y":
        break
    answer=input("""Which institution issues Sovereign Gold Bonds for public subscription?
    [A] Reserve Bank of India
    [B] State Bank of India
    [C] NITI Aayog
    [D] SEBI\n""")
    if answer == "a":
        print("Correct Answer\n")
        score+=1
    else:
        print("Wrong Answer\n")
    loop=input("Do you want to keep playing?")
    if loop !="y":
        break

print("Your Score is",score)