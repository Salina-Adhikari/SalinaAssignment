import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pet:
    def __init__(self, name):
        self.pet_name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def is_sick(self):
        return self.hunger == 0 or self.happiness == 0 or self.energy == 0

    def feed_pet(self):
        self.hunger = min(self.hunger + 20, 100)
        print(f"\n{self.pet_name}'s hunger increased to {self.hunger}.")

    def play_pet(self):
        self.happiness = min(self.happiness + 20, 100)
        self.energy = max(self.energy - 20, 0)
        print(f"\n{self.pet_name}'s happiness increased to {self.happiness} and energy decreased to {self.energy}.")

    def rest_pet(self):
        self.energy = min(self.energy + 20, 100)
        self.hunger = max(self.hunger - 5, 0)
        print(f"\n{self.pet_name}'s energy increased to {self.energy} and hunger decreased to {self.hunger}.")

    def pet_status(self):
        print(f"\n{self.pet_name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

    def random_event(self):
        events = [
            ("found a toy! Happiness increased.", "happiness", 10),
            ("found some food! Hunger increased.", "hunger", 10),
            ("got tired while playing. Energy decreased.", "energy", -10),
        ]
        event = random.choice(events)
        if event[1] == "happiness":
            self.happiness = min(self.happiness + event[2], 100)
        elif event[1] == "hunger":
            self.hunger = min(self.hunger + event[2], 100)
        elif event[1] == "energy":
            self.energy = max(self.energy + event[2], 0)
        print(f"\n{self.pet_name} {event[0]}")

    def check_win(self, win_count):
        if self.hunger > 80 and self.happiness > 80 and self.energy > 80:
            win_count += 1
        else:
            win_count = 0
        return win_count

def input_with_timer(prompt, timeout):
    clear_screen()
    # Show pet menu
    print("== Update the Pet ==")
    print("1. Feed the Pet")
    print("2. Play with Pet")
    print("3. Rest Time")
    print("4. Exit to Main Menu")
    
    print(f"\nYou have {timeout} seconds to respond!")
    
    # Start timing
    start_time = time.time()
    
    # Get input
    user_input = input(prompt)
    
    # Check if time is up
    if time.time() - start_time > timeout:
        print("\nTime's up! Too slow!")
        time.sleep(1)  # Show the message for a second
        return None
    
    return user_input

def save_game(pet):
    with open("savegame.txt", "w") as file:
        file.write(f"{pet.pet_name},{pet.hunger},{pet.happiness},{pet.energy}")
    print("\nGame saved!")

def load_game():
    try:
        with open("savegame.txt", "r") as file:
            data = file.read().split(",")
            pet = Pet(data[0])
            pet.hunger = int(data[1])
            pet.happiness = int(data[2])
            pet.energy = int(data[3])
            print("\nGame loaded successfully!")
            return pet
    except FileNotFoundError:
        print("\nNo saved game found.")
        return None

def pet_game(pet):
    win_count = 0
    while True:
        if pet.is_sick():
            print("\nOh no! Your pet got sick. Thank you for playing!")
            break

        if win_count >= 3:
            print(f"\nCongratulations! {pet.pet_name} is super happy and energetic. You win!")
            break

        # Show current pet status before choice
        pet.pet_status()
        choice = input_with_timer("Enter your choice (1/2/3/4): ", 12)  # Changed to 12 seconds

        if choice is None:
            print(f"\n{pet.pet_name} got distracted while waiting!")
            pet.random_event()
        elif choice == "1":
            pet.feed_pet()
        elif choice == "2":
            pet.play_pet()
        elif choice == "3":
            pet.rest_pet()
        elif choice == "4":
            print(f"\nReturning to the main menu, {pet.pet_name}!")
            break
        else:
            print("Invalid choice. Please try again.")

        win_count = pet.check_win(win_count)
        time.sleep(1)  # Give time to read the update

def main():
    pet = None
    while True:
        clear_screen()
        print("\n== Adventure Game ==")
        print("1. Pet Game")
        print("2. View Your Pet's Status")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            if not pet:
                pet_name = input("\nEnter your pet's name: ").strip()
                pet = Pet(pet_name)
            pet_game(pet)
        elif choice == "2":
            if pet:
                pet.pet_status()
                input("\nPress Enter to continue...")
            else:
                print("\nYou need to start the pet game first!")
                time.sleep(1)
        elif choice == "3":
            if pet:
                save_game(pet)
            else:
                print("\nStart a game first to save progress!")
            time.sleep(1)
        elif choice == "4":
            loaded_pet = load_game()
            if loaded_pet:
                pet = loaded_pet
            time.sleep(1)
        elif choice == "5":
            print("You exited the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()