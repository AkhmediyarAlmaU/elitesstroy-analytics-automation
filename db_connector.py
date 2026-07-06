import pandas as pd
import sqlite3
from typing import Optional

def fetch_construction_data(db_path: str) -> Optional[pd.DataFrame]:
    """
    Устанавливает соединение с базой данных и извлекает информацию 
    об одобренных счетах субподрядчиков по строительным объектам.
    """
    query = """
    SELECT 
        project_id,
        project_name,
        SUM(invoice_amount) AS total_spent,
        COUNT(invoice_id) AS invoice_count
    FROM 
        construction_invoices
    WHERE 
        approval_status = 'Approved'
    GROUP BY 
        project_id, project_name;
    """
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None
