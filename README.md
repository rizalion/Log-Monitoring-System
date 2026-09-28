# Log Monitoring and Security Alert System

A Flask-based web application that analyzes system log files, detects suspicious security events, calculates risk scores, generates alerts, and visualizes security activity through an interactive dashboard.

The project simulates a basic **Security Operations Center (SOC)** workflow and demonstrates fundamental concepts of log analysis, threat detection, security alerting, and risk assessment.

---

## Project Overview

Organizations generate large amounts of system and authentication logs. Manually reviewing these logs can make it difficult to identify suspicious activity quickly.

This project provides a simple automated solution that:

1. Accepts log files through a web interface.
2. Parses the uploaded logs into structured events.
3. Detects suspicious activities using rule-based detection.
4. Identifies repeated failed login attempts.
5. Flags unknown or unrecognized events.
6. Calculates an overall security risk score.
7. Assigns a risk level.
8. Generates security alerts.
9. Visualizes the results through a web dashboard.

The system is designed as an educational implementation of a simplified SOC/log-monitoring workflow.

---

## Key Features

### Log File Upload

Users can upload log files through the Flask web interface for automated analysis.

### Log Parsing

The uploaded file is processed and converted into structured security events that can be analyzed by the detection engine.

### Failed Login Detection

The system monitors failed login events and identifies repeated failures associated with the same user.

This can be used to demonstrate detection of potential **brute-force login behavior**.

### Unknown Event Detection

Events that do not match the recognized log patterns are classified as unknown and treated as suspicious.

### Risk Scoring

A rule-based scoring mechanism evaluates detected events and produces an overall risk score.

The resulting risk level is categorized as:

* LOW
* MEDIUM
* HIGH

### Security Alert Generation

The system generates alerts when suspicious activity is detected and categorizes the alerts according to their severity.

### Security Dashboard

The dashboard presents key security information including:

* Total events
* Successful logins
* Failed logins
* Risk score
* Risk level
* Generated security alerts

### Data Visualization

Charts are used to make security activity easier to understand, including:

* Successful vs. failed logins
* Event distribution
* Alert severity distribution

---

## System Architecture

The application follows a simple processing pipeline:

```text
                    ┌──────────────────┐
                    │   User Uploads   │
                    │     Log File     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Log Parser    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Threat Detector  │
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    ▼                  ▼
             Failed Login       Unknown Events
              Detection           Detection
                    │                  │
                    └────────┬─────────┘
                             ▼
                    ┌──────────────────┐
                    │  Risk Calculator │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Alert Generation │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Security Dashboard│
                    │   + Visualizations│
                    └──────────────────┘
```

---

## Detection Methodology

The project uses **rule-based security detection** rather than machine learning.

### 1. Failed Login Detection

The system examines login-related events and tracks failed attempts.

Repeated failed attempts for the same user can indicate potential brute-force activity.

### 2. Unknown Event Detection

Events that do not correspond to recognized patterns such as:

```text
LOGIN_SUCCESS
LOGIN_FAILED
```

are classified as unknown events and flagged for further investigation.

### 3. Risk Calculation

The detected security events are passed to a risk calculation component.

The risk calculator considers the detected event types and their frequency to produce:

```text
Risk Score
     ↓
Risk Level
     ↓
LOW / MEDIUM / HIGH
```

### 4. Alert Generation

Detected suspicious activity is converted into security alerts containing relevant information about the event and its severity.

---

## Example Workflow

A typical analysis follows this process:

```text
Upload Log File
      ↓
Read Log Entries
      ↓
Parse Events
      ↓
Analyze Event Patterns
      ↓
Detect Suspicious Activity
      ↓
Calculate Risk
      ↓
Generate Alerts
      ↓
Display Dashboard
```

---

## Technologies Used

| Technology         | Purpose                             |
| ------------------ | ----------------------------------- |
| Python             | Core application and security logic |
| Flask              | Web application framework           |
| HTML               | Dashboard structure                 |
| CSS                | User interface styling              |
| JavaScript         | Client-side functionality           |
| Chart.js           | Security data visualization         |
| Visual Studio Code | Development environment             |
| Windows            | Development operating system        |

---

## Project Components

The application is organized around several logical components:

### Log Parser

Responsible for reading uploaded logs and converting raw entries into structured events.

### Threat Detector

Applies security rules to identify suspicious behavior such as:

* Repeated failed logins
* Unknown events

### Risk Calculator

Processes detected events and determines:

* Risk score
* Risk level

### Alert Generator

Creates security alerts based on detected suspicious events.

### Dashboard

Presents the analysis results and visualizations through the Flask web interface.

---

## Dashboard

The security dashboard provides a centralized view of the analyzed log data.

It displays:

```text
Total Events
Successful Logins
Failed Logins
Risk Score
Risk Level
Security Alerts
```

Charts provide visual representations of event and alert distributions.

---

## Example Security Events

The system can work with events such as:

```text
LOGIN_SUCCESS
LOGIN_FAILED
```

Repeated failed login events can be used to demonstrate suspicious authentication behavior.

Unknown events are also detected and flagged by the system.

---

## Running the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
cd log-monitoring-security-alert-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

If a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

Otherwise, install Flask:

```bash
pip install flask
```

and any additional dependencies used by the project.

### 5. Run the Application

```bash
python app.py
```

The Flask development server will start locally.

Open the displayed local address in a web browser.

### 6. Upload a Log File

Use the web interface to upload a supported log file and start the analysis.

---

## Testing

The application can be tested using different log files containing different event patterns.

### Test Case 1 — Normal Activity

A log containing successful login events should produce a relatively low level of suspicious activity.

### Test Case 2 — Failed Login Activity

A log containing repeated failed login attempts can trigger failed-login detection and corresponding alerts.

### Test Case 3 — Unknown Events

A log containing unrecognized event types should cause the system to flag unknown events.

### Test Case 4 — Mixed Activity

A log containing successful logins, failed logins, and unknown events demonstrates the complete analysis pipeline and produces a combined risk assessment.

---

## Security Concepts Demonstrated

This project provides practical exposure to:

* Security log analysis
* Authentication monitoring
* Brute-force detection concepts
* Rule-based threat detection
* Security alert generation
* Risk scoring
* Event classification
* SOC monitoring concepts
* Security visualization
* Web-based security applications

---

## Limitations

This project is an educational security monitoring system and has several limitations:

* Detection is rule-based rather than machine-learning based.
* It analyzes uploaded log files rather than continuously monitoring a live production environment.
* Detection rules are limited to the implemented event patterns.
* Risk scoring is based on predefined logic.
* It does not replace a production SIEM or SOC platform.

---

## Future Improvements

Possible extensions include:

* Real-time log monitoring
* Support for multiple log formats
* Database-based log storage
* User authentication
* More advanced threat-detection rules
* IP-based threat intelligence
* Email/SMS alert notifications
* Machine-learning-based anomaly detection
* SIEM-style event correlation
* Interactive investigation and filtering
* Deployment using Docker or cloud infrastructure

---

## Project Information

**Project:** Log Monitoring and Security Alert System
**Course:** Essentials of Information Security
**Institution:** HITEC University, Taxila
**Department:** Computer Science
**Semester:** Spring 2026 — 6th Semester
**Section:** 6C
**Instructor:** Eman Ali

### Authors

**Muhammad Huzaifa — 23-CS-007**
**Muhammad Awais — 23-CS-055**

---

## Disclaimer

This project was developed for educational purposes to demonstrate fundamental cybersecurity monitoring and log-analysis concepts. It is a simplified simulation and is not intended to replace a production Security Information and Event Management (SIEM) system.
