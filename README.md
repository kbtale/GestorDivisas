<h1 align="center">GestorDivisas</h1>

<p align="center">
  A Django-based dashboard to monitor USD and EUR exchange rates in Venezuela.
  <br>
  It aggregates data from official and parallel sources for real-time comparison.
  <br>
  <br>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-4.1-092E20?logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/UI-Tabler-blue?logo=tabler&logoColor=white" alt="Tabler" />
  <img src="https://img.shields.io/badge/License-MIT-purple" alt="License" />
</p>

<hr>

> [!NOTE]
> **Project Status: Archived.** This project is completed, read-only, and archived. It has been configured with local offline fallbacks to ensure dashboard visualization remains functional post-archival.

## Overview

**GestorDivisas** is a simple web tool that fetches and displays the current exchange rates for the Venezuelan Bolivar (VES). It consumes external APIs to provide a comparison between different market markers.

### Data Sources
* **BCV (Banco Central de Venezuela):** Official rate (via SICAD II data).
* **DolarToday:** Parallel market rate.
* **LocalBitcoins:** Crypto-exchange reference rate.

## Stack

* **Backend:** Django 4.1 (Python)
* **HTTP Client:** `requests` library for API consumption.
* **Frontend:** HTML5 with [Tabler](https://tabler.io/) (Bootstrap-based UI kit).
* **Data Source:** DolarToday S3 JSON endpoint.

## Features

* Displays current USD and EUR exchange rates.
* Compares rates from BCV, DolarToday, and LocalBitcoins.
* API Resilience: If the external DolarToday S3 JSON endpoint is offline or returns an invalid structure, the dashboard displays cached fallback exchange rates with a warning notice rather than throwing a 500 server error.

## Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Navigate to:
   ```
   http://127.0.0.1:8000/showdata/
   ```

## Verification

To run system configuration and dependency checks:
```bash
python manage.py check
```
