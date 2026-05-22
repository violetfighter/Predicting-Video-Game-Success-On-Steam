import joblib
import pandas as pd

print("\n   Game Success Predictor")
print("-" * 30)

# Platform input
while True:
    print("\nPlatform: \nOptions: windows, mac, linux")
    print("(You can enter multiple platforms separated by commas)")
    platform = input("Enter Platform: ").strip().lower().replace(',', ';').replace(', ', ';')
    valid = all(i.strip() in ['windows', 'mac', 'linux'] for i in platform.split(';'))
    if not valid:
        print("Invalid input. Please enter a valid platform.")
        continue
    break

# Genre input
genre_map = {
    1: 'Action', 2: 'Adventure', 3: 'RPG', 4: 'Strategy',
    5: 'Indie', 6: 'Casual', 7: 'Simulation', 8: 'Racing',
    9: 'Sports', 10: 'Free to Play', 11: 'Massively Multiplayer',
    12: 'Animation & Modeling', 13: 'Video Production'
}

print("\nGenre Options:")
for k, v in genre_map.items():
    print(f"  {k}. {v}")
print("(You can enter multiple genres separated by commas)")

while True:
    try:
        genre_input = input("Choose Genre: ").strip()
        genre_nums = [int(i.strip()) for i in genre_input.split(',')]
        if not all(1 <= n <= 13 for n in genre_nums):
            print("Invalid input. Please enter valid genre numbers.")
            continue
        genre = ';'.join(genre_map[n] for n in genre_nums)
        break
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

# Category input
category_map = {
    1: 'Single-player', 2: 'Multi-player', 3: 'Online Multi-Player',
    4: 'Local Multi-Player', 5: 'Co-op', 6: 'Online Co-op',
    7: 'Cross-Platform Multiplayer', 8: 'Steam Trading Cards',
    9: 'Steam Cloud', 10: 'Steam Workshop', 11: 'Steam Leaderboards',
    12: 'SteamVR Collectibles', 13: 'Valve Anti-Cheat enabled',
    14: 'Stats', 15: 'Full controller support',
    16: 'Partial Controller Support', 17: 'Captions available',
    18: 'Includes Source SDK', 19: 'Includes level editor',
    20: 'Commentary available', 21: 'In-App Purchases',
    22: 'Steam Achievements'
}

print("\nCategory Options:")
for k, v in category_map.items():
    print(f"  {k}. {v}")
print("(You can enter multiple categories separated by commas)")

while True:
    try:
        category_input = input("Choose Category: ").strip()
        category_nums = [int(i.strip()) for i in category_input.split(',')]
        if not all(1 <= n <= 22 for n in category_nums):
            print("Invalid input. Please enter valid category numbers.")
            continue
        category = ';'.join(category_map[n] for n in category_nums)
        break
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

# Tags input
tag_map = {
    1: 'Action', 2: 'FPS', 3: 'Multiplayer', 4: 'Sci-fi',
    5: 'Classic', 6: 'Singleplayer', 7: 'Indie', 8: 'RPG',
    9: 'Horror', 10: 'Strategy', 11: 'Casual', 12: 'Adventure',
    13: 'World War II', 14: 'Open World', 15: 'Simulation',
    16: 'Puzzle', 17: 'First-Person', 18: 'Free to Play',
    19: 'MOBA', 20: 'Fighting', 21: 'Co-op', 22: 'Zombies',
    23: 'Cyberpunk', 24: 'RTS', 25: 'Hacking', 26: 'Naval',
    27: '4X', 28: 'Turn-Based Strategy', 29: 'Fantasy',
    30: 'Tanks', 31: 'Space', 32: 'Shooter', 33: 'Racing',
    34: 'Sports', 35: 'Platformer', 36: 'Stealth',
    37: 'Survival', 38: 'Tower Defense'
}

print("\nTag Options:")
for k, v in tag_map.items():
    print(f"  {k}. {v}")
print("(You can enter multiple tags separated by commas)")

while True:
    try:
        tag_input = input("Choose Tags: ").strip()
        tag_nums = [int(i.strip()) for i in tag_input.split(',')]
        if not all(1 <= n <= 38 for n in tag_nums):
            print("Invalid input. Please enter valid tag numbers.")
            continue
        tags = ';'.join(tag_map[n] for n in tag_nums)
        break
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

# Price input
while True:
    try:
        price = float(input("\nEnter Price in dollars (USD): "))
        if price < 0:
            print("Invalid input. Please enter a valid price.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Achievements input
while True:
    try:
        achievements = int(input("Enter Number of Achievements: "))
        if achievements < 0:
            print("Invalid input. Please enter a valid number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

#release year input
while True:
    try:
        date_year = int(input("Enter Release Year: "))
        if date_year < 1970 or date_year > 2100:
            print("Invalid year.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
# Model selection and prediction loop
q = 'y'
while q == 'y':
    while True:
        try:
            print("\nSelect Model:")
            print("1. Logistic Regression")
            print("2. Random Forest")
            print("3. SVM")
            model_choice = int(input("Enter choice (1, 2, or 3): "))
            if model_choice not in [1, 2, 3]:
                print("Please enter 1, 2, or 3!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    if model_choice == 1:
        model = joblib.load('model_lr.pkl')
        model_name = "Logistic Regression"
    elif model_choice == 2:
        model = joblib.load('model_rf.pkl')
        model_name = "Random Forest"
    elif model_choice == 3:
        model = joblib.load('model_svm.pkl')
        model_name = "SVM"

    input_data = pd.DataFrame([[price, achievements, platform, genre, category, tags, date_year]],
        columns=['price', 'achievements', 'platforms', 'genres', 'categories', 'steamspy_tags', 'date_year'])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    success_rate = probability[1] * 100
    fail_rate = probability[0] * 100

    print("\n" + "-" * 30)
    print(f"Model Used: {model_name}")
    print(f"Success Rate: {success_rate:.1f}%")
    print(f"Fail Rate: {fail_rate:.1f}%")

    if success_rate >= 70:
        print("Result: SUCCESSFUL!")
    else:
        print("Result: NOT SUCCESSFUL")
    print("-" * 30)

    while True:
        q = input("\nDo you want to try another model? (y/n): ").lower()
        if q in ['y', 'n']:
            break
        print("Please enter y or n!")

print("\nThank you for using Game Success Predictor!")