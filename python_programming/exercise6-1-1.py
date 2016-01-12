# exercise6-1-1.py

def oldMacDonald():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, oh!")

def creature(animal):
    print("And on that farm he had a", animal, ", Ee-igh, Ee-igh, oh!")    

def animalSound(sound):    
    print("With a", sound + ",", sound, "here and a", sound + ",", sound, "there")
    print("Here a", sound + ", there a", sound + ", everywhere a", sound
          + ",", sound)

def sing(animal, sound):
    oldMacDonald()
    creature(animal)
    animalSound(sound)
    oldMacDonald()
    
def main():
    sing("cow", "moo")
    print()    
    sing("pig", "oink")
    print()
    sing("duck", "quack")
    print()
    sing("horse", "neigh")
    print()
    sing("lamb", "baa")
    print()
    sing("chicken", "cluck")
    print()
    animalSound("baa")
    animalSound("neigh")
    animalSound("quack")
    animalSound("oink")
    animalSound("moo")    
    print()
    oldMacDonald()

main()
