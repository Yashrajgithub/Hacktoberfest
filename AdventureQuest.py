import random

class Game:
    def __init__(self):
        self.rooms = {
            'Hall': Room('Hall', 'You are in a grand hall with portraits on the walls. There are doors to the north and east.'),
            'Kitchen': Room('Kitchen', 'You are in a kitchen. There is a delicious smell coming from the oven.'),
            'Library': Room('Library', 'You are in a library filled with ancient books. There is a door to the south.'),
            'Garden': Room('Garden', 'You are in a beautiful garden with flowers and a fountain. There is a door to the west.'),
            'Cellar': Room('Cellar', 'You are in a dark cellar. You can hear the sound of dripping water.'),
            'Attic': Room('Attic', 'You are in a dusty attic filled with old furniture and forgotten memories.'),
            'Bathroom': Room('Bathroom', 'You are in a bathroom. The air smells of soap and fresh towels.'),
            'Bedroom': Room('Bedroom', 'You are in a cozy bedroom with a large bed and a window overlooking the garden.')
        }
        self.rooms['Hall'].set_exits(north=self.rooms['Kitchen'], east=self.rooms['Library'])
        self.rooms['Kitchen'].set_exits(south=self.rooms['Hall'], west=self.rooms['Cellar'])
        self.rooms['Library'].set_exits(west=self.rooms['Hall'], north=self.rooms['Attic'])
        self.rooms['Garden'].set_exits(south=self.rooms['Library'])
        self.rooms['Cellar'].set_exits(east=self.rooms['Kitchen'])
        self.rooms['Attic'].set_exits(south=self.rooms['Library'])
        self.rooms['Bathroom'].set_exits(north=self.rooms['Bedroom'])
        self.rooms['Bedroom'].set_exits(south=self.rooms['Bathroom'])

        self.current_room = self.rooms['Hall']
        self.inventory = []
        self.start_game()

    def start_game(self):
        print("Welcome to Adventure Quest!")
        print("Type 'quit' or 'exit' to end the game at any time.")
        self.game_loop()

    def game_loop(self):
        while True:
            self.describe_room()
            command = input("What do you want to do? ").lower()
            if command in ['quit', 'exit']:
                print("Thank you for playing!")
                break
            self.process_command(command)

    def describe_room(self):
        print(f"\nYou are in the {self.current_room.name}.")
        print(self.current_room.description)
        self.show_inventory()
        self.show_items()

    def show_items(self):
        if self.current_room.items:
            print("You see: " + ", ".join(self.current_room.items))
        else:
            print("There are no items here.")

    def process_command(self, command):
        if command in self.current_room.exits:
            self.current_room = self.current_room.exits[command]
        elif command.startswith('take '):
            item = command.split(' ', 1)[1]
            self.take_item(item)
        elif command.startswith('drop '):
            item = command.split(' ', 1)[1]
            self.drop_item(item)
        elif command.startswith('look '):
            item = command.split(' ', 1)[1]
            self.look_at(item)
        elif command.startswith('use '):
            item = command.split(' ', 1)[1]
            self.use_item(item)
        else:
            print("Invalid command. Try again.")

    def take_item(self, item):
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)
            print(f"You have taken the {item}.")
        else:
            print(f"There is no {item} here.")

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.items.append(item)
            print(f"You have dropped the {item}.")
        else:
            print(f"You do not have a {item}.")

    def look_at(self, item):
        descriptions = {
            'book': 'It is an ancient book filled with spells and secrets.',
            'key': 'A rusty old key that looks like it might open something.',
            'sword': 'A shiny sword, its blade gleaming in the light.',
            'potion': 'A mysterious potion that shimmers with colors.',
            'apple': 'A shiny red apple, fresh and juicy.'
        }
        if item in descriptions:
            print(descriptions[item])
        else:
            print("You can’t look at that.")

    def use_item(self, item):
        if item in self.inventory:
            if item == 'key' and self.current_room.name == 'Cellar':
                print("You unlock a secret passage with the key!")
                self.current_room = self.rooms['Garden']
            elif item == 'potion':
                print("You drink the potion and feel rejuvenated!")
                self.inventory.remove(item)
            else:
                print(f"You can't use the {item} here.")
        else:
            print(f"You do not have a {item}.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying: " + ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def set_exits(self, north=None, south=None, east=None, west=None):
        if north: self.exits['north'] = north
        if south: self.exits['south'] = south
        if east: self.exits['east'] = east
        if west: self.exits['west'] = west

    def add_item(self, item):
        self.items.append(item)

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
