import pandas as pd

def process_financial_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Выполняет очистку данных и рассчитывает аналитические показатели:
    гарантийные удержания, чистые выплаты и средний чек счета.
    """
    if df is None or df.empty:
        raise ValueError("Входной датафрейм пуст или не существует.")
        
    # Заполнение пропущенных значений, если они есть
    df['total_spent'] = df['total_spent'].fillna(0)
    df['invoice_count'] = df['invoice_count'].fillna(0)
    
    # Расчет гарантийного удержания (10% от суммы для контроля качества работ субподрядчика)
    df['retention_money_10_percent'] = df['total_spent'] * 0.10
    
    # Расчет суммы к фактической выплате
    df['final_payout'] = df['total_spent'] - df['retention_money_10_percent']
    
    # Расчет среднего чека по одобренным счетам для каждого объекта
    df['average_invoice_value'] = df.apply(
        lambda row: row['total_spent'] / row['invoice_count'] if row['invoice_count'] > 0 else 0, 
        axis=1
    )
    
    # Округление финансовых показателей до двух знаков после запятой
    df = df.round({'retention_money_10_percent': 2, 'final_payout': 2, 'average_invoice_value': 2})
    
    return df
