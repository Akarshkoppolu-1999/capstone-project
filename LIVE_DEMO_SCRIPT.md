# Live Demo Script: CI/CD Pipeline

Follow these steps for a perfect live demonstration of your project to your examiner or team.

## 🕒 Preparation
- Open **VS Code** with your project folder.
- Open **Jenkins** in your browser (`http://localhost:8080`).
- Open your **App** in your browser (`http://localhost:8081`).
- Open your **GitHub** repository.

---

## 🎭 The 5-Step Demo Script

### Step 1: Show the Current State
1. Open [http://localhost:8081](http://localhost:8081).
2. Click **Refresh Status** to show the database is working.
3. **Point out**: "This is the current live version deployed by Jenkins."

### Step 2: Make a Code Change (Live!)
1. Go to VS Code and open `frontend/index.html`.
2. Change the text in the `<h1>` tag (Line 49):
   - From: `<h1>Capstone CI/CD App</h1>`
   - To: `<h1>Akarsh's Live Demo!</h1>`
3. Save the file.

### Step 3: Trigger the Pipeline
1. Open your terminal in VS Code and run:
   ```bash
   git add .
   git commit -m "Demo: Live UI update"
   git push origin main
   ```
2. **Explain**: "I am pushing a code change. In a real production environment, this would auto-trigger the pipeline."

### Step 4: Watch Jenkins Work
1. Go to Jenkins and click **Build Now** (if it hasn't started automatically).
2. Open the **"Open Blue Ocean"** view or the Stage View.
3. **Explain as it runs**:
   - **Build**: "Docker is creating our multi-stage, secure images."
   - **Test**: "The system is running automated health checks."
   - **Deploy**: "Jenkins is updating the containers on the server."

### Step 5: Verify the Result
1. Once Jenkins finished (Green ✅), go back to [http://localhost:8081](http://localhost:8081).
2. **Refresh the browser**.
3. **The Big Reveal**: The title should now say **"Akarsh's Live Demo!"**.
4. Click **Refresh Status** to show that the database data was **NOT lost** during the update (Persistence!).

---

## 💡 Key Talking Points for the Demo
- **Zero Downtime (Simulated)**: "Notice how Jenkins updated the app without us having to manually stop and start Docker commands."
- **Data Safety**: "Even though the app updated, the visit count stayed the same because we used **Docker Volumes** for PostgreSQL."
- **Nginx Role**: "Nginx acted as the entry point, seamlessly routing us to the new version of the app."
