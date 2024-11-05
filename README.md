# Blog-API-Django

## Description

BlogAPI is a RESTful web service for managing blog posts, user authentication, and user profiles.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alexpeain/BlogAPI.git
   ```

2. ### Setup Virtual Environment

   ```bash
   python -m venv venv
   ```

   ### On Window

   ```bash
   venv\Scripts\activate
   ```

   ### On MacOs /Linux

   ```bash
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .**gitignore** file to Root Project.
   Add the **.venv/** Directory to .gitignore
5. Run the migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a Superuser

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file in the .**gitignore** and add the following variables:

```bash
DEBUG=True

SECRET_KEY=your_secret_key

DATABASE_URL=sqlite:///db.sqlite3
```

## Endpoints

| Endpoint                          | HTTP Verb | Description                       |
| --------------------------------- | --------- | --------------------------------- |
| /                                 | GET       | Root endpoint                     |
| /:pk/                             | GET       | Retrieve specific blog post by ID |
| /users/                           | GET       | List all users                    |
| /users/:pk/                       | GET       | Retrieve specific user by ID      |
| /rest-auth/registration           | POST      | Register a new user               |
| /rest-auth/login                  | POST      | Login a user                      |
| /rest-auth/logout                 | GET       | Logout a user                     |
| /rest-auth/password/reset         | POST      | Request password reset            |
| /rest-auth/password/reset/confirm | POST      | Confirm password reset            |

## Usage Examples

### Retrieve All Users

```bash
curl -X GET http://localhost:8000/api/v1/users/
```

## Available Filters

You can filter the blog posts using the following query parameters:

- `?title=example` - Filter by title containing "example".
- `?author=2` - Filter by the author with ID 2.
- `?created_at=2024-11-01T00:00:00Z` - Filter by posts created on or after the specified date.

### Example Request

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/posts/?author=2&created_at=2024-11-01T00:00:00Z"
```

## Authentication

This API uses token-based authentication. After registering or logging in, you will receive a token which must be included in the `Authorization` header for subsequent requests.

## Testing

To run tests, use the following command:

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
