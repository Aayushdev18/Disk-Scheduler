# Backend - Disk Scheduling Algorithm Simulator

Django REST Framework backend for the Disk Scheduling Algorithm Simulator.

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run database migrations:
```bash
python manage.py migrate
```

## Running the Server

```bash
python manage.py runserver 8000
```

The API will be available at `http://localhost:8000`

## Project Structure

- `disk_scheduler/`: Django project settings
  - `settings.py`: Django configuration
  - `urls.py`: Main URL routing
- `api/`: Django REST API app
  - `views.py`: API view functions
  - `urls.py`: API URL routing
- `app/algorithms/disk_scheduling.py`: Implementation of all disk scheduling algorithms

## API Endpoints

- `GET /api/`: Root endpoint
- `GET /api/algorithms/`: List available algorithms
- `POST /api/simulate/`: Simulate a single algorithm
- `POST /api/compare/`: Compare all algorithms

## Django Admin

Access Django admin panel at `http://localhost:8000/admin/`

To create a superuser:
```bash
python manage.py createsuperuser
```
