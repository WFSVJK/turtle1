#!/usr/bin/env python
# coding: utf-8

class Parent():
    def __init__(self, name):
        self.name = name
        self.spouse = None
        self.children = []
        self.pet = None
    
    def set_spouse(self,other):
        self.spouse = other
        other.spouse = self
        
    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)
        if len(self.children)>1:
            for i in range(len(self.children)-1):
                if not child in self.children[i].siblings:
                    self.children[i].add_sibling(child)
                    
    def add_pet(self, pet):
        self.pet = pet
        
    def __repr__(self):
        return f"Parent({self.name})"

    def __str__(self):
        desc = f"{self.name}"
        if self.spouse:
            desc += f" married to {self.spouse.name}"
        if len(self.children):
            desc += " has children " + ", ".join([child.name for child in self.children])
        if self.pet:
            desc += f" and has a pet {self.pet.animal_type}, {self.pet.name}"
        return desc



class Family():
    def __init__(self, parent_1, parent_2):
        parent_1.set_spouse(parent_2)
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.children = []
        self.pets = []

        
    def add_child(self, child):
        for parent in [self.parent_1, self.parent_2]:
            parent.add_child(child)
        self.children = self.parent_1.children
    
    def add_pet(self, pet):
        self.pets.append(pet)
            
    def add_children(self, children):
        for child in children:
            self.add_child(child)
        self.children = self.parent_1.children
        

class Pet():
    def __init__(self, name, animal_type, person_close_to):
        self.name = name
        self.animal_type = animal_type
        self.person_close_to = person_close_to
        person_close_to.add_pet(self)


    def talk(self):
        if (self.animal_type == "Dog") or (self.animal_type == "dog"):
            return("Woof Woof!!")
        elif (self.animal_type == "Cat") or (self.animal_type == "cat") :
            return("Meow Meow!!")
        else:
            return("I don't know how I talk, how about Wuff Meow Grrr Woot")
            
    def __repr__(self):
        return f"{self.animal_type}({self.name})"
    
    def __str__(self):
        return f"{self.name} is a {self.animal_type} close to {self.person_close_to.name} and goes '{self.talk()}''"


class Child():
    def __init__(self, name):
        self.name = name
        self.siblings = []
        self.parents = []
        self.friends = []
        self.pet = None
        
    def add_sibling(self, other):
        self.siblings.append(other)
        other.siblings.append(self)
        
    def add_pet(self, pet):
        self.pet = pet
        
    def add_friend(self, other):
        self.friends.append(other)
        other.friends.append(self)
        
    def __str__(self):
        desc = self.name
        if len(self.parents):
            desc += " is a child of " + " and ".join([parent.name for parent in self.parents])
        if len(self.siblings):
            desc += " has sibling(s) " + ", ".join([sibling.name for sibling in self.siblings])
        if self.pet:
            desc += f" and has a pet {self.pet.animal_type}, {self.pet.name}"
        if len(self.friends):
            desc += ". Has friend(s) " + ", ".join([friend.name for friend in self.friends]) + "."
        return desc
    
    def __repr__(self):
        return f"Child({self.name})"


parent_1 = Parent(input("Enter a parent's name: "))
parent_2 = Parent(input("Enter another parent's name: "))
fam = Family(parent_1, parent_2)

characters = [parent_1, parent_2]

# ---- Adding Children ---
print("\n\nAdding children")
choice = input("ADD?? Enter Y to add child or N to go to the next step: ")
while(choice == "Y"):
    child = Child(input("Enter a child's name: "))
    fam.add_child(child)
    characters.append(child)
    choice = input("ADD?? Enter Y to keep adding children or N to go to the next step: ")


# --- Addming Friends -----
print("\n\nAdding friends")
if fam.children:
    choice = input("ADD?? Enter Y to add a friend or N to go to the next step: ")
    while(choice == "Y"):
        print("\nEnter the child you want a friend for:")
        for i in range(len(fam.children)):
            print(f"Enter {i} for {fam.children[i].name}")
        choice = input("Enter number: ")
        child_to_add_friend_to = fam.children[int(choice)]
        
        child = Child(input("Now enter a friend's name: "))
        child_to_add_friend_to.add_friend(child)
        characters.append(child)
        choice = input("ADD?? Enter Y to keep adding friends and N to go to the next step: ")
        


# -----  Adding Pets ------
print("\n\nAdding Pets")
choice = input("ADD?? Enter Y to add pet or N to go to the RELATIONSHIP SUMMARY: ")
while(choice == "Y"):
    pet = input("Enter a pet's name: ")
    animal_type = input("Enter a pet's type (Dog or Cat): ")
    fam.add_pet(Pet(pet, animal_type, fam.parent_1))
    choice = input("ADD?? Enter Y to keep adding pets or N to go to the next step: ")
    characters.append(pet)



for character in characters:
    print(character)

# --- use Digraph for directional arrows for graphs --
from graphviz import Digraph

g = Digraph('G', filename='process.gv', engine='sfdp')


g.edge(parent_1.name, 'Parents')
g.edge(parent_2.name, 'Parents')
if len(fam.children):
    g.edge('Parents', 'Kids')
    for child in fam.children:
        g.edge('Kids',child.name)
        if len(child.friends):
            g.edge(child.name, f"{child.name}'s friends")
            for friend in child.friends:
                g.edge(f"{child.name}'s friends", friend.name)
    
    
if len(fam.pets):
    g.edge('Parents', 'Pets')
    for pet in fam.pets:
        g.edge('Pets',pet.name)


# ---- Generate the family out tree in PDF form and display on the conole ---
g.render('family_tree.png', view=True)


# ----------------------------
# -------   END PROGRAM  -----
# ----------------------------


