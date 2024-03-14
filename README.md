# Électricité HackQc 2024

## Data

Data from the following sources is used. License information can be viewed by following each link.

| Dataset name         | URL     | Modifications |
|--------------|-----------|------------|
| Sources de l’électricité produite au Québec | https://www.donneesquebec.ca/recherche/dataset/sources-production-electricite-quebec | None |
| Consommation d'énergie et émissions de gaz à effet de serre des bâtiments municipaux de 2000 m² et plus | https://www.donneesquebec.ca/recherche/dataset/vmtl-consommation-emissions-batiments-municipaux | 5 buildings were selected from the original data and 3 were reconstructed by matching data from different existing ones with names that were not in the dataset. In all cases, geographical coordinates were added using Google Maps. |

## Project Setup

This project involves setting up the server and the UI separately. Follow the steps below:

### Server Setup

1. Navigate to the `/server` directory:
     ```bash
     cd server
     ```

2. Create a Virtual Environment using `venv`:
     ```bash
     python -m venv venv
     ```

3. Activate the Virtual Environment:
     ```bash
     source venv/bin/activate  # On Windows: ./venv/Scripts/activate
     ```

4. Install Required Packages:
     ```bash
     pip install -r requirements.txt
     ```

5. Download the data from Données Québec:
     ```bash
     python download.py
     ```

6. Run the Server:
   - Start the server using the main Python file:
     ```bash
     python main.py
     ```
   - The server will run at [`localhost:5000`](http://localhost:5000).
   - You can check the server health at [`localhost:5000/health`](http://localhost:5000/health)

### UI Setup

1. Navigate to the `/ui` directory:
     ```bash
     cd ui
     ```

2. Install Required Packages:
     ```bash
     npm install
     ```

3. Run the UI in Development Mode (with Hot-Reloading):
     ```bash
     npm run serve
     ```
     - The UI will run at [`localhost:8080`](http://localhost:8080).

4. Production Build:
     ```bash
     npm run build
     ```

## Project structure

The project follows a typical structure for a web application, with separate directories for the server and the UI.

### Server Structure

The server directory contains the backend code and is organized as follows:

- `api`: This directory contains the API routes.
- `infra`: This directory contains the infrastructure-related code, such as database connections or external service integrations.
- `infra/data`: This subdirectory contains the data-related files.
- `domain`: This directory contains the business logic and domain-specific code.
- `main.py`: This is the main entry point for the server.

### UI Structure

The UI directory contains the frontend code and is organized as follows:

- `src`: This directory contains the source code for the UI.
- `components`: This subsubdirectory contains reusable UI components.
- `assets`: This subdirectory contains static assets such as images or stylesheets.
- `main.js`: This is the main entry point for the UI.
