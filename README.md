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

## 📋 Overview

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
