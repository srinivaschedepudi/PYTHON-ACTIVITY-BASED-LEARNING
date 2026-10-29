"""Case 53: Food waste monitoring system."""

# Each tuple: (day, meals prepared, meals served).
DAILY_MEALS = [
    ("Monday", 100, 88),
    ("Tuesday", 120, 90),
    ("Wednesday", 80, 70),
]
WASTE_LIMIT_PERCENT = 15.0


def analyze_food_waste(daily_meals, waste_limit_percent):
    total_prepared = 0
    total_served = 0
    excessive_days = []
    print("FOOD WASTE MONITORING")
    for day, prepared, served in daily_meals:
        if prepared <= 0 or served < 0 or served > prepared:
            print(f"{day}: invalid meal counts")
            continue
        leftover = prepared - served
        waste_percent = leftover / prepared * 100
        total_prepared += prepared
        total_served += served
        status = "EXCEEDS LIMIT" if waste_percent > waste_limit_percent else "Within limit"
        if waste_percent > waste_limit_percent:
            excessive_days.append(day)
        print(f"{day}: leftover={leftover}, waste={waste_percent:.2f}% ({status})")
    overall_leftover = total_prepared - total_served
    if total_prepared > 0:
        overall_percent = overall_leftover / total_prepared * 100
    else:
        overall_percent = 0.0
    print(f"Overall prepared: {total_prepared}; served: {total_served}; leftover: {overall_leftover}")
    print(f"Overall waste: {overall_percent:.2f}%")
    print(f"Days exceeding limit: {excessive_days}")
    return overall_percent, excessive_days


if __name__ == "__main__":
    analyze_food_waste(DAILY_MEALS, WASTE_LIMIT_PERCENT)
