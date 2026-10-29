"""Case 51: Bus passenger occupancy simulation."""

CAPACITY = 35
INITIAL_PASSENGERS = 8
# Tuple for each stop: (stop name, passengers boarding, passengers alighting).
STOPS = [
    ("Stop 1", 10, 2),
    ("Stop 2", 15, 3),
    ("Stop 3", 12, 4),
    ("Stop 4", 2, 5),
]


def simulate_bus(capacity, initial_passengers, stops):
    if initial_passengers < 0 or initial_passengers > capacity:
        raise ValueError("Initial passenger count must be within bus capacity.")
    passengers = initial_passengers
    total_refused = 0
    print("BUS PASSENGER OCCUPANCY")
    print(f"Starting passengers: {passengers}/{capacity}")
    for stop_name, boarding, alighting in stops:
        if boarding < 0 or alighting < 0:
            print(f"{stop_name}: invalid negative count; stop ignored")
            continue
        if alighting > passengers:
            print(f"{stop_name}: invalid alighting count; stop ignored")
            continue
        passengers -= alighting
        available_seats = capacity - passengers
        accepted_boarding = min(boarding, available_seats)
        refused = boarding - accepted_boarding
        passengers += accepted_boarding
        total_refused += refused
        print(f"{stop_name}: boarded={accepted_boarding}, alighted={alighting}, occupancy={passengers}/{capacity}")
        if refused > 0:
            print(f"  Capacity reached; {refused} passenger(s) could not board.")
    print(f"Final passengers: {passengers}")
    print(f"Total passengers refused: {total_refused}")
    return passengers, total_refused


if __name__ == "__main__":
    simulate_bus(CAPACITY, INITIAL_PASSENGERS, STOPS)
