lost_objects = []
found_objects = []


def add_lost():
    name = input("Object Name: ")
    color = input("Color: ")
    place = input("Lost Place: ")

    lost_objects.append({
        "name": name.lower(),
        "color": color.lower(),
        "place": place.lower()
    })

    print("Lost object added successfully!")


def add_found():
    name = input("Object Name: ")
    color = input("Color: ")
    place = input("Found Place: ")

    found_objects.append({
        "name": name.lower(),
        "color": color.lower(),
        "place": place.lower()
    })

    print("Found object added successfully!")


def match_objects():
    if not lost_objects or not found_objects:
        print("Add lost and found objects first!")
        return

    for lost in lost_objects:
        match_found = False

        for found in found_objects:
            score = 0

            if lost["name"] == found["name"]:
                score += 50

            if lost["color"] == found["color"]:
                score += 30

            if lost["place"] == found["place"]:
                score += 20

            if score >= 80:
                print("\n=== MATCH FOUND ===")
                print("Object:", found["name"])
                print("Color:", found["color"])
                print("Found Place:", found["place"])
                print("Match Score:", score, "%")
                match_found = True

        if not match_found:
            print("\nNo strong match for", lost["name"])


while True:
    print("\n===== LOST AND FOUND SYSTEM =====")
    print("1. Add Lost Object")
    print("2. Add Found Object")
    print("3. Match Objects")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_lost()

    elif choice == "2":
        add_found()

    elif choice == "3":
        match_objects()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")




