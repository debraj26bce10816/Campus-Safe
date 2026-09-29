CAMPUS SAFE

Project Overview

Campus Safe is a straightforward safety and support system based on Python. It enables students and other members of the campus community to report emergencies, lost and found items, and complaints relating to the campus.

The system has a menu-driven interface which allows users to file reports, look for lost items, and see all the reports that have been submitted.

Features

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

Technologies / Tools Used

- Python 3
- Python lists for storing reports
- Python functions for organizing program features
- Conditional statements for menu selection and complaint priority
- Loops for displaying and searching reports
- GitHub for source-code management

Project Structure

CampusSafe/
│
├── main.py
├── README.md
└── statement.md

How to Use

Instructions to Run the Program

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

Type a number between 1 and 7 to choose an operation.

Report Emergency

Enter:

- Name
- Emergency type
- Location
- Description

The emergency report is kept in the system.

Report Lost Item

Enter:

- Name
- Lost item
- Last known location
- Description

The item is included on the list of lost items.

Report Found Item

Enter:

- Name
- Found item
- Location where it was found
- Description

The item is included on the list of found items.

Submit Complaint

Enter:

- Name
- Complaint category
- Location
- Complaint description

The complaint is stored in the system and a priority is automatically assigned according to the complaint category.

Search Lost Item

Input the name or part of the name of an item you're looking for.

The program looks through the stored lost-item reports and shows the ones that match.

View All Reports

This option displays:

- Total emergency reports
- Total lost items
- Total found items
- Total complaints
- Details of each report

Exit

Select option 7 to exit the program.

Project Purpose

The main purpose of Campus Safe is to provide a simple and organized way for students to report campus emergencies, manage lost and found items, and submit campus complaints through a single Python-based console application.

Future Improvements

Possible future improvements include:

- File-based data storage
- Database integration
- Graphical User Interface (GUI)
- Admin login and authentication
- Report deletion and management
- Better search and filtering options
- Email or notification support

Author

Debraj Roy
B.Tech – Computer Science
First Year
Session: 2026–27
