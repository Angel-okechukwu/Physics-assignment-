def calculate_force(mass, acceleration):
    """Calculate force using F = m * a."""
    return mass * acceleration


def calculate_energy(mass, speed_of_light=299792458):
    """Calculate energy using E = m * c^2."""
    return mass * speed_of_light ** 2


def calculate_momentum(mass, velocity):
    """Calculate momentum using p = m * v."""
    return mass * velocity


def calculate_work(force, distance):
    """Calculate work using W = F * d."""
    return force * distance


def calculate_power(work, time):
    """Calculate power using P = W / t."""
    return work / time


def main():
    print("Welcome to Physics 101!")
    print("Enter 'a' to calculate force or 'e' to calculate power.")
    user_input = input("Your choice: ").strip().lower()

    if user_input == 'a':
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))
        force = calculate_force(mass, acceleration)
        print(f"The calculated force is {force} N.")

    elif user_input == 'e':
        work = float(input("Enter work done (J): "))
        time = float(input("Enter time taken (s): "))
        power = calculate_power(work, time)
        print(f"The calculated power is {power} W.")

    else:
        print("Invalid input. Please enter 'a' or 'e'.")


if __name__ == "__main__":
    main()
