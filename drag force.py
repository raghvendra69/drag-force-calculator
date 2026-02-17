def calculate_drag_force(rho, velocity, drag_coefficient, area):
    """
    Calculate drag force using:
    Fd = 0.5 * rho * v^2 * Cd * A
    """
    return 0.5 * rho * (velocity ** 2) * drag_coefficient * area


def main():
    print("=== Drag Force Calculator ===")

    try:
        rho = float(input("Enter air density (kg/m^3): "))
        velocity = float(input("Enter velocity (m/s): "))
        cd = float(input("Enter drag coefficient (Cd): "))
        area = float(input("Enter cross-sectional area (m^2): "))

        drag_force = calculate_drag_force(rho, velocity, cd, area)

        print(f"\nDrag Force: {drag_force:.3f} N")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
