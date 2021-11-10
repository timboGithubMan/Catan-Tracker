# Catan-Tracker
A simple script I coded in python that uses Selenium to track resources in Colonist, an online version of Settlers of Catan.
The script is definitely inefficient and could be written in less lines of code, but it's very fast anyways and not worth my time to optimize.

Requires the selenium and numpy packages to be installed. 
Requires chromedriver.exe to be in C:\\
https://chromedriver.chromium.org/

Resource values on Colonist are hidden, so the script obtains information by parsing the chat box that outputs player moves.

Room for Improvement:

When players steal from another, it is not known which resource was stolen - by game design, it is a secret.
Although the script tracks the number of thefts between players, more logic is needed to deduce which resource in particular was stolen
(once a player has negative of a resource, it can be assumed that they must have stolen that resource - but if they've stolen from multiple players, you can not be sure who they stole it from).
