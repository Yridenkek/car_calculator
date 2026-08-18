# database/init_db.py
from database.db_manager import init_db, get_connection

def fill_sample_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Очищаем таблицу перед заполнением
    cursor.execute("DELETE FROM cars")
    
    total_cars = [
        ("Geely", "Monjaro", 2026, "Luxury SE", 4599990, 4379990, 0, 0, 200000, 250000),
        ("Geely", "Monjaro", 2026, "Flagship SE", 4954990, 4587300, 0, 0, 155000, 205000),
        ("Geely", "Atlas", 2026, "Luxury 2WD", 3449990, 3289990, 0, 0, 190000, 0),
        ("Geely", "Okavango", 2026, "Luxury", 3779990, 1, 0, 0, 300000, 350000),
        ("Geely", "Okavango", 2026, "Flagship", 4025990, 3795990, 0, 0, 300000, 350000),
        ("Geely", "Preface", 2026, "Luxury", 3329990, 1, 0, 0, 250000, 0),
        ("Geely", "Preface", 2026, "Flagship", 3434990, 3279990, 0, 0, 170000, 0),
        ("Geely", "Cityray", 2026, "Comfort", 2924990, 2741300, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2026, "Luxury", 3174990, 2991500, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2026, "Flagship", 3314990, 3121600, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2026, "Sport", 3354990, 3161600, 0, 0, 230000, 270000),
        ("Geely", "Coolray", 2026, "Exclusive", 2944990, 2764500, 0, 0, 150000, 0),
        ("Geely", "EX5 EM-R", 2026, "Pro", 3464990, 1, 0, 0, 250000, 0),        
        ("Geely", "EX5 EM-R", 2026, "Max", 3814990, 1, 0, 0, 250000, 0),        
        ("Geely", "EX5 EM-i", 2026, "Max", 3974990, 3759800, 50000, 0, 0, 250000),        
        ("Haval", "Poer", 2026, "Optimum 2.0T", 3699000, 1, 0, 0, 0, 0),
        ("Haval", "Poer", 2026, "Premium 2.0T", 3899000, 3665060, 0, 0, 0, 0),
        ("Haval", "Poer", 2026, "Premium 2.4D", 3999000, 3759060, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Elite 1,5T 2WD", 2899000, 2725060, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Premium 1,5T 2WD", 3099000, 2913060, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Elite 2.0T 4WD", 3299000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Premium 2.0T 4WD", 3499000, 3289060, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Tech plus 2.0T 4WD", 3699000, 3477060, 0, 0, 0, 0),
        ("Haval", "F7x", 2026, "Premium", 3599000, 1, 0, 0, 0, 0),
        ("Haval", "F7x", 2026, "Tech plus", 3799000, 3571060, 0, 0, 0, 0),        
        ("Haval", "M6", 2026, "Family MT", 2049000, 1946550, 0, 0, 0, 0),
        ("Haval", "M6", 2026, "Family AT", 2299000, 2184050, 0, 0, 0, 0),
        ("Haval", "M6 MY26", 2026, "Family MT", 2049000, 1946550, 0, 0, 0, 0),
        ("Haval", "M6 MY26", 2026, "Family AT", 2349000, 2231550, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Comfort", 3199000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Elite", 3399000, 3195060, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Premium", 3599000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Tech plus", 3749000, 3524060, 0, 0, 0, 0),
        ("Haval", "Dargo X", 2026, "Elite", 3499000, 3289060, 0, 0, 0, 0),
        ("Haval", "Dargo X", 2026, "Premium", 3699000, 3477060, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Comfort 2WD", 2049000, 1946550, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Elite 2WD", 2449000, 2302060, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Premium 2WD", 2649000, 2490060, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Elite 4WD", 2599000, 2443060, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Premium 4WD", 2799000, 2631060, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Tech plus 4WD", 2899000, 2725060, 0, 0, 0, 0),
                                

    ]
    
    cursor.executemany("INSERT INTO cars (brand, model, year, trim, retailprice, price, pryamaya, finance, tradein, loyaltradein) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", total_cars)
    conn.commit()
    print(f"Добавлено {len(total_cars)} автомобилей")
    
    conn.close()

if __name__ == "__main__":
    init_db()
    fill_sample_data()
    print("База данных инициализирована")