-- Create the 'users' table to store user information
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    chat_id BIGINT NOT NULL UNIQUE, -- Telegram chat ID for message routing
    username VARCHAR(50) NOT NULL UNIQUE,         -- Telegram username
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- User creation timestamp
);

-- Create the 'friendships' table to store user friendships
-- NOT TESTED
CREATE TABLE friendships (
    id SERIAL PRIMARY KEY,                          -- Unique ID for each friendship
    user_id INT NOT NULL,                           -- First user's ID
    friend_id INT NOT NULL,                         -- Second user's ID
    status VARCHAR(20) DEFAULT 'pending',           -- Friendship status: 'pending', 'accepted', 'declined'
    requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the friend request
    accepted_at TIMESTAMP,                          -- Timestamp when the friendship is accepted
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    CONSTRAINT fk_friend FOREIGN KEY (friend_id) REFERENCES users (id) ON DELETE CASCADE,
    CONSTRAINT unique_friendship UNIQUE (user_id, friend_id), -- Prevent duplicate friendships
    CONSTRAINT check_no_reverse_friends CHECK (user_id < friend_id); -- Ensure user_id < friend_id for consistency 
);


-- Create the 'mails' table to track sent messages
CREATE TABLE mails (
    id SERIAL PRIMARY KEY,
    sender_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Sender's user ID
    recipient_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Recipient's user ID
    content TEXT NOT NULL,                         -- Message content
    status VARCHAR(50) NOT NULL DEFAULT 'in_transit', -- Message status (in_transit, delivered, lost)
    sent_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time the mail was sent
    delivery_time TIMESTAMP,                        -- Time the mail was delivered or lost
    delivery_eta TIMESTAMP                         -- Estimated time of arrival for the mail
);

CREATE TABLE user_locations (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- User's ID
    latitude FLOAT NOT NULL,                                    -- Latitude of the user
    longitude FLOAT NOT NULL,                                   -- Longitude of the user
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP              -- When the location was last updated
);

