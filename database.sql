CREATE TABLE stores (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nom TEXT NOT NULL
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    store_id INTEGER NOT NULL, 
    nom TEXT NOT NULL, 
    unitats INTEGER NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores(id)
);

INSERT INTO stores(nom) VALUES ("Mercadona");
INSERT INTO stores(nom) VALUES ("Lidl");
INSERT INTO stores(nom) VALUES ("Aldi");
INSERT INTO stores(nom) VALUES ("Condis");

CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL);
INSERT INTO users (email, password) VALUES ('pepe@pepe.com', 'pepe123');
