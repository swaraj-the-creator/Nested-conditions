name = str(input("Enter your name:"))
print("Pick your location")
print("1: Beach")
print("2: snowy mountains")
act1 = int(input("1 or 2:"))
if act1 == 1:
    Act ="Beach"
    print("Pick your beach activity")
    print("1: Water sports")
    print("2: Swimming")
    act2 = int(input("1 or 2:"))
    if act2 == 1:
        TT = "You picked: Water sports"
        TF = "Best time: Morning"
        FF = "Remember: Carry a towel and life jackets"
    elif act2 == 2:
     TT= "You picked: Swimming"
     TF =  "Best time: Evening"
     FF =  "Remember: Carry a towel"
    else:
        print("COMMAND NOT FOUND")
elif act1 == 2:
    Act = "Snowy mountains"
    print("Pick your Snowy mountain activity")
    print("1: Snowman building")
    print("2: Hiking")
    act2 = int(input("1 or 2:"))
    if act2 == 1:
        TT = "You picked: Snowman building"
        TF = "Best near: Snow"
        FF = "Remember: Wear a jacket and gloves and carry a carrot"
    elif act2 == 2:
        TT = "You picked: Hiking"
        TF = "Best for: Exploring trails"
        FF = "Remember: Wear comfortable and high grip shoes"
    else:
        print("COMMAND NOT FOUND")
else:
    print("COMMAND NOT FOUND")   
print("\n========= HOLIDAY PLANNER ============")     
print(name," picked: ",Act)
print(TT)
print(TF)
print(FF)
print("========================================")