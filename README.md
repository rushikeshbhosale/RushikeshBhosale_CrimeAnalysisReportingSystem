# Crime Analysis & Reporting System

Project Title: Crime Analysis and Reporting System (C.A.R.S.)

Description:
The Crime Analysis and Reporting System (C.A.R.S.) is a comprehensive Python software application designed to assist law enforcement agencies in managing and reporting crime data efficiently. This project implements a robust system focusing on object-oriented principles, SQL database interaction, control flow statements, loops, arrays, collections, exception handling, and unit testing.

Key Features:

1) Schema Design: The project includes a well-defined schema with entities such as Incidents, Victims, Suspects, Law Enforcement Agencies, Officers, Evidence, and Reports.
Service Provider Interface: An interface (ICrimeAnalysisService) and its implementation classes handle various functionalities like creating incidents, updating status, generating reports, and managing cases.
2) Database Connectivity: Utilizing SQL database interaction, the application establishes connections, reads connection properties from a property file, and performs CRUD operations.
3) Exception Handling: Custom exceptions are defined and thrown when needed, ensuring robust error handling and graceful degradation.
4) Main Module: A menu-driven application (MainModule) demonstrates the functionalities of the system, allowing users to interact with the implemented features.
5) Unit Testing: Unit tests validate the correctness and reliability of the system's components, ensuring that each functionality behaves as expected.

Directory Structure:

1) entity: Contains entity classes representing real-world entities with encapsulated data and behavior.
2) dao: Includes service provider interfaces and their implementation classes for database interaction.
3) exception: Houses user-defined exceptions to handle errors effectively.
4) util: Contains utility classes for database connection and property retrieval.
5) main: Features the main module demonstrating system functionalities through a menu-driven application.
