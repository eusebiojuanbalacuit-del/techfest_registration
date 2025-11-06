print("Welcome to SMIT TechFest!")
print("Event organized by Ej Balacuit of APPDAET <BTCS2>")  # Replace with your actual name and section

num_participants = int(input("How many participants will register? "))
if num_participants <= 0:
    print("Invalid number of participants.")
    exit()  # Stop the program
participants = []  # List to store participant dictionaries
for i in range(num_participants):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participant = {"name": name, "track": track}
    participants.append(participant)

# Display registered participants
print("\nRegistered Participants:")
for idx, p in enumerate(participants, start=1):
    print(f"{idx}. {p['name']} - {p['track']}")
unique_tracks = set(p['track'] for p in participants)
print(f"\nTracks offered in this event: {', '.join(unique_tracks)}")
if len(unique_tracks) < 2:
    print("Not enough variety in tracks.")
