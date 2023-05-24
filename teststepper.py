import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode and define pin numbers
GPIO.setmode(GPIO.BCM)
step_pin = 17
dir_pin = 18
enable_pin = 27

# Set GPIO pin modes
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)

# Set initial motor state
GPIO.output(enable_pin, GPIO.LOW)  # Enable the motor

# Define motor parameters
steps_per_rev = 200  # Number of steps per revolution (depends on your motor)
delay = 0.001  # Delay between steps (adjust as needed for motor speed)

# Function to move the stepper motor
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
        move_stepper(steps_per_rev, GPIO.HIGH)
        time.sleep(1)  # Pause for 1 second
        
        # Rotate counterclockwise for 1 revolution
        move_stepper(steps_per_rev, GPIO.LOW)
        time.sleep(1)  # Pause for 1 second

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.output(enable_pin, GPIO.HIGH)  # Disable the motor
    GPIO.cleanup()
