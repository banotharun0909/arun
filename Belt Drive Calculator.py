
import math

def calculate_velocity(diameter, rpm):
    """v = (pi * d * N) / 60"""
    return (math.pi * diameter * rpm) / 60

def calculate_power(t1, t2, velocity):
    """P = (T1 - T2) * v"""
    return (t1 - t2) * velocity

def calculate_tension_ratio(t1, t2):
    """Ratio = T1 / T2"""
    return t1 / t2 if t2 != 0 else 0

def calculate_torque(t1, t2, diameter):
    """Torque = (T1 - T2) * radius"""
    return (t1 - t2) * (diameter / 2)

def main():
    while True:
        print("\n--- Belt Drive Calculator ---")
        print("1. Belt Velocity")
        print("2. Power Transmitted")
        print("3. Tension Ratio")
        print("4. Torque Transmitted")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice == '1':
            d = float(input("Enter pulley diameter (m): "))
            n = float(input("Enter rotational speed (RPM): "))
            print(f"Belt Velocity: {calculate_velocity(d, n):.2f} m/s")
            
        elif choice == '2':
            t1 = float(input("Enter tight side tension T1 (N): "))
            t2 = float(input("Enter slack side tension T2 (N): "))
            v = float(input("Enter belt velocity (m/s): "))
            print(f"Power Transmitted: {calculate_power(t1, t2, v):.2f} W")
            
        elif choice == '3':
            t1 = float(input("Enter tight side tension T1 (N): "))
            t2 = float(input("Enter slack side tension T2 (N): "))
            print(f"Tension Ratio (T1/T2): {calculate_tension_ratio(t1, t2):.2f}")
            
        elif choice == '4':
            t1 = float(input("Enter tight side tension T1 (N): "))
            t2 = float(input("Enter slack side tension T2 (N): "))
            d = float(input("Enter pulley diameter (m): "))
            print(f"Torque Transmitted: {calculate_torque(t1, t2, d):.2f} Nm")
            
        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()
