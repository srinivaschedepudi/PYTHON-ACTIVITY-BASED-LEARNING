"""Case 18: Fuel consumption and route comparison."""

DISTANCE_KM = 180.0
FUEL_PRICE_PER_LITRE = 110.0
RESERVE_PERCENT = 10.0
VEHICLES = [
    ("Car", 15.0, 20.0),
    ("Motorcycle", 40.0, 5.0),
    ("SUV", 10.0, 20.0),
]


def compare_vehicles(distance, fuel_price, reserve_percent, vehicles):
    feasible = []
    print("FUEL AND ROUTE COMPARISON")
    print(f"Distance: {distance:.1f} km; reserve: {reserve_percent:.0f}%")
    for name, mileage, tank_capacity in vehicles:
        if distance <= 0 or mileage <= 0 or tank_capacity < 0:
            print(f"{name}: invalid vehicle or route data")
            continue
        trip_fuel = distance / mileage
        fuel_with_reserve = trip_fuel * (1 + reserve_percent / 100)
        cost = fuel_with_reserve * fuel_price
        if fuel_with_reserve <= tank_capacity:
            feasible.append((name, fuel_with_reserve, cost))
            print(f"{name}: required {fuel_with_reserve:.2f} L, cost ${cost:.2f} (feasible)")
        else:
            print(f"{name}: required {fuel_with_reserve:.2f} L, tank {tank_capacity:.2f} L (not feasible)")
    if feasible:
        best = min(feasible, key=lambda option: option[2])
        print(f"Lowest-cost feasible vehicle: {best[0]} (${best[2]:.2f})")
        return best
    print("No vehicle is feasible for this trip.")
    return None


if __name__ == "__main__":
    compare_vehicles(DISTANCE_KM, FUEL_PRICE_PER_LITRE, RESERVE_PERCENT, VEHICLES)
