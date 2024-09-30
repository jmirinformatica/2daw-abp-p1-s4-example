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

INSERT INTO items(store_id, nom, unitats) VALUES (1, "Llet", 1);
INSERT INTO items(store_id, nom, unitats) VALUES (2, "Pa", 20);
INSERT INTO items(store_id, nom, unitats) VALUES (3, "Ous", 12);
INSERT INTO items(store_id, nom, unitats) VALUES (4, "Formatge", 5);
INSERT INTO items(store_id, nom, unitats) VALUES (1, "Iogurt", 4);