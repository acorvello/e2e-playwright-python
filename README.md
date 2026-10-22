# Cross-Browser E2E Automation Framework
### Scalable End-to-End Web Testing Deployed with Playwright and Pytest

This repository implements a resilient and ultra-fast end-to-end (E2E) automation testing suite leveraging Playwright and Python. Built to execute complex user journeys against the OWASP Juice Shop platform, the framework isolates execution states natively to track performance, catch behavioral anomalies, and deliver high-fidelity continuous quality telemetry.

This suite complements the other repositories in the global portfolio (Cypress, Selenium, and API tests) and runs in the same integrated Jenkins pipeline.

## Engineering Highlights
* **Native Cross-Browser Parallelization:** Configured to orchestrate execution concurrently across Chromium, Firefox, and WebKit engines out-of-the-box, mitigating platform-specific drift.
* **Isolated Browser Contexts:** Eradicates cookies, cache, and session leakage by allocating fresh, independent browser contexts per execution block, maximizing pipeline stability.
* **Advanced Telemetry Collection:** Structured to capture HTML execution reports, network traces, and native screenshots on failure states to feed predictive test analysis tools.
* **Environment-Driven Architecture:** Decoupled base URL parameters to seamlessly scale from a local developer environment to multi-container containerized systems.

## Tech Stack and Dependencies
* **Automation Engine:** Playwright 1.48+ (Python bindings)
* **Test Orchestrator:** pytest with pytest-playwright
* **Infrastructure Layer:** Official Microsoft Playwright container base ready for headless integration inside Jenkins CI/CD loops.

## Project Structure
```
e2e-playwright-python/
├── requirements.txt
├── pytest.ini
└── tests/
├── conftest.py
└── test_juice_shop_login.py
```
## Covered Scenarios
* **Core Interface Verification:** Home page loads successfully and aggregates structured product components.
* **Navigation Flow:** Login interface renders correctly when triggered via the account dashboard menu.
* **Exception Handling Validation:** Security barrier triggers error display alerts upon receiving invalid credentials.

## Running Locally

**Prerequisites:** Python 3.10+ and a running instance of Juice Shop (locally or in a container).

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install --with-deps

pytest --base-url=http://localhost:3001 --browser chromium --browser firefox --browser webkit
```

Running via Docker (CI/CD Orchestration)

This repository is actively consumed by the docker-test-env orchestration project. The pipeline spins up Juice Shop and executes this testing suite inside the official mcr.microsoft.com/playwright/python container image, triggered and tracked seamlessly by a unified Jenkins pipeline. See that project's docker-compose.yml for the full setup.

Roadmap and Next Steps

• Integrate pytest-html to generate clean visual reports and archive them dynamically as CI artifacts.
• Expand the functional matrix to cover multi-step cart, basket management, and checkout flows.
• Inject backend component testing layer natively to complement client-side UI automation.

License

This repository is licensed under the MIT License. Feel free to clone, study, modify, and distribute the code for educational or portfolio purposes.

---
<sub>Keywords: Playwright, Python, Pytest, E2E Automation, Cross-Browser, UI Testing, Telemetry, Docker, CI/CD Jenkins, Headless Runner, Test Orchestration, Software Engineering.
