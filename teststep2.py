import RPi.GPIO as GPIO
import time

# Define GPIO pins for motor control
step_pin = 17
dir_pin = 18

# Set GPIO mode and setup the pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

# Define motor parameters
steps_per_revolution = 200  # Number of steps per full revolution
delay = 0.005  # Delay between steps (adjust as needed for motor speed)

# Function to control the stepper motor
def move_stepper(steps, direction):
    # Set the direction (HIGH or LOW)
    GPIO.output(dir_pin, direction)
    
    # Step the motor
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

# Example usage
try:
    while True:
        # Rotate clockwise for 1 revolution
        move_stepper(steps_per_revolution, GPIO.HIGH)
        time.sleep(1)  # Pause for 1 second
        
        # Rotate counterclockwise for 1 revolution
        move_stepper(steps_per_revolution, GPIO.LOW)
        time.sleep(1)  # Pause for 1 second

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()

