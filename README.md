# Password Generator
A simple FastAPI application to generate random passwords of specified length.

## Prerequisites
 You should have installed [python3](https://www.python.org/downloads/) and [Git](https://www.git-scm.com/downloads)

## Installation
1. Clone the project from GitHub
    ```git
    git clone https://github.com/koushikromel/fluvi-task1.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```
    uvicorn main:app --host 0.0.0.0 --port 3000
    ```

## Endpoints
1. Generate Password
    Generate random password with specified length
    -   Method: GET
    -   Endpoint: http://0.0.0.0:3000/generate_password
    -   Parameters:
        - max_length: int
    -   Request: GET /generate_password
    -   Response: 
        ```json
            {
                "password": "nzZKFk3NNVtDKsA0rzUQcz6"
            }
        ```

## License
This Project is licensed under the MIT License - see the [License](https://choosealicense.com/licenses/mit/) file for details.