CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(200) NOT NULL,
    contact_name VARCHAR(200) NOT NULL,
    phone VARCHAR(50),
    email VARCHAR(200),
    last_contacted DATE,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);