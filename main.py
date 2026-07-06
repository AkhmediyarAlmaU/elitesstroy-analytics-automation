import pandas as pd
from db_connector import fetch_construction_data
from data_processor import process_financial_metrics
from excel_reporter import generate_styled_excel

def run_pipeline():
    # Название базы данных и итогового отчета
    db_file = "elitesstroy_data.db"
    report_file = "weekly_construction_report.xlsx"
    
    print("Запуск автоматического построения отчета...")
    
    # ЭТАП 1: Выгрузка данных через SQL
    raw_data = fetch_construction_data(db_file)
    
    # Если базы данных нет на локальном компьютере, создаем тестовый датасет для демонстрации кода
    if raw_data is None:
        print("Реальная база данных не обнаружена. Генерация демонстрационного пула данных по объектам...")
        mock_data = {
            'project_id': [101, 102, 103],
            'project_name': ['ЖК Eco-Park', 'ЖК Аль-Фараби', 'ЖК Хан-Тенгри'],
            'total_spent': [150000000, 240000000, 85000000],
            'invoice_count': [15, 24, 8]
        }
        raw_data = pd.DataFrame(mock_data)
        
    # ЭТАП 2: Обработка и расчет бизнес-метрик на Python
    processed_data = process_financial_metrics(raw_data)
    
    # ЭТАП 3: Формирование визуального Excel-отчета
    generate_styled_excel(processed_data, report_file)
    
    print("Процесс автоматизации успешно завершен.")

if __name__ == "__main__":
    run_pipeline()
