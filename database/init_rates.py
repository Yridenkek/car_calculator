# init_rates.py
from database.db_manager import init_rates_table, get_connection

def fill_rates():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM credit_rates")
    
    rates_data = [
        (0,   0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 18.0),
        (10,  0.01, 12.1, 14.2, 15.5, 15.7, 16.1, 17.7, 18.0),
        (20,  0.01, 4.50, 8.10, 9.10, 10.7, 12.1, 12.2, 13.1),
        (30,  0.01, 2.00, 6.40, 7.40, 9.30, 11.1, 11.2, 12.4),
        (40,  0.01, 0.50, 3.90, 5.60, 7.80, 9.90, 9.80, 11.0),
        (50,  0.01, 0.01, 2.00, 3.00, 6.10, 8.40, 8.30, 9.40),
        (60,  0.01, 0.01, 0.01, 0.01, 3.00, 5.00, 6.20, 8.50),
        (70,  0.01, 0.01, 0.01, 0.01, 0.01, 1.00, 2.40, 4.50),
        (80,  0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01),
    ]
    
    for data in rates_data:
        cursor.execute("""
            INSERT INTO credit_rates (pervak, rate12, rate24, rate36, rate48, rate60, rate72, rate84, rate96)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()
    print(f"✅ Добавлено {len(rates_data)} строк ставок")

if __name__ == "__main__":
    init_rates_table()
    fill_rates()
    print("✅ Таблица кредитных ставок инициализирована")