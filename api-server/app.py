from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)
"""
Replace these values with your PostgreSQL's container name
You can get it using the following command
> docker ps | grep postgres
"""
DB_HOST = 'flask_with_db_docker-postgres-1'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'postgres'
#
# # Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()


@app.route("/users", methods=["GET"])
def list_users():
    # return {"hello": "worlding"}
    # Example: Execute a SELECT query to fetch all users from the 'users' table
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()

    # Convert the result to a JSON format
    user_list = [{'id': user[0], 'name': user[1], 'email': user[2]} for user in users]

    return jsonify(user_list)


@app.route("/users", methods=["POST"])
def create_user():
    # Get the JSON data from the request body
    data = request.json

    # Extract user information from the JSON data
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Example: Execute an INSERT query to insert a new user into the 'users' table
    cur.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s);', (name, email, password))
    conn.commit()  # Commit the transaction

    # Return a success message
    return jsonify({"message": "User created successfully"}), 201


# Start the app in debug mode
app.run(host="0.0.0.0", port=5000, debug=True)

# Something
