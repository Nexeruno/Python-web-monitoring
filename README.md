# Web Monitoring System

[![CI](https://github.com/Nexeruno/Python-web-monitoring/actions/workflows/ci.yml/badge.svg)](https://github.com/Nexeruno/Python-web-monitoring/actions/workflows/ci.yml)
[![Build and Publish Docker Image](https://github.com/Nexeruno/Python-web-monitoring/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/Nexeruno/Python-web-monitoring/actions/workflows/docker-publish.yml)

A simple website monitoring system written in Python.

The project regularly checks the availability of selected websites, measures response time, writes results to a log file, sends Slack alerts when a website is unavailable, and exposes metrics for Prometheus. The data is then displayed in a Grafana dashboard. The log file is also uploaded to AWS S3.

## Dashboard Preview
![Grafana Dashboard](screenshots/monitoring.jpg)

## Technologies Used
* Python
* Requests
* Prometheus Client
* Prometheus
* Grafana
* Docker Compose
* Slack Webhook
* AWS S3
* dotenv / `.env` configuration
* GitHub Actions (CI/CD)
* Trivy (security scanning)

## Features
* Website availability monitoring
* Response time measurement
* Slack alerts when a website is down
* Prometheus metrics
* Grafana dashboard (State timeline view)
* Log upload to AWS S3
* Secure configuration using `.env`
* Unit tests with 87% code coverage
* Multi-stage Docker build
* Docker healthcheck
* Automated CI/CD pipeline
* Docker image vulnerability scanning

## How to Run
1. Create `.env` file based on `.env.example`
2. Start the stack:
```bash
cd monitoring-stack
docker compose up -d --build
```
3. Open services:
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- Metrics: http://localhost:8000

## Testing
```bash
pip install -r requirements.txt
pytest --cov=monitoring_system test_monitoring.py
```

---

# Web Monitoring System

Jednoduchý monitoring webových stránek napsaný v Pythonu.

Projekt pravidelně kontroluje dostupnost vybraných webů, měří dobu odezvy, zapisuje výsledky do logu, odesílá upozornění do Slacku při výpadku a vystavuje metriky pro Prometheus. Data jsou následně zobrazena v Grafana dashboardu. Log soubor je zároveň nahráván do AWS S3.

## Použité technologie
* Python
* Requests
* Prometheus Client
* Prometheus
* Grafana
* Docker Compose
* Slack Webhook
* AWS S3
* dotenv / `.env` konfigurace
* GitHub Actions (CI/CD)
* Trivy (bezpečnostní skenování)

## Funkce
* Kontrola dostupnosti webů
* Měření odezvy
* Slack alert při výpadku
* Prometheus metriky
* Grafana dashboard (State timeline zobrazení)
* Upload logů do AWS S3
* Bezpečné ukládání konfigurace přes `.env`
* Unit testy s 87% pokrytím kódu
* Multi-stage Docker build
* Docker healthcheck
* Automatická CI/CD pipeline
* Skenování zranitelností Docker image

## Jak spustit
1. Vytvoř `.env` soubor podle `.env.example`
2. Spusť stack:
```bash
cd monitoring-stack
docker compose up -d --build
```
3. Otevři služby:
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- Metriky: http://localhost:8000

## Testování
```bash
pip install -r requirements.txt
pytest --cov=monitoring_system test_monitoring.py
```
