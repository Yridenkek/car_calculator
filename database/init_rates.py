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
        (0,   0.01, 11.0, 15.0, 15.6, 16.0, 16.5, 16.5, 25.0),
        (10,  0.01, 11.0, 15.0, 15.6, 16.0, 16.5, 16.5, 25.0),
        (20,  0.01, 6.50, 9.20, 10.2, 11.5, 12.9, 12.8, 12.8),
        (30,  0.01, 4.00, 7.50, 8.50, 10.3, 11.2, 11.7, 11.7),
        (40,  0.01, 2.00, 6.00, 7.00, 9.00, 10.2, 10.8, 10.8),
        (50,  0.01, 0.01, 3.90, 4.70, 7.50, 8.80, 9.30, 9.60),
        (60,  0.01, 0.01, 0.90, 2.00, 4.80, 6.40, 7.20, 8.10),
        (70,  0.01, 0.01, 0.01, 0.01, 1.50, 3.00, 4.50, 4.80),
        (80,  0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 1.00, 2.10),
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_geely (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84, rate96)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()

def fill_rates_haval():
    """Заполняет таблицу ставок Haval"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_haval")
    
    rates_data = [
        (0,   25.0, 25.1, 25.2, 25.5, 25.7, 26.1, 26.7),
        (10,  4.00, 11.5, 12.0, 13.5, 13.4, 14.0, 14.0),
        (20,  3.00, 10.2, 11.5, 12.5, 12.6, 13.3, 13.3),
        (30,  0.01, 7.80, 10.5, 11.5, 11.7, 12.5, 12.5),
        (40,  0.01, 4.50, 8.50, 10.0, 10.5, 11.7, 11.8),
        (50,  0.01, 2.00, 5.50, 8.00, 9.00, 9.80, 10.4),
        (60,  0.01, 0.01, 1.50, 4.40, 6.00, 7.20, 8.00),
        (70,  0.01, 0.01, 0.01, 1.00, 2.50, 4.10, 5.10),
        (80,  0.01, 0.01, 0.01, 1.00, 2.50, 4.10, 5.10),
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
        (0,   0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 18.0, 18.5, 19.0),
        (10,  0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 18.0, 18.5, 19.0),
        (20,  0.01, 10.0, 12.3, 13.1, 13.1, 13.1, 14.1, 15.0, 16.4, 16.6),
        (30,  0.01, 8.30, 10.7, 12.3, 12.3, 12.4, 13.2, 14.3, 15.9, 16.5),
        (40,  0.01, 6.10, 9.20, 10.9, 11.0, 11.3, 12.3, 13.4, 15.1, 15.8),
        (50,  0.01, 4.00, 7.40, 9.60, 10.2, 10.5, 11.3, 12.6, 14.3, 14.9),
        (60,  0.01, 0.50, 4.80, 8.20, 8.50, 9.20, 10.0, 11.0, 12.9, 13.7),
        (70,  0.01, 0.01, 0.01, 4.50, 5.00, 6.50, 7.50, 8.50, 10.8, 11.3),
        (80,  0.01, 0.01, 0.01, 0.01, 2.60, 4.50, 5.00, 6.50, 7.50, 8.50),
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_knewstar (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84, rate96, rate108, rate120)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
    
