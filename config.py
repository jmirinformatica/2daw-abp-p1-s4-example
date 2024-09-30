class Config:

    # clau secreta per a les sessions guardades a les cookies
    SECRET_KEY="Valor aleatori molt llarg i super secret"
    
    # ruta relativa de la base de dades
    SQLITE_FILE_RELATIVE_PATH="sqlite/database.db"
    
    # mostra les sentències SQL generades pel log
    SQLALCHEMY_ECHO="True" 
    
    # nivell de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    LOGGING_LEVEL="WARNING"
