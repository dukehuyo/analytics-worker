# utils.py

import logging
from analytics_worker.config import Config
from analytics_worker.exceptions import AnalyticsException
from analytics_worker.models import DataRecord
from typing import List

def validate_data_record(record: DataRecord) -> None:
    """Validates a DataRecord instance."""
    required_fields = ['identifier', 'timestamp', 'value']
    for field in required_fields:
        if not hasattr(record, field) or not getattr(record, field):
            raise AnalyticsException(f"Missing required field '{field}'")

def calculate_average(data: List[DataRecord]) -> float:
    """Calculates the average value of a list of DataRecord instances."""
    if not data:
        return 0.0
    return sum(record.value for record in data) / len(data)

def get_config() -> Config:
    """Returns the application configuration."""
    return Config()