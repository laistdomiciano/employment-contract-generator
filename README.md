# Employment Contract Generator API

## Overview
This is a Flask-based API that allows users to generate employment contracts. Users can choose from three types of contracts: Full-Time Employment, Part-Time Employment, and Freelance Contract. The application uses JWT for authentication and PostgreSQL for data storage.

## Features
- User registration and authentication
- Three types of contract templates
- Generate contracts based on user input
- Input validation and sanitization
- Secure endpoints with JWT
- Deployment configuration for Vercel/Render
- Unit testing with pytest
- API documentation with Swagger

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/contract-generator.git
    cd contract-generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```bash
    cp .env.example .env
    ```
   Update `.env` with your configuration.

5. Run the application:
    ```bash
    flask run
    ```

## Endpoints

- `/auth/register` - Register a new user
- `/auth/login` - Login and receive a JWT
- `/contract/generate` - Generate a contract based on selected type and user input (Authenticated)

## Deployment

To deploy the application to Vercel or Render, follow the respective platform's deployment instructions. Ensure to set the environment variables on the deployment platform.

## Testing

Run unit tests using pytest:
```bash
pytest
