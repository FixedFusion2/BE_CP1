        print("You can't use that item.")

#FUNCTION Combat
def combat(player,enemy):
    print(f"A{enemy['name']} attacks you.")
    print(f"{enemy["description"]}")
    enemy_hp = enemy["health"]
    #Combat loop
    while player["health"] > 0 and enemy_hp > 0:
        print(f"\nYour HP: {player["health"]} | {enemy['name']} HP: {enemy_hp}")
        print("Actions:\n1. Punch\n2. Run\n3. Use item")
        attack = input("Choose what do to. Type 1-3: ")
        #Punch
        if attack == "1":
            damage = 5 + player["backpack"]["strength_drugs"] * 3
            print(f"You punch the {enemy['name']} and do {damage}!")
            enemy_hp -= damage
        #Run
        elif attack == "2":
            base_escape = 30
            escape_chance = base_escape + (player["backpack"]["speed_drugs"] * 15)
            if random.randint(1,100) <= escape_chance:
                print("You escaped.")
                return "escaped"
            else:
                print(f"You try to run but the {enemy['name']} stops you.")
        #Use Item
        elif attack == "3":
            use_item(player)
        else:
            print("Invalid Choice.")
    #Enemy turn befroe chicking if player died.
            if enemy_hp > 0:
                dmg = enemy["attack"]
                print(f"The {enemy['name']} does {dmg}.")
                player["health"] -= dmg
        #Outcome
    if player["health"] <= 0:
        print("You died.")
        return "dead"
    else:
        print(f"You defeated the {enemy['name']}.")
        return "victory"