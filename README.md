# Restful Booker API Test Automation

## Overview

This project demonstrates REST API testing using both Postman and Python against the Restful Booker API. API scenarios were initially explored and validated in Postman and then automated using Python, pytest, and the requests library. The project covers booking retrieval, query parameter filtering, booking creation, authentication, booking updates, partial updates, and deletion workflows.

## Technologies Used

- Python
- pytest
- requests
- Postman
- REST APIs
- GitHub
- Jenkins

## Project Structure

```text
restful_booker_api_tests/
│
├── tests/
│   ├── test_get_booking_ids.py
│   ├── test_get_booking.py
│   ├── test_get_booking_by_name.py
│   ├── test_get_booking_by_checkin.py
│   ├── test_get_booking_by_checkout.py
│   ├── test_create_booking.py
│   ├── test_create_token.py
│   ├── test_update_booking.py
│   ├── test_patch_booking.py
│   └── test_delete_booking.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── restful_booker_postman_collection.json
```

## Test Coverage

### Booking Retrieval

- Get all booking IDs
- Get booking details by booking ID
- Get booking IDs filtered by first name and last name
- Get booking IDs filtered by check-in date
- Get booking IDs filtered by check-out date

### Booking Management

- Create booking
- Generate authentication token
- Update booking (PUT)
- Partially update booking (PATCH)
- Delete booking

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

## Run All Tests

```bash
pytest -v
```

## Run Individual Tests

Examples:

```bash
pytest tests/test_get_booking.py -v
```

## Validations Performed

The test suite includes validation of:

- HTTP status codes
- Response JSON content
- Authentication token generation
- Response data fields
- Query parameter filtering
- Booking updates
- Booking deletion
- Basic response time validation

## Notes

Some tests require a valid booking ID. If a booking no longer exists, update the booking ID before running the test.

## Jenkins Integration

The project can be executed using Jenkins.

Typical Jenkins workflow:

1. Pull source code from GitHub
2. Install project dependencies
3. Execute pytest test suite
4. Display test execution results

Example Jenkins build commands:

```bash
pip install -r requirements.txt
pytest -v
```
