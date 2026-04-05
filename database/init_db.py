# database/init_db.py
from database.db_manager import init_db, get_connection

def fill_sample_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Очищаем таблицу перед заполнением
    cursor.execute("DELETE FROM cars")
    
    total_cars = [
        ("Geely", "Monjaro", 2025, "Flagship SE", 4899990, 4579990,40000, 0, 200000, 250000),
        ("Geely", "Monjaro", 2026, "Luxury SE", 4379990, 4579990, 0, 0, 200000, 250000),
        ("Geely", "Monjaro", 2026, "Flagship SE", 4899990, 4579990, 0, 0, 0, 0),
        ("Geely", "Atlas", 2025, "Luxury 2WD", 3449990, 3289990, 0, 0, 260000, 0),
        ("Geely", "Atlas", 2025, "Luxury", 3760990, 1, 0, 0, 150000, 0),
        ("Geely", "Atlas", 2025, "Flagship", 3970990, 3800990, 0, 0, 150000, 0),
        ("Geely", "Atlas", 2025, "Sport", 4080990, 3910990, 0, 0, 150000, 0),
        ("Geely", "Atlas", 2026, "Luxury 2WD", 3449990, 3289990, 0, 0, 260000, 0),
        ("Geely", "Atlas", 2026, "Luxury", 3904990, 1, 0, 0, 160000, 0),
        ("Geely", "Atlas", 2026, "Flagship", 4114990, 1, 0, 0, 160000, 0),
        ("Geely", "Atlas", 2026, "Sport", 4224990, 1, 0, 0, 160000, 0),
        ("Geely", "Okavango", 2025, "Flagship MY24", 3908990, 3692190, 0, 0, 300000, 350000),
        ("Geely", "Preface", 2025, "Luxury", 3329990, 1, 0, 0, 250000, 0),
        ("Geely", "Preface", 2025, "Flagship", 3429990, 1, 0, 0, 250000, 0),
        ("Geely", "Cityray", 2025, "Comfort", 2849990, 2739990, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2025, "Luxury", 3094990, 2964990, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2025, "Flagship", 3214990, 3074990, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2025, "Sport", 3254990, 3114990, 0, 0, 230000, 270000),
        ("Knewstar", "001", 2024, "Sport", 4569990, 4242990, 320000, 0, 0, 300000),
        ("Knewstar", "001", 2025, "Sport", 4569990, 4242990, 120000, 0, 0, 300000),
                

    ]
    
    cursor.executemany("INSERT INTO cars (brand, model, year, trim, retailprice, price, pryamaya, finance, tradein, loyaltradein) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", total_cars)
    conn.commit()
    print(f"Добавлено {len(total_cars)} автомобилей")
    
    conn.close()

if __name__ == "__main__":
    init_db()
    fill_sample_data()
    print("База данных инициализирована")