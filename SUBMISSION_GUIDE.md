# Submission & Presentation Guide

This guide details exactly what we did, the project history, and where you should take screenshots for your final presentation.

## 📝 Part 1: Step-by-Step History (What we did)
If your examiner asks how you built this, here is the order:
1.  **Architecture Design**: We planned a 2-tier app (Frontend + Backend) with a PostgreSQL database.
2.  **Coding the App**: 
    - Created a **Flask Backend** that tracks "Visitor Counts" in a database.
    - Created an **Nginx Frontend** with a button to refresh the count.
3.  **Dockerization**: We wrote custom `Dockerfiles`. We used **Multi-stage builds** (a builder stage and a final stage) to make the images tiny and secure (non-root users).
4.  **Local Orchestration**: We used `docker-compose.yml` to make all 3 containers talk to each other on a private network.
5.  **Jenkins Pipeline Setup**: We wrote a `Jenkinsfile` to automate everything. 
6.  **Troubleshooting (Crucial for presentation!)**: We solved three major real-world DevOps problems:
    - **Permissions**: Jenkins couldn't talk to Docker until we fixed the socket permissions.
    - **Checkout**: Jenkins had an empty workspace until we configured "Pipeline from SCM".
    - **Port Conflicts**: We moved the app from 8080 to 8081 because Jenkins was already using 8080.
7.  **Reverse Proxy**: We added an Nginx configuration so that the user only visits one port (8081) and Nginx handles the communication with the backend.

---

## 📸 Part 2: Where to Take Screenshots (For your slides)

### 1. The Jenkins "Green" Pipeline
- **Go to**: Your Jenkins dashboard.
- **Screenshot**: The main status page of the `capstone-app` showing the successful "Weather" icon and the green stages (Build, Test, Security, Deploy).
- **Why**: This proves your automation is working.

### 2. Jenkins Console Output (The End)
- **Go to**: Current Build -> Console Output.
- **Screenshot**: Scroll to the very bottom where it says `Finished: SUCCESS`.
- **Why**: Official proof of a passed build.

### 3. Docker Container List
- **Command**: Run `docker ps` in your terminal.
- **Screenshot**: The table showing 3 containers running (`db`, `backend`, `frontend`).
- **Why**: Proves the deployment stage actually worked on your machine.

### 4. Image Size Optimization (Syllabus Requirement!)
- **Command**: Run `docker images` in your terminal.
- **Screenshot**: The lines showing `capstone-app-backend` and `capstone-app-frontend`.
- **Why**: Show the examiner that the images are small (likely under 100MB-200MB) thanks to multi-stage builds. Compare these to the original `python` or `nginx` image sizes if possible.

### 5. Final Web Application (The Result)
- **Go to**: `http://localhost:8081` in your browser.
- **Screenshot**: The UI showing "Total Visits: X" (where X is a number higher than 1).
- **Why**: This is the "Product" you delivered.

### 6. GitHub Repository
- **Go to**: Your GitHub project page.
- **Screenshot**: The file list showing all folders and the `README.md` / `DOCUMENTATION.md`.
- **Why**: Shows your code is organized and version-controlled.

---

## 🎓 Part 3: Examiners Tips
- If they ask about **Security**: Mention we use **non-root users** inside Docker so that if the app is hacked, the hacker doesn't get root access to the server.
- If they ask about **Automation**: Mention the **Jenkinsfile** uses a "Pipeline-as-Code" approach.
- If they ask about **Scalability**: Mention the **Nginx Reverse Proxy** allows us to add more backend servers easily in the future.
