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
        ("Geely", "Okavango", 2024, "Flagship", 3847190, 3692190, 150000, 0, 300000, 350000),
        ("Geely", "Preface", 2025, "Luxury", 3329990, 1, 0, 0, 250000, 0),
        ("Geely", "Preface", 2025, "Flagship", 3429990, 1, 0, 0, 250000, 0),
        ("Geely", "Cityray", 2025, "Comfort", 2849990, 2739990, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2025, "Luxury", 3094990, 2964990, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2025, "Flagship", 3214990, 3074990, 0, 0, 230000, 270000),
        ("Geely", "Cityray", 2025, "Sport", 3254990, 3114990, 0, 0, 230000, 270000),
        ("Knewstar", "001", 2024, "Sport", 4569990, 4242990, 320000, 0, 0, 300000),
        ("Knewstar", "001", 2025, "Sport", 4569990, 4242990, 120000, 0, 0, 300000),
        ("Haval", "Poer", 2025, "Optimum 2.0T", 3699000, 1, 100000, 0, 0, 0),
        ("Haval", "Poer", 2025, "Premium 2.0T", 3899000, 1, 0, 0, 0, 0),
        ("Haval", "Poer", 2025, "Premium 2.4D", 3999000, 1, 0, 0, 0, 0),
        ("Haval", "Poer", 2026, "Optimum 2.0T", 3699000, 1, 0, 0, 0, 0),
        ("Haval", "Poer", 2026, "Premium 2.0T", 3899000, 1, 0, 0, 0, 0),
        ("Haval", "Poer", 2026, "Premium 2.4D", 3999000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2025, "Elite 1,5T 2WD", 2849000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2025, "Premium 1,5T 2WD", 3049000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2025, "Elite 2.0T 4WD", 3249000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2025, "Premium 2.0T 4WD", 3449000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2025, "Tech plus 2.0T 4WD", 3649000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Elite 1,5T 2WD", 2899000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Premium 1,5T 2WD", 3099000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Elite 2.0T 4WD", 3299000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Premium 2.0T 4WD", 3499000, 1, 0, 0, 0, 0),
        ("Haval", "F7", 2026, "Tech plus 2.0T 4WD", 3699000, 1, 0, 0, 0, 0),
        ("Haval", "F7x", 2025, "Premium", 3549000, 1, 0, 0, 0, 0),
        ("Haval", "F7x", 2025, "Tech plus", 3749000, 1, 0, 0, 0, 0),
        ("Haval", "F7x", 2026, "Premium", 3599000, 1, 0, 0, 0, 0),
        ("Haval", "F7x", 2026, "Tech plus", 3799000, 1, 0, 0, 0, 0),        
        ("Haval", "M6", 2025, "Family MT", 1999000, 1, 0, 0, 0, 0),
        ("Haval", "M6", 2025, "Family AT", 2249000, 1, 0, 0, 0, 0),
        ("Haval", "M6", 2026, "Family MT", 2049000, 1, 0, 0, 0, 0),
        ("Haval", "M6", 2026, "Family AT", 2299000, 1, 0, 0, 0, 0),
        ("Haval", "M6 MY26", 2026, "Family MT", 2049000, 1, 0, 0, 0, 0),
        ("Haval", "M6 MY26", 2026, "Family AT", 2349000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2025, "Comfort", 3149000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2025, "Elite", 3349000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2025, "Premium", 3549000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2025, "Tech plus", 3699000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Comfort", 3199000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Elite", 3399000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Premium", 3599000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo", 2026, "Tech plus", 3749000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo X", 2025, "Elite", 3449000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo X", 2025, "Premium", 3649000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo X", 2026, "Elite", 3499000, 1, 0, 0, 0, 0),
        ("Haval", "Dargo X", 2026, "Premium", 3699000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2025, "Comfort 2WD", 1999000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2025, "Elite 2WD", 2399000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2025, "Premium 2WD", 2599000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2025, "Elite 4WD", 2549000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2025, "Premium 4WD", 2749000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2025, "Tech plus 4WD", 2849000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2026, "Comfort 2WD", 1999000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2026, "Elite 2WD", 2449000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2026, "Premium 2WD", 2649000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2026, "Elite 4WD", 2599000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2026, "Premium 4WD", 2799000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY24", 2026, "Tech plus 4WD", 2899000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Comfort 2WD", 2049000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Elite 2WD", 2449000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Premium 2WD", 2649000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Elite 4WD", 2599000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Premium 4WD", 2799000, 1, 0, 0, 0, 0),
        ("Haval", "Jolion MY26", 2026, "Tech plus 4WD", 2899000, 1, 0, 0, 0, 0),
                                

    ]
    
    cursor.executemany("INSERT INTO cars (brand, model, year, trim, retailprice, price, pryamaya, finance, tradein, loyaltradein) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", total_cars)
    conn.commit()
    print(f"Добавлено {len(total_cars)} автомобилей")
    
    conn.close()

if __name__ == "__main__":
    init_db()
    fill_sample_data()
    print("База данных инициализирована")