import time
import random

class HomeProtectionSystem:
    def __init__(self):
        self.motion_detected = False
        self.smoke_detected = False
        self.door_open = False
        self.alarm_triggered = False

    def check_motion_sensor(self):
        # Simulated sensor (True = motion)
        self.motion_detected = random.choice([True, False])
        if self.motion_detected:
            print("[Motion Sensor] Movement detected!")
            self.trigger_alarm("Intruder alert!")

    def check_smoke_sensor(self):
        # Simulated sensor (True = smoke/fire)
        self.smoke_detected = random.choice([True, False])
        if self.smoke_detected:
            print("[Smoke Sensor] Smoke or fire detected!")
            self.trigger_alarm("Fire alert!")

    def check_door_sensor(self):
        # Simulated sensor (True = door open)
        self.door_open = random.choice([True, False])
        if self.door_open:
            print("[Door Sensor] Door opened!")
            # You can add logic to ignore authorized access
            self.trigger_alarm("Unauthorized door entry!")

    def trigger_alarm(self, message):
        if not self.alarm_triggered:
            self.alarm_triggered = True
            print(f"[ALARM] {message}")
            self.send_emergency_notification(message)

    def send_emergency_notification(self, message):
        # Simulated alert (could be email, SMS, etc.)
        print(f"[NOTIFICATION] Sending emergency alert: {message}")

    def reset_system(self):
        print("[System] Resetting system status...")
        self.motion_detected = False
        self.smoke_detected = False
        self.door_open = False
        self.alarm_triggered = False

    def run(self, cycles=5):
        print("Home Protection System Active...\n")
        for i in range(cycles):
            print(f"--- Cycle {i+1} ---")
            self.check_motion_sensor()
            self.check_smoke_sensor()
            self.check_door_sensor()
            print()
            time.sleep(2)
