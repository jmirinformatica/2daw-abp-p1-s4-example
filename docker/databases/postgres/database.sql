CREATE TABLE stores (
    id SERIAL PRIMARY KEY, 
    nom TEXT NOT NULL
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY, 
    store_id INTEGER NOT NULL, 
    nom TEXT NOT NULL, 
    unitats INTEGER NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    email TEXT NOT NULL UNIQUE, 
    role TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO stores(nom) VALUES ('Mercadona');
INSERT INTO stores(nom) VALUES ('Lidl');
INSERT INTO stores(nom) VALUES ('Aldi');
INSERT INTO stores(nom) VALUES ('Condis');

INSERT INTO items(store_id, nom, unitats) VALUES (1, 'Llet', 1);
INSERT INTO items(store_id, nom, unitats) VALUES (2, 'Pa', 20);
INSERT INTO items(store_id, nom, unitats) VALUES (3, 'Ous', 12);
INSERT INTO items(store_id, nom, unitats) VALUES (4, 'Formatge', 5);
INSERT INTO items(store_id, nom, unitats) VALUES (1, 'Iogurt', 4);

-- La contrasenya és patata
INSERT INTO users (email, role, password) VALUES ('ed@test.cat', 'editor', 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');
INSERT INTO users (email, role, password) VALUES ('vi@test.cat', 'viewer', 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');

-- Afegir columnes per a l'autenticació
ALTER TABLE users ADD COLUMN auth_token TEXT DEFAULT NULL;
ALTER TABLE users ADD COLUMN auth_token_expiration TIMESTAMP DEFAULT NULL;
