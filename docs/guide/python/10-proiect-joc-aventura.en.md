---
lesson: 10
tags: [python, project, game, text-adventure, functions, dictionaries, files]
summary: Final project — build a complete text adventure game step by step.
---

# Lesson 10 · Project: Text adventure game

!!! tip "What you'll practice"
    - Variables, conditions, loops
    - Functions and code organization
    - Dictionaries for structured data
    - Files for saving progress

---

## Project overview

You will build a simple **text adventure game** in which the player explores rooms, picks up items, and must reach the exit.

**Example run:**
```
=== ADVENTURE IN THE MYSTERIOUS CASTLE ===

You are in: Entrance
Description: A large hall with a stone floor. You feel a cold draft.
Items: ['torch']
Exits: ['north']

What do you do? (go [direction] / take [item] / inventory / quit): take torch
You took: torch

What do you do?: go north

You are in: Corridor
Description: A narrow corridor. At the end you see a massive door.
Items: ['key']
Exits: ['south', 'north']
```

---

## Step 1: The world structure

First we define the rooms as a dictionary:

```python
world = {
    "entrance": {
        "name": "Entrance",
        "description": "A large hall with a stone floor. You feel a cold draft.",
        "items": ["torch"],
        "exits": {"north": "corridor"}
    },
    "corridor": {
        "name": "Corridor",
        "description": "A narrow corridor. At the end you see a massive door.",
        "items": ["key"],
        "exits": {"south": "entrance", "north": "treasure_room"}
    },
    "treasure_room": {
        "name": "Treasure Room",
        "description": "A room full of gold! But the exit door is locked...",
        "items": ["treasure"],
        "exits": {"south": "corridor", "east": "exit"}
    },
    "exit": {
        "name": "Exit",
        "description": "You left the castle! Congratulations, adventurer!",
        "items": [],
        "exits": {}
    }
}
```

## Step 2: The player's state

```python
player = {
    "current_room": "entrance",
    "inventory": [],
    "steps": 0
}
```

## Step 3: The basic functions

```python
def show_room(world, player):
    room = world[player["current_room"]]
    print(f"\nYou are in: {room['name']}")
    print(f"Description: {room['description']}")
    if room["items"]:
        print(f"Items: {room['items']}")
    print(f"Exits: {list(room['exits'].keys())}")

def move(world, player, direction):
    room = world[player["current_room"]]
    if direction in room["exits"]:
        player["current_room"] = room["exits"][direction]
        player["steps"] += 1
        print(f"You move {direction}...")
    else:
        print("You can't go that way.")

def take_item(world, player, item):
    room = world[player["current_room"]]
    if item in room["items"]:
        room["items"].remove(item)
        player["inventory"].append(item)
        print(f"You took: {item}")
    else:
        print(f"There is no '{item}' in this room.")

def show_inventory(player):
    if player["inventory"]:
        print(f"Inventory: {player['inventory']}")
    else:
        print("Your inventory is empty.")
```

## Step 4: The main game loop

```python
def game():
    print("=== ADVENTURE IN THE MYSTERIOUS CASTLE ===\n")
    print("Commands: go [direction] | take [item] | inventory | quit\n")

    while True:
        show_room(world, player)

        # Check if the player reached the exit
        if player["current_room"] == "exit":
            print(f"\nYou finished the game in {player['steps']} steps!")
            print(f"Final inventory: {player['inventory']}")
            break

        command = input("\nWhat do you do? ").strip().lower()

        if command.startswith("go "):
            direction = command[3:]
            move(world, player, direction)

        elif command.startswith("take "):
            item = command[5:]
            take_item(world, player, item)

        elif command == "inventory":
            show_inventory(player)

        elif command == "quit":
            print("You abandoned the adventure.")
            break

        else:
            print("Unknown command. Try: go [direction], take [item], inventory, quit")

game()
```

## The complete code

Here is the complete game, combining all the steps:

```python
# === Text adventure game ===

world = {
    "entrance": {
        "name": "Entrance",
        "description": "A large hall with a stone floor. You feel a cold draft.",
        "items": ["torch"],
        "exits": {"north": "corridor"}
    },
    "corridor": {
        "name": "Corridor",
        "description": "A narrow corridor. At the end you see a massive door.",
        "items": ["key"],
        "exits": {"south": "entrance", "north": "treasure_room"}
    },
    "treasure_room": {
        "name": "Treasure Room",
        "description": "A room full of gold! But the exit door is locked...",
        "items": ["treasure"],
        "exits": {"south": "corridor", "east": "exit"}
    },
    "exit": {
        "name": "Exit",
        "description": "You left the castle! Congratulations, adventurer!",
        "items": [],
        "exits": {}
    }
}

player = {
    "current_room": "entrance",
    "inventory": [],
    "steps": 0
}

def show_room(world, player):
    room = world[player["current_room"]]
    print(f"\nYou are in: {room['name']}")
    print(f"Description: {room['description']}")
    if room["items"]:
        print(f"Items: {room['items']}")
    print(f"Exits: {list(room['exits'].keys())}")

def move(world, player, direction):
    room = world[player["current_room"]]
    if direction in room["exits"]:
        player["current_room"] = room["exits"][direction]
        player["steps"] += 1
    else:
        print("You can't go that way.")

def take_item(world, player, item):
    room = world[player["current_room"]]
    if item in room["items"]:
        room["items"].remove(item)
        player["inventory"].append(item)
        print(f"You took: {item}")
    else:
        print(f"There is no '{item}' in this room.")

def game():
    print("=== ADVENTURE IN THE MYSTERIOUS CASTLE ===\n")
    print("Commands: go [direction] | take [item] | inventory | quit\n")

    while True:
        show_room(world, player)

        if player["current_room"] == "exit":
            print(f"\nCongratulations! You finished in {player['steps']} steps.")
            print(f"Final inventory: {player['inventory']}")
            break

        command = input("\nWhat do you do? ").strip().lower()

        if command.startswith("go "):
            move(world, player, command[3:])
        elif command.startswith("take "):
            take_item(world, player, command[5:])
        elif command == "inventory":
            if player["inventory"]:
                print(f"Inventory: {player['inventory']}")
            else:
                print("Your inventory is empty.")
        elif command == "quit":
            print("You abandoned the adventure.")
            break
        else:
            print("Unknown command.")

game()
```

---

## Ideas for extending the project

- Add more rooms and items
- Implement a door that only opens if you have the key
- Save progress to JSON (from Lesson 09)
- Add a points or health system
- Create a monster that blocks a corridor

---

**Next step:** [→ Project: Turtle Graphics](11-proiect-turtle.md)
