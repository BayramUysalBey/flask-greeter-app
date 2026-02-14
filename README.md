# Flask Greeter App

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)

## 📌 Project Overview

**Flask Greeter App** is a containerized web application that demonstrates a modern deployment pipeline. Originally hosted on Render.com, it has been migrated to **Google Cloud Platform (GCP)** to leverage the "Always Free" tier.

**Live Demo**: [http://34.27.34.57:5000](http://34.27.34.57:5000)

The application allows users to enter their names and receive a personalized greeting, while maintaining a persistent count of all greetings served using a PostgreSQL backend.

---

## 🚀 Key Features

- **NAME GREETING**: Simple and interactive web interface.
- **PERSISTENCE**: PostgreSQL database records every interaction.
- **DOCKERIZED**: Fully portable environment using Docker and Docker Compose.
- **CLOUD READY**: Optimized for low-cost cloud hosting on GCE.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Flask (Web Framework)
- **Database**: PostgreSQL 15 (Alpine)
- **Production Server**: Gunicorn
- **Infrastructure**: Docker, Docker Compose
- **Cloud Provider**: Google Cloud Platform (Compute Engine e2-micro)

---

## ⚙️ Setup & Installation

### Using Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BayramUysalBey/flask-greeter-app.git
   cd sayHello
   ```

2. **Prepare Environment**:
   Copy `.env.example` to `.env` and configure your database credentials.

3. **Launch the Stack**:
   ```bash
   docker compose up --build
   ```

4. **Access the App**:
   Navigate to `http://localhost:5000` in your browser.

---

## 📂 Project Structure

```text
├── app.py                # Main Flask application logic
├── Dockerfile            # Container definition
├── docker-compose.yml    # Multi-container orchestration
├── boot.sh               # Entrypoint script for production
├── requirements.txt      # Python dependencies
├── templates/            # Jinja2 HTML templates
└── static/               # CSS and static assets
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
