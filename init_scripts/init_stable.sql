CREATE TABLE events (
    id VARCHAR(36) NOT NULL, -- Duh. No UUID in MySQL :(
    name VARCHAR(256),
    info TEXT,
    PRIMARY KEY (id)
);
