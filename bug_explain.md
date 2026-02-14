# **Consolidated Bug Log: Flask Application Architecture & Maintenance**

This log tracks critical errors related to Flask application structure, extension initialization, data persistence, and security configuration within the project codebase.

| Date | Bug Title | Context | Symptom | Cause | Fix | Lesson Learned |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **2026-02-14** | **GCP Transition & CLI Auth** | Migrating app from Render to GCP Free Tier (e2-micro). | `gcloud` command errors; SSH auth failure; SCP failed locally. | **1. Placeholders:** Placeholder strings like `[PROJECT_ID]` caused syntax errors. **2. Auth:** Cloud Shell session timed out. **3. Local CLI:** `gcloud` was not installed on local PC. | **1. Commands:** Used explicit, simplified `gcloud` commands. **2. Fallback:** Used browser-based folder upload in Cloud Shell for file transfer. **3. Auth:** Re-authenticated using `gcloud auth login`. | Use explicit Project IDs in commands; the GCP Console's browser upload is a reliable "no-install" fallback for file transfers. |
| **2025-10-05** | **SQL Conflict (Migration)** | Migrating from SQLite to PostgreSQL. | Migration failed; version mismatch error. | Error entering PostgreSQL identity data (version difference). | Created and configured a new DB specifically for PostgreSQL compatibility. | Always check version differences and dialect specifics before performing database migrations. |
