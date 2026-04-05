import streamlit as st

calc_internal = st.Page("pages/calc_internal.py", title="Калькулятор КМ", icon="🔧")
calc_client = st.Page("pages/calc_client.py", title="Кредитный калькулятор", icon="👥")
warehouse = st.Page("pages/warehouse.py", title="Склад", icon="📦")
issued = st.Page("pages/issued.py", title="Выданные авто", icon="🚗")
price = st.Page("pages/price.py", title="Прайсы", icon="📦")


pg = st.navigation([calc_internal, calc_client, warehouse, issued, price])
pg.run()