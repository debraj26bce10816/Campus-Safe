# CAMPUS SAFE

## Project Overview

Campus Safe is a simple Python-based campus safety and support system. It allows students and campus users to report emergencies, lost and found items, and campus-related complaints.

The system provides a menu-driven interface where users can submit reports, search for lost items, and view all submitted reports.

## Features

- Report a campus emergency
- Report a lost item
- Report a found item
- Submit a campus complaint
- Automatically assign complaint priority
- Search for lost items
- View emergency reports
- View lost item reports
- View found item reports
- View campus complaints
- View all reports and their totals
- Simple command-line menu
- Exit option

## Technologies / Tools Used

- **Python 3**
- Python lists for storing reports
- Python functions for organizing program features
- Conditional statements for menu selection and complaint priority
- Loops for displaying and searching reports
- GitHub for source-code management

## Project Structure

```text
CampusSafe/
│
├── main.py
├── README.md
└── statement.mdHow to Use


## Instructions to run the program
After starting the program, the following menu is displayed:

==============================
          CAMPUS SAFE
  Campus Safety & Support
==============================
1.Report Emergency
2.Report Lost Item
3.Report Found Item
4.Submit Complaint
5.Search Lost Item
6.View All Reports
7.Exit
==============================

# Enter a number from 1 to 7 to select an operation.

Report Emergency

Enter:

Name
Emergency type
Location
Description

The emergency report is stored in the system.

# Report Lost Item

Enter:

Name
Lost item
Last known location
Description

The item is added to the lost-items list.

# Report Found Item

Enter:

Name
Found item
Location where it was found
Description

The item is added to the found-items list.

# Submit Complaint

Enter:

Name
Complaint category
Location
Complaint description


# Search Lost Item

Enter the name or part of the name of a lost item.

The program searches the stored lost-item reports and displays matching results.

# View All Reports

This option displays:

Total emergency reports
Total lost items
Total found items
Total complaints
Details of each report
Exit

Select option 7 to exit the program
