# Basic FastAPI CRUD Example

## Project Aim
This project serves as a minimal, entry-level example of a RESTful API built with Python and the FastAPI framework. It demonstrates the basic Create, Read, Update, Delete (CRUD) operations using an in-memory data store.

## Technical Implementation
The application is built with FastAPI and uses Python's standard data structures (a list) to simulate a database. It defines endpoints for creating and retrieving user data. The API is designed to be run locally using an ASGI server like Uvicorn.

## Key Features
- **FastAPI Framework:** Built on the high-performance FastAPI web framework.
- **In-Memory Database:** Uses a simple Python list to store data, making it easy to run without a database setup.
- **Basic API Operations:** Implements `GET` and `POST` endpoints for reading and creating user resources.

## Setup Instructions
- **Install dependencies:** `pip install fastapi uvicorn`
- **Run the API server:** `uvicorn main:app --reload`

## System Diagram
```mermaid
graph TD
    A[Client] --> B{FastAPI Server};
    
    subgraph "API Endpoints"
        C[/]
        D[/users/ - GET]
        E[/users/ - POST]
    end

    subgraph "Data Store"
        F[(In-Memory List)]
    end

    B --> C;
    B --> D;
    B --> E;

    D -- Reads from --> F;
    E -- Writes to --> F;
```
