# project1

## Fundamental Project

## Resources
Trello  https://trello.com/b/Lip5TLbt

## Brief: Project Outline

A Games list organiser that allows users to create and manage their personal games collection, adding information taken from a game database that features content such as the game’s title, age rating, console platform and other details. It will allow the function of creating new inputs if the game is not already in the database, also letting the users create multiple lists at will. It will allow the user to Read a short description for each game, Update details on their lists adding and deleting games from their lists. The application is running on a Google Cloud Ubuntu 18.04 virtual machine, hosted on a GCP MySQL server.

## Requirements
### My requirements: 
•	Trello Board
•	SQL relationship Database with at least two tables within a relationship
•	Documentation of the chosen methodologic study that breaks down the process and decrypt the risks involved of the said app
•	Various tests of the application including automated testing
•	Front-End website
•	CI Server design and implementation, integrating code through a Version Control System (VCS) and deploying to a cloud-based virtual machine

## My Plan
My goal is to create an application that stores a database of games and consoles and allows users to interact with the database through lists. The plan to execute the idea is:
•	Create User Controlled Lists that contains the following information:
o	List ID
o	Title of the List
o	List’s description about the features of it
o	Favourites from the user
o	Date of Entry, games that have been added into the database and when.
•	Read game and console description pages that will give users further insight into each of the entities that are to be added to each person’s lists.
•	Update their profile and user list information, editing details they may have got incorrect or re-establishing information.
•	Delete their account, their personalised lists or games within their lists.

## Architect
### Database Structure
![erdfirst](https://github.com/AndreM132/project1/blob/master/folder/first%20drawio.jpg)
### ERD diagram 1
This was the first ERD diagram iteration. Including all the main sections of the initial program idea of functionality where users would log in and have databases for each games and consoles. Including access to their personal lists.
![erd](https://github.com/AndreM132/project1/blob/master/folder/ERD%20diagram%20(1).jpg)
### ERD Diagram 2
As presented in the ERD diagram, the app follows a couple different relationships between the tables. For instance, from Users to Lists is a one to many relationships where a user can take advantage of having only one list to multiple. Whereas a List is mandatory to be linked to one user, as it is personalised by the user who created it. The Games & Consoles table holds a one to many relationships with Lists also, being one game/console can be linked or multiple. Finally, a list can either feature no games/consoles, or have many included. 

## CI Pipeline
![cipipeline](https://github.com/AndreM132/project1/blob/master/folder/struct.JPG) 

The image presented is the diagram of the CI pipeline used to function the application. It is a breakdown of the services and tools used to develop and deploy a well-tested functioning program, and the services chosen within the pipeline provide the most efficient method of rapid development to be automated and tested. In theory the code provided into the pipeline should be controlled by GIT and fed into the automated CI server Jenkins via webhook to ensure whenever the code is running, Jenkins is being automatically updated and aware of any changes. The webhook acts as a gateway to the CI server linking the program.  The testing environment was Flask, using GCP virtual machines to host our application code. Pytest was used to perform these test functions and check over coverage of tests in results.

## Project Planning
Trello  https://trello.com/b/Lip5TLbt
![trello](https://github.com/AndreM132/project1/blob/master/folder/trello.JPG) 
### Trello Board
The Trello board displays a breakdown of the project and process that had been thought and worked on to produce the final application. The project stages move from left to right as any finished tasks are updated to ensure clarification of what jobs are left are clearly displayed. 

## Implementation 
![home](https://github.com/AndreM132/project1/blob/master/folder/home.JPG)
Home Page: The Home page is the initial start point of the application, giving you choices within the navigation bar to go to different areas of the application.
![about](https://github.com/AndreM132/project1/blob/master/folder/about.JPG) 
About Page: The about page is to give a brief description of what the application is set to do, giving you the option of accessing the navigation bar to traverse to other pages.
![games](https://github.com/AndreM132/project1/blob/master/folder/games.JPG)
Games Page: The Games page displays the full database of games that are stored already. This displays in table formatting the games ID, title, age rating, price, description and console title for users to input their information into the fields above to add to the database. 
![lists](https://github.com/AndreM132/project1/blob/master/folder/lists.JPG)
Lists Page: On this page users are able to create a new list of their own where they can fill in field information such as their first name, last name, title of their list, description, favourite console and the select games ID from the database that they’d like to add.
![update](https://github.com/AndreM132/project1/blob/master/folder/update.JPG)
Update: The update page features a dynamic url that directs users to this page through the Update button on the Lists page. This will allow users to edit and change their information of their list details.
![addgame](https://github.com/AndreM132/project1/blob/master/folder/addgame.JPG)
Add game: Giving the user the ability to add a game by its game ID to their own list, as well as the game title to clarify the two fields.

## Risk Assessment
![risk](https://github.com/AndreM132/project1/blob/master/folder/r.JPG)
Risk Assessment diagram

## Testing
![test1](https://github.com/AndreM132/project1/blob/master/folder/Capture2.JPG)
75% Test Coverage: Unit testing on application folders equalled at 75% coverage overall
![test2](https://github.com/AndreM132/project1/blob/master/folder/inttest.JPG)
Integration testing had passed successfully.
![jenkins](https://github.com/AndreM132/project1/blob/master/folder/jenkins.JPG) 
Jenkins: Had actively been running in the program, allowing the ability to use the same external IP address to access the application through Jenkins, using port 8080 due to it being java based.


## Future Improvements
The building of the application was successful as the app was able to run CRUD functions. It allowed a user to create a new entity into the games database, and to create their own list. Reading data directly from the database in a table manor. That displayed beneath the input forms. This went well for the list page as more functionality had been implemented such as the delete and update functions of the program that allow users to update their fields information or remove the list all together if they no longer want it.

Testing the project had proved at slight difficult due to ensuring the correct tests had been applied to the project’s test files. All functions running within the program were tested and checked to result in the 75% overall coverage. This included the successful Integration testing in which had passed.

Working on the update function for the program had proved difficult as well as there had been many variations of how the function should be performed, yet figuring out the correct to get the page dynamically leading to a new url to update the form was a task. The function’s route had to be altered so it would increment to lead to its update page and that was the hardest part of the task. Yet once understanding how dynamic urls work, the task at hand seemed to make more sense.

In the future I would improve these factors about my program and its testing:
•	Have a functioning ‘Add Game’ button that would allow users to add games into their specific lists
•	Let users create an account and only access lists if they’re logged in.
•	Give users the ability to post comments on game’s specific description pages, where multiple users could leave posts to engage more within the application.
•	Allow users to link a game to a number of different console lists if they own the platforms.
•	Update specific fields within the update for instead of having to retype in all field entries.
•	Improve testing coverage to ensure more of the application is covered by testing and running as efficient as possible.


