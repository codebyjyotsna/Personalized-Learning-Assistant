CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    interaction_data JSON,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
