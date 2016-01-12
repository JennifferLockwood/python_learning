# exercise6-2.py

def firstTwoSentences(number):
    print("The ants go marching", number, "by", number + ", hurra! hurra!")
    print("The ants go marching", number, "by", number + ", hurra! hurra!")
    print("The ants go marching", number, "by", number + ",")

def action(verb):
    print("The little one stops to", verb)
    
def endSentences():
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")
    
def main():
    numbers = ["one", "two", "three", "four", "five", "six",
               "seven", "eight", "nine", "ten"]
    actions = ["suck his thumb,", "tie his shoe,", "climb a tree,",
               "shut the door,", "take a dive,", "pick up sticks,", "pray to heaven,",
               "roller skate,", "check the time,", "shut 'The End',"]
    for i in range(len(numbers)):
        firstTwoSentences(numbers[i])
        action(actions[i])
        endSentences()

main()
