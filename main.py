# CAMPUS SAFE

emergency_reported = []
items_lost = []
items_found = []
complaint = []


# A function to report an emergency
def reporting_emergency():
    print("\n--- REPORTING EMERGENCY ---")

    n = input("Enter your name: ")
    em = input("Enter emergency type: ")
    l = input("Enter location: ")
    d = input("Enter description: ")

    # Storing all the details in a single list
    r = [n, em, l, d]
    emergency_reported.append(r)

    print("\n Emergency is reported successfully!")


# A function for reporting a lost item
def items_lost_report():
    print("\n --- REPORT OF LOST ITEM --- ")

    n = input("Enter your name: ")
    i = input("Enter the item lost: ")
    l = input("Where did you last saw it? ")
    d = input("Enter the description of the item lost: ")

    r = [n, i, l, d]
    items_lost.append(r)

    print("\n Lost item is reported successfully!")


# A function to report an item that is found
def items_found_report():
    print("\n--- REPORT ITEM TO BE FOUND ---")

    n = input("Enter your name: ")
    i = input("Enter the item found: ")
    l = input("Where did you found it? ")
    d = input("Enter the description of the item: ")

    r = [n, i, l, d]
    items_found.append(r)

    print("\n Found item is reported successfully!")


# A Function for submitting a complaint regarding campus
def submission_complaint():
    print("\n--- SUBMISSION OF COMPLAINT ---")

    n = input("Enter your name: ")
    c = input("Enter what type of category is your complaint: ")
    l = input("Enter the location: ")
    c = input("Enter your complaint regarding the campus: ")

    #Giving a simple priority based on category
    if c.lower() == "security":
        prior = "HIGH"
    elif c.lower() == "electricity":
        prior = "HIGH"
    elif c.lower() == "water":
        prior = "MEDIUM"
    else:
        prior = "NORMAL"

    r = [n, c, l, c, prior]
    complaint.append(r)

    print("\n Complaint is submitted successfully!")
    print("Priority:", prior)


# A Function for displaying emergency reports
def viewing_emergencies():
    print("\n --- REPORTING EMERGENCY ---")

    if len(emergency_reported) == 0:
        print("No emergency reports are available.")
    else:
        for i in range(len(emergency_reports)):
            print("\nReport", i + 1)
            print("Name:", emergency_reported[i][0])
            print("Emergency:", emergency_reported[i][1])
            print("Location:", emergency_reported[i][2])
            print("Description:", emergency_reported[i][3])


# A Function for displaying items lost
def viewing_items_lost():
    print("\n --- ITEMS LOST ---")

    if len(items_lost) == 0:
        print("No lost items are reported.")
    else:
        for i in range(len(items_lost)):
            print("\n Items Lost", i + 1)
            print("Name:", items_lost[i][0])
            print("Item:", items_lost[i][1])
            print("Last seen:", items_lost[i][2])
            print("Description:", items_lost[i][3])


# A Function for displaying the items found
def viewing_items_found():
    print("\n --- ITEMS FOUND ---")

    if len(items_found) == 0:
        print("No found items are reported.")
    else:
        for i in range(len(items_found)):
            print("\n Item found", i + 1)
            print("Name:", items_found[i][0])
            print("Item:", items_found[i][1])
            print("Found at:", items_found[i][2])
            print("Description:", items_found[i][3])


# A Function for displaying complaints regarding campus
def viewing_complaint():
    print("\n --- COMPLAINTS REGARDING CAMPUS ---")

    if len(complaint) == 0:
        print("No complaints are available.")
    else:
        for i in range(len(complaint)):
            print("\nComplaint", i + 1)
            print("Name:", complaint[i][0])
            print("Category:", complaint[i][1])
            print("Location:", complaint[i][2])
            print("Complaint:", complaint[i][3])
            print("Priority:", complaint[i][4])


# A Function for searching a item lost
def searching_item_lost():
    print("\n --- SEARCHING ITEM LOST ---")

    if len(items_lost) == 0:
        print("No report of any lost items.")
        return

    name_item = input("Enter the name of the item for searching: ")
    f = False

    # Checking every lost items one by one
    for i in range(len(items_lost)):
        if name_item.lower() in items_lost[i][1].lower():
            print("\nItem found!")
            print("Name:", items_lost[i][0])
            print("Item:", items_lost[i][1])
            print("Last seen:", items_lost[i][2])
            print("Description:", items_lost[i][3])
            f = True

    if f == False:
        print("No matching item is found.")


# A Function for displaying all the reports
def viewing_all_reports():
    print("\n ============================== ")
    print("       ALL CAMPUS REPORTS  ")
    print(" ============================== ")

    print("\n Total emergency reports:", len(emergency_reported))
    print("Total lost items:", len(items_lost))
    print("Total found items:", len(items_found))
    print("Total complaints:", len(complaint))

    viewing_emergencies()
    viewing_items_lost()
    viewing_items_found()
    viewing_complaint()


# Main function of the program
def main_():

    # For Keep showing the menu list until the user chooses Exit
    while True:
        print("\n ============================== ")
        print("          CAMPUS SAFE  ")
        print("  Campus Safety & Support  ")
        print(" ============================== ")
        print("1.Report Emergency")
        print("2.Report Lost Item")
        print("3.Report Found Item")
        print("4.Submit Complaint")
        print("5.Search Lost Item")
        print("6.View All Reports")
        print("7.Exit")
        print(" =============================  ")

        ch = input("Enter your choice: ")

        # Call the required function according to the choice
        if ch == "1":
            reporting_emergency()
        elif ch == "2":
            items_lost_report()
        elif ch == "3":
            items_found_report()
        elif ch == "4":
            submission_complaint()
        elif ch == "5":
            searching_item_lost()
        elif ch == "6":
            viewing_all_reports()
        elif ch == "7":
            print("\n Thank you for using CampusSafe!")
            print(" Have a safe day!")
            break
        else:
            print("\n Invalid choice. Please enter a number from 1 to 7.")


main_()
