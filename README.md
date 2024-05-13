# Crime Analysis and Reporting System (C.A.R.S.)

## Introduction
Welcome to the Crime Analysis and Reporting System (C.A.R.S.) project! This project aims to develop a comprehensive system for managing crime incidents, victims, suspects, law enforcement agencies, officers, evidence, and reports using Python programming language. The system provides law enforcement agencies with a robust platform for crime data management, analysis, and reporting.

## Technologies Used - 
- **Python**
- **MySQL**
- **GIT**

## Project Structure
The project follows a modular structure, with different components organized into packages:

- **entity**: Contains entity classes representing real-world entities such as incidents, victims, suspects, law enforcement agencies, officers, evidence, and reports. These classes encapsulate data and behavior related to each entity.
- **dao**: Contains service provider interfaces (SPIs) and their implementations for interacting with the database. This package handles database operations such as creating incidents, updating incident status, searching incidents, generating reports, and managing cases.
- **exception**: Contains user-defined exceptions that are thrown and handled within the application. These exceptions help in handling error scenarios gracefully and provide meaningful feedback to users.
- **util**: Contains utility classes for database connection management and property file handling. These classes facilitate establishing connections to the database and retrieving database configuration properties.
- **main**: Contains the main module of the application, which demonstrates the functionalities in a menu-driven console application. Users interact with the system through this module, accessing various features and functionalities.

## Database Schema Design
The database schema for the Crime Analysis and Reporting System includes tables for incidents, victims, suspects, law enforcement agencies, officers, evidence, and reports. Relationships between these tables are defined using foreign keys to maintain data integrity.

## Key Functionalities
The project implements the following key functionalities:

1. **Incident Management**: Creating, updating, and searching incidents based on various criteria such as incident type, date range, and status.
2. **Victim and Suspect Management**: Managing victim and suspect information associated with incidents.
3. **Law Enforcement Agency and Officer Management**: Managing law enforcement agency and officer details.
4. **Evidence Management**: Associating evidence with incidents for further investigation.
5. **Report Generation**: Generating reports for incidents by reporting officers.
6. **Case Management**: Creating and managing cases associated with multiple incidents.
7. **Database Interaction**: Establishing a connection to the SQL database and performing database operations such as CRUD operations, data retrieval, and report generation.

## Service Provider Interface/Abstract Class
The `ICrimeAnalysisService` interface defines methods for creating incidents, updating incident status, searching incidents, generating reports, creating cases, and managing case details. Implementation classes provide concrete implementations for these methods, interacting with the database to perform the required operations.

## Exception Handling
The project incorporates exception handling mechanisms to gracefully handle error scenarios and provide meaningful feedback to users. User-defined exceptions are thrown and handled within the application to handle scenarios such as incident number not found.

## Main Method
The `MainModule` class contains the main method of the application, where all the implemented functionalities are triggered and demonstrated through a menu-driven console application.

## Unit Testing
Unit testing is essential to ensure the correctness and reliability of the Crime Analysis and Reporting System. Test cases can be created using Python's unittest framework to test various components of the system, such as incident creation, incident status update, report generation, and case management.

## GitHub Repository
The project code is hosted on GitHub. You can access the repository [[here](https://github.com/rushikeshbhosale/RushikeshBhosale_CrimeAnalysisReportingSystem.git)]
