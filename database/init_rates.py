# init_rates.py
from database.db_manager import (
    init_rates_table_geely, 
    init_rates_table_haval, 
    init_rates_table_haval_kv,
    init_rates_table_geely_cityray,
    get_connection
)

def fill_rates_geely():
    """Заполняет таблицу ставок Geely"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_geely")
    
    rates_data = [
    (0,  0.01, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0),
    (10, 0.01, 8.20, 10.9, 12.3, 13.1, 13.7, 14.1, 25.0),
    (20, 0.01, 6.70, 9.80, 11.1, 12.1, 13.1, 13.4, 13.9),
    (30, 0.01, 4.70, 8.50, 9.40, 11.0, 12.2, 12.4, 12.9),
    (40, 0.01, 2.00, 6.60, 8.00, 9.70, 11.0, 11.3, 11.9),
    (50, 0.01, 0.01, 4.00, 5.80, 7.30, 8.30, 9.00, 9.60),
    (60, 0.01, 0.01, 0.01, 3.30, 5.10, 5.50, 5.60, 7.00),
    (70, 0.01, 0.01, 0.01, 0.01, 1.00, 1.20, 2.50, 5.00),
    (80, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)    
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_geely (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84, rate96)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()


def fill_rates_geely_cityray():
    """Заполняет таблицу ставок Geely Cityray"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_geely_cityray")
    
    rates_data = [
    (0,   0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01),
    (10,  0.01, 7.60, 10.60, 11.70, 12.60, 13.60, 13.70, 14.10),
    (20,  0.01, 6.00, 9.50, 10.70, 11.80, 12.90, 13.10, 13.50),
    (30,  0.01, 3.90, 8.00, 8.90, 10.70, 11.90, 12.10, 12.50),
    (40,  0.01, 2.50, 6.00, 7.50, 9.30, 10.50, 11.00, 11.70),
    (50,  0.01, 0.01, 3.20, 5.30, 7.00, 8.00, 8.70, 9.30),
    (60,  0.01, 0.01, 0.01, 2.80, 5.00, 5.10, 5.30, 6.00),
    (70,  0.01, 0.01, 0.01, 0.01, 1.00, 1.20, 2.20, 3.10),
    (80,  0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_geely_cityray (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84, rate96)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()    

def fill_rates_haval():
    """Заполняет таблицу ставок Haval без кв"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_haval")
    
    rates_data = [
        (0,   26.0, 26.0, 26.0, 26.0, 26.0, 26.0, 26.0),
        (10,  26.0, 26.0, 26.0, 26.0, 11.3, 12.3, 12.8),
        (20,  26.0, 26.0, 26.0, 26.0, 10.4, 11.3, 11.8),
        (30,  26.0, 26.0, 26.0, 26.0, 9.10, 26.0, 11.0),
        (40,  26.0, 26.0, 26.0, 26.0, 9.10, 26.0, 11.0),
        (50,  26.0, 26.0, 0.01, 4.10, 5.80, 26.0, 8.40),
        (60,  26.0, 26.0, 0.01, 0.01, 2.80, 26.0, 5.70),
        (70,  26.0, 26.0, 0.01, 0.01, 0.01, 0.01, 1.30),
        (80,  26.0, 26.0, 0.01, 0.01, 0.01, 0.01, 1.30),
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates_haval (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()

def fill_rates_haval_kv():
    """Заполняет таблицу ставок Haval с кв"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates_haval_kv")
    
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



if __name__ == "__main__":
    init_rates_table_geely()
    init_rates_table_geely_cityray()
    init_rates_table_haval()
    init_rates_table_haval_kv()
    
    fill_rates_geely()
    fill_rates_geely_cityray()
    fill_rates_haval()
    fill_rates_haval_kv()
    
