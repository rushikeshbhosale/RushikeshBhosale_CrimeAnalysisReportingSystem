create database CrimeReportingSystem;
use CrimeReportingSystem;

CREATE TABLE Incident (
    incident_id INT PRIMARY KEY AUTO_INCREMENT,
    incident_type VARCHAR(100) NOT NULL,
    incident_date DATE NOT NULL,
    location_latitude DECIMAL(10, 8) NOT NULL,
    location_longitude DECIMAL(11, 8) NOT NULL,
    description TEXT,
    status VARCHAR(50) NOT NULL,
    victim_id INT,
    suspect_id INT,
    FOREIGN KEY (victim_id) REFERENCES Victim(victim_id) ON DELETE CASCADE,
    FOREIGN KEY (suspect_id) REFERENCES Suspect(suspect_id) ON DELETE CASCADE,
    CHECK (status IN ('Open', 'Closed', 'Under Investigation'))
);

CREATE TABLE Victim (
    victim_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address TEXT,
    phone_number VARCHAR(20) UNIQUE
);

CREATE TABLE Suspect (
    suspect_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address TEXT,
    phone_number VARCHAR(20) UNIQUE
);

CREATE TABLE LawEnforcementAgency (
    agency_id INT PRIMARY KEY AUTO_INCREMENT,
    agency_name VARCHAR(255) NOT NULL,
    jurisdiction VARCHAR(255) NOT NULL,
    contact_information TEXT
);

CREATE TABLE Officer (
    officer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    badge_number VARCHAR(20) NOT NULL UNIQUE,
    `rank` VARCHAR(50),
    contact_information TEXT,
    agency_id INT,
    FOREIGN KEY (agency_id) REFERENCES LawEnforcementAgency(agency_id) ON DELETE CASCADE
);

CREATE TABLE Evidence (
    evidence_id INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT,
    location_found VARCHAR(255),
    incident_id INT,
    FOREIGN KEY (incident_id) REFERENCES Incident(incident_id) ON DELETE CASCADE
);

CREATE TABLE Report (
    report_id INT PRIMARY KEY AUTO_INCREMENT,
    incident_id INT,
    reporting_officer_id INT,
    report_date DATE,
    report_details TEXT,
    status VARCHAR(50),
    FOREIGN KEY (incident_id) REFERENCES Incident(incident_id) ON DELETE CASCADE,
    FOREIGN KEY (reporting_officer_id) REFERENCES Officer(officer_id) ON DELETE CASCADE,
    CHECK (status IN ('Draft', 'Finalized'))
);

CREATE TABLE Cases (
    case_id INT PRIMARY KEY AUTO_INCREMENT,
    case_description TEXT,
    case_status VARCHAR(50)
);

CREATE TABLE IncidentType (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(100) NOT NULL
);
