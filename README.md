# Compliment Generator API

The FastAPI Compliment Generator is a delightful and engaging web service that generates unique and heartwarming compliments. Built with FastAPI, it showcases the power of modern web frameworks to create efficient and fun APIs.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or later
- pip (Python package manager)

### Installing

1. **Clone the Repository**

    ```
    git clone https://github.com/Peakz/ComplimentGeneratorAPI.git
    cd ComplimentGeneratorAPI
    ```

2. **Create and Activate a Virtual Environment** (optional but recommended)

    For Windows:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

    For macOS and Linux:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Required Packages**

    ```
    pip install -r requirements.txt
    ```

### Running the Application

Run the FastAPI server with the following command:

```
uvicorn main:app
```

### Accessing the API

Once the server is running, visit `http://localhost:8000/compliment` in your browser or use tools like Postman to make GET requests and receive compliments.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
