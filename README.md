# SFIA1 Project

SFIA Project 1: Online Library Website (By: Haris Munir)

Resources: 

Presentation => https://drive.google.com/file/d/1TisIeIpU3vXZpkvpPwtHtMVOyJV9IpEG/view?usp=sharing

Trello =>  https://trello.com/b/KEfmR0iO/sfia1-project

Website => http:// 34.89.44.111:5000/

Contents:

•	Brief about the project
•	Additional Requirements
•	My Approach / Database Structure
•	CRUD Satisfaction
•	ERD
•	CI Pipeline
•	Project Tracking (Trello, Risk Assessment, Testing, Front-End Design)
•	Issues
•	Future Improvements

Brief about the project:

Following objective are set up: Create a CRUD (utilises create, read, update and delete) application with usage of supported tools, methodologies and technologies, which were covered during the first 4 weeks of our Training. The major aspect for this project is to demonstrate, what I have been learned over this period.

Additional requirements have been set and are to be included:

•	A Trello board
•	A relational database, consisting of at least two tables that model a relationship
•	Clear documentation of the design phase, app architecture and risk assessment
•	A python-based functional application that follows best practices and design principles
•	Test suites for the application, which will include automated tests for validation of the application
•	A front-end website, created using Flask
•	Code integrated into a Version Control System which will be built through a CI server and deployed to a cloud-based virtual machine

My Approach:

I have decided to produce an online library app that allows the user to do the following:

Create a database with 3 table.

Table 1: User

ID => Primary key with automatic number
First and Last Name
Email
Password

Table 2: Books (Provided by the admin)

Includes following
Book ISBN as ID => Primary key with automatic number
Book title
Book author
Book genre

Table 3: Blog Post

ID => Primary key with automatic number
Title of the blog post
Author of the blog post
Content of the blog post
Date posted 

CRUD Satisfaction

Create =>

User create account
User can post a blog about the book

Read => 

User can read from Books database

Update =>

User can update his account information

Delete =>

Delete his blogs.

ERD:

 

As shown in the ERD, the app models a many-to-many relationship between User entities and Observation entities using an association table. This allows the user to create observation posts and tag multiple users in the database with one observation. Similarly, many observations can therefore be associated with a user.

CI Pipeline Failed to test

Trello was used to track the progress of the project (pictured below): https://trello.com/b/KEfmR0iO/sfia1-project

 

Risk Assessment

The risk assessment for this project can be found in full here: https://drive.google.com/file/d/15kd5iaEML6gLsbw4cDjZ7zivrPEBetZL/view?usp=sharing

Screenshot:

 

Front-End Design

 	 
 	 

Issues: The application is not working. Issues need to be identified in the Backend.

Future Improvements

First => Look in the code to ensure the functionality is working
Furthermore, allow additional functions, where books can be seen with images on the website
Implements search option

