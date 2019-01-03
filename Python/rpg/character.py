class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """Prints name and description of the character"""
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """Set what this character will say when talked to"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """Talk to this character"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """Returns true or false - Fight with this character"""
        print(self.name + " doesn't want to fight with you")
        return False
        
class Enemy(Character):
  
    #Create enemy from within Character class using super().
    enemies_defeated = 0
  
    def __init__(self, char_name, char_description):
      """Creates enemy from within Character class using super()."""
      super().__init__(char_name, char_description)
      self.weakness = None 

    # Fight with an enemy
    def fight(self, combat_item):
      """Returns true or false - Fight with this character"""
      if combat_item == self.weakness:
        print("You fend " + self.name + " off with the " + combat_item)
        Enemy.enemies_defeated += 1
        return True
      else:
        print(self.name + " crushes you, puny adventurer!")
        return False
      
    def set_weakness(self, item_weakness):
      """Getters and setters for weakness""" 
      self.weakness = item_weakness
    
    def get_weakness(self):
      """Getters and setters for weakness"""  
      return self.weakness
  
    # Getters and setters for the enemies_defeated variable
    def get_defeated(self):
      """"Getters and setters for the enemies_defeated variable"""
      return Enemy.enemies_defeated
  
    def set_defeated(self, number_defeated):
      """Getters and setters for the enemies_defeated variable"""
      Enemy.enemies_defeated = number_defeated
  
    def steal(self):
      print("You steal from " + self.name)
      # How will you decide what this character has to steal?
  

class Friend(Character):
  
    #Create friend from within Character class using super()
    def __init__(self, char_name, char_description):

      super().__init__(char_name, char_description)
      self.feeling = None
     
    def hug(self):
       """Returns a string containing hug action"""
       print(self.name + " hugs you back!")  
