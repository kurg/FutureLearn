###Player Class NEW PLAYER CLASS######################################

class Player():
    def __init__(self,player_name):
        self.name = player_name
        self.health = None
        self.inventory = []

    def set_inventory(self,inventory_list):
        self.inventory = inventory_list

    def get_inventory(self):
        return self.inventory

    def set_health(self,health_points):
        self.health = health_points

    def get_health(self):
        return self.health

    def describe(self):
        print ("You name is, ", self.name)
        print ("You are carrying:")
        for item in self.inventory:
            print (item[0], item[1])
        print ()
        print ("Your health is :", self.health)


#####THE BIT OF MAIN THAT USES THE NEW PLAYER CLASS#####################
    ###STATUS
    elif command =="Status":
        protag.describe()
    ###GET
    elif command =="Get":
        if room_item is not None:
            get_what = input("What will you get? >>> ")
            if get_what in room_item.item:
                inventory = protag.inventory
                got = [room_item.item,room_item.item_description]
                inventory.append(got)
                print ("You got the ", room_item.item)
                room_item.item = None
                room_item.item_description = None
                
            else:
                print ("You can't get that!")
