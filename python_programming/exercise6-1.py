# exercise6-1.py

def oldMacDonald():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, oh!")

#   def animal(animal):
    

def animalSound(animal, sound):
    print("And on that farm he had a", animal, ", Ee-igh, Ee-igh, oh!")
    print("with a", sound + ",", sound, "here and a", sound + ",", sound, "there")
    print("Here a", sound + ", there a", sound + ", everywhere a", sound
          + ",", sound)

def sing(animal, sound):
    oldMacDonald()
    animalSound(animal, sound)
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

main()
