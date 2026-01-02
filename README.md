# Capstone: 2-Tier Web App with Automated CI/CD

This project is a complete, production-ready CI/CD implementation for a 2-tier web application (Python Flask + PostgreSQL + Nginx). It is built to demonstrate modern DevOps practices including Multi-stage Docker builds, non-root security, and automated Jenkins pipelines.

##  Folder Structure
- **`backend/`**: The logic layer (API).
    - `app.py`: Flask application that connects to PostgreSQL and handles visit logic.
    - `dockerfile`: Multi-stage Dockerfile for the backend (Python slim + builder stage).
    - `requirements.txt`: Python dependencies (Flask, psycopg2, etc.).
- **`frontend/`**: The presentation layer (Web).
    - `index.html`: The user interface designed with modern CSS.
    - `nginx.conf`: Nginx configuration used as a **Reverse Proxy** to route traffic to the backend.
    - `dockerfile`: Multi-stage Dockerfile for the frontend (Nginx alpine).
- **`docker-compose.yml`**: Orchestrates the DB, Backend, and Frontend containers locally.
- **`Jenkinsfile`**: The automated pipeline script (Build -> Test -> Security -> Deploy -> Verify).
- **`DOCUMENTATION.md`**: Technical architecture and pipeline diagrams.

##  How to Run locally
1. Ensure your Port 8081 is free.
2. Run `docker-compose up --build`.
3. Open `http://localhost:8081`.

##  Tech Stack
- **Languages**: Python (Backend), HTML/CSS/JS (Frontend).
- **Database**: PostgreSQL 13.
- **Server**: Nginx (Web Server + Reverse Proxy).
- **Orchestration**: Docker Compose.
- **CI/CD**: Jenkins.
