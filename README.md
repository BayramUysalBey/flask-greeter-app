# Flask Greeter App (Containerized Demo)

This is a simple Flask application that serves as a demonstration of production-ready architecture.

## Features

- Fully containerized with Docker Compose.
- Persists data using PostgreSQL.
- Uses Gunicorn for production server emulation.

## Requirements

- Docker Desktop (running)

## Setup and Run (One Command)

1. **Clone the repository:**
   `git clone [your-repo-url]`

2. **Create the Secret File:**
   Copy the provided `.env.example` file to `.env` and fill in the POSTGRES_PASSWORD.
   **(We will create the .env.example next).**

3. **Build and Launch the Stack:**
   `docker compose up --build`

The application will be available at <http://localhost:5000>.
