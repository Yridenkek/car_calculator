# init_rates.py
from database.db_manager import (
    init_rates_table_geely, 
    init_rates_table_haval, 
    init_rates_table_knewstar,
    get_connection
)

def fill_rates_geely():
    """Заполняет таблицу ставок Geely"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_geely")
    
    rates_data = [
        (0,   0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 18.0, 18.5, 19.0),
        (10,  0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 18.0, 18.5, 19.0),
        (20,  0.01, 6.50, 9.20, 10.2, 11.5, 12.9, 13.0, 13.8, 14.9, 15.1),
        (30,  0.01, 4.00, 7.50, 8.50, 10.3, 11.9, 12.0, 13.1, 14.2, 14.5),
        (40,  0.01, 2.00, 6.00, 7.00, 9.00, 10.6, 10.7, 11.9, 13.4, 13.7),
        (50,  0.01, 0.01, 3.90, 4.70, 7.50, 9.20, 9.30, 10.4, 12.2, 13.2),
        (60,  0.01, 0.01, 1.00, 2.00, 4.90, 6.50, 7.20, 9.50, 10.5, 11.0),
        (70,  0.01, 0.01, 0.01, 0.01, 1.50, 3.00, 4.50, 6.90, 7.70, 8.40),
        (80,  0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 1.80, 3.10, 4.20, 5.60),
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_geely (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84, rate96, rate108, rate120)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()

def fill_rates_haval():
    """Заполняет таблицу ставок Haval"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_haval")
    
    rates_data = [
        (0,   0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7),
        (10,  0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7),
        (20,  0.01, 4.50, 8.10, 9.10, 10.7, 12.1, 12.2),
        (30,  0.01, 2.00, 6.40, 7.40, 9.30, 11.1, 11.2),
        (40,  0.01, 0.50, 3.90, 5.60, 7.80, 9.90, 9.80),
        (50,  0.01, 0.01, 2.00, 3.00, 6.10, 8.40, 8.30),
        (60,  0.01, 0.01, 0.01, 0.01, 3.00, 5.00, 6.20),
        (70,  0.01, 0.01, 0.01, 0.01, 0.01, 1.00, 2.40),
        (80,  0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01),
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_haval (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()

def fill_rates_knewstar():
    """Заполняет таблицу ставок Knewstar"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_knewstar")
    
    rates_data = [
        (0,   0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 17.7),
        (10,  0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 17.7),
        (20,  0.01, 4.50, 8.10, 9.10, 10.7, 12.1, 12.2, 17.7),
        (30,  0.01, 2.00, 6.40, 7.40, 9.30, 11.1, 11.2, 17.7),
        (40,  0.01, 0.50, 3.90, 5.60, 7.80, 9.90, 9.80, 17.7),
        (50,  0.01, 0.01, 2.00, 3.00, 6.10, 8.40, 8.30, 17.7),
        (60,  0.01, 0.01, 0.01, 0.01, 3.00, 5.00, 6.20, 17.7),
        (70,  0.01, 0.01, 0.01, 0.01, 0.01, 1.00, 2.40, 17.7),
        (80,  0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 17.7),
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_knewstar (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84, rate96)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_rates_table_geely()
    init_rates_table_haval()
    init_rates_table_knewstar()
    
    fill_rates_geely()
    fill_rates_haval()
    fill_rates_knewstar()
    
