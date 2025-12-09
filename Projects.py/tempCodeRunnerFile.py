 if "baseball-bat" in backpack.keys:
                print("You've already been here, there is nothing here.")
                continue
            else:
                print("You explore the bedroom.\nYou find a baseball bat.\nBaseball bat added to backpack")
                backpack["baseball-bat"] = 30
                continue