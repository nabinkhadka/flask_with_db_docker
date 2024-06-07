# Build and execute the docker-compose
1. Open your linux terminal and run the following
`docker-compose up --build`

Do not close this terminal

# Prepare database table
Open another terminal and do the following:

1. Get your db container's name using `docker ps` which will give list like the following
<img width="1203" alt="image" src="https://github.com/nabinkhadka/flask_with_db_docker/assets/6050613/30a7cfa8-e35c-474f-acd4-d0a5f463ecc9">

2. Then go inside the container using the command `docker exec -it <container_name> bash`. In my case it was `flask_with_db_docker-postgres-1` as selected in the screenshot above

3. Then run the psql shell using `psql -U postgres` command

4. Execute the table creation SQL query

   ```SQL
   CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
    );
   ```

# From browser check the following URL
`http://127.0.0.1:5001/users`

The response will be empty

Now using postman, try to add users to the table.

<img width="999" alt="image" src="https://github.com/nabinkhadka/flask_with_db_docker/assets/6050613/f1a57716-a23d-4017-a933-1996e80c1417">


Again go back to browser, you will see one record

<img width="611" alt="image" src="https://github.com/nabinkhadka/flask_with_db_docker/assets/6050613/5b4c98fa-ad6f-4102-bd6c-30ba5c81a8f6">


