import csv
from datetime import datetime

THRESHOLD = 80.0

def read_sensor_data(file_path):
    """Reads equipment sensor data from CSV file"""
    readings = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            readings.append({
                "time": row["timestamp"],
                "value": float(row["temperature"])
            })
    return readings

def check_condition(readings):
    """Checks sensor values against threshold and generates alerts"""
    alerts = []
    for data in readings:
        if data["value"] > THRESHOLD:
            alerts.append(
                f"ALERT | Time: {data['time']} | Value: {data['value']} exceeded threshold"
            )
    return alerts

def log_status(message):
    """Logs system messages"""
    print(f"{datetime.now()} - {message}")

if __name__ == "__main__":
    log_status("Equipment monitoring started")

    sensor_data = read_sensor_data("equipment_data.csv")
    alerts = check_condition(sensor_data)

    if alerts:
        for alert in alerts:
            log_status(alert)
    else:
        log_status("All equipment values are within safe limits")
