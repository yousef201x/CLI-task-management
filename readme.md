# SQLite Database Initialization Script

This script initializes an SQLite database for managing tasks.

## Table of Contents

- [Database Schema](#database-schema)
- [Functions](#functions)
  - [openConnection](#openconnection)
  - [createCursor](#createcursor)
  - [endConnection](#endconnection)
  - [logError](#logerror)
  - [handleError](#handleerror)
  - [myTasks](#mytasks)
  - [searchTask](#searchtask)
  - [createTask](#createtask)
  - [updateTask](#updatetask)
  - [deleteTask](#deletetask)
- [Usage](#usage)
- [Notes](#notes)

## Database Schema

The script creates a 'tasks' table within the database with the following schema:

- **id**: INTEGER, primary key autoincremented
- **description**: TEXT, description of the task (cannot be empty)
- **due_date**: DATE, due date of the task (cannot be empty)
- **status**: TEXT, status of the task, defaults to 'pending' and can be 'pending' or 'completed'

## Functions

### openConnection

Function to establish a connection to the SQLite database.

### createCursor

Function to create a cursor object to execute SQL commands.

### endConnection

Function to close the cursor and connection.

### logError

Function to log errors to a log file.

### handleError

Function to handle errors by printing a message and logging the error.

### myTasks

Function to fetch tasks based on their status.

### searchTask

Function to search tasks based on a search term in description or due_date.

### createTask

Function to create a new task.

### updateTask

Function to update an existing task.

### deleteTask

Function to delete a task.

