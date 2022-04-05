# Define your function
def laps_to_miles(user_laps):
    a = user_laps
    x = 0
    if x != a:
        laps_to_miles = a * miles
    return laps_to_miles

miles = 0.25
if __name__ == '__main__':
    print(f'{laps_to_miles(user_laps = float(input())):.2f}')
