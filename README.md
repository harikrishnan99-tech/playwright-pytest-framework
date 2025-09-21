# Playwright Pytest Automation

Python automation framework for UI, API, and E2E testing using Playwright and pytest.

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

```bash
# Run by test type
pytest -m ui          # UI tests
pytest -m api         # API tests  
pytest -m e2e         # End-to-end tests

# Generate HTML report
pytest -m ui --html=reports/report.html --self-contained-html

# Run all tests
pytest
```

## Test Markers

- `@pytest.mark.ui_health_check` - UI tests
- `@pytest.mark.api_health_check` - API tests
- `@pytest.mark.e2e_health_check` - E2E tests
