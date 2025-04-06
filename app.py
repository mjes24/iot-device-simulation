import time
import random

def send_data_to_server():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(30.0, 50.0), 2)
    print(f"Sending data to server... Temperature: {temperature}°C, Humidity: {humidity}%")

def main():
    print("Starting IoT device simulation...\n")
    while True:
        send_data_to_server()
        time.sleep(5)  # Send data every 5 seconds

if __name__ == "__main__":
    main()
