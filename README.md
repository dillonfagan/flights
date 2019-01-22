# Flights
Flights is a flight schedule visualizer to be used as a learning tool for beginner programmers.
It will be written in Python and simply print a flight schedule to the console.

Flight data will be read in from a `.csv` file and then displayed in a nicely formatted table that adapts to the given data.

This project should serve as a decent introduction to the principles of MVC.

## Data format
The flight data is stored in a `.csv` (comma-separated) file with the following columns:

`Airline`, `Flight`, `Arrives`, `Departs`, `Fare`

## Flights program
The flights program should run in the terminal and display the flight data in a neatly formatted table with headers for each column. The program should also offer the user a basic menu where they can choose what to display:

* List of all flights in order by airline and flight number
* List of all flights in order by departure time
* List of all flights within a given time range
* Flight with the lowest fare
* Average fare of a given airline

The program should continue running until the user chooses to quit it.
