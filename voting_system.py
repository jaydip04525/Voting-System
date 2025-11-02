# ==============================================
# 🇮🇳 Indian Voting System (Beginner + JSON)
# ✅ Allows duplicate names but unique 10-digit Voter IDs only
# ==============================================

import json
import os

DATA_FILE = "voting_data.json"

# ---------- Load & Save Data ----------
def load_data():
    """Load data from JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        # Default structure
        return {"candidates": [], "votes": {}, "voters": [], "voted": []}

def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Admin Functions ----------
def add_candidates(data):
    n = int(input("Enter number of candidates: "))
    for i in range(n):
        name = input(f"Enter candidate {i+1} name: ").strip()
        if name in data["candidates"]:
            print("⚠️ Candidate already exists, skipping.")
        else:
            data["candidates"].append(name)
            data["votes"][name] = 0
    save_data(data)
    print("\n✅ Candidates added successfully!\n")

def add_voters(data):
    n = int(input("Enter number of voters to register: "))
    for i in range(n):
        while True:
            voter_id = input(f"Enter Voter ID for voter {i+1} (must be at least 10 digits): ").strip()
            name = input(f"Enter Name for voter {i+1}: ").strip()

            # ✅ Check: ID must be digits only and 10+ length
            if not voter_id.isdigit() or len(voter_id) < 10:
                print("❌ Invalid ID. Must contain only digits and be at least 10 digits long.")
                continue

            # ✅ Check: ID already used
            id_exists = any(v["id"] == voter_id for v in data["voters"])
            if id_exists:
                print("⚠️ This Voter ID is already registered! Please use a unique ID.")
                continue

            # ✅ All good — add voter (name can be duplicate)
            data["voters"].append({"id": voter_id, "name": name})
            print(f"✅ Voter '{name}' (ID: {voter_id}) added successfully!\n")
            break

    save_data(data)
    print("🎉 All voters added successfully!\n")

def show_candidates(data):
    """Anyone can view candidate names."""
    if not data["candidates"]:
        print("⚠️ No candidates added yet.")
        return
    print("\n--- List of Candidates ---")
    for i, name in enumerate(data["candidates"], start=1):
        print(f"{i}. {name}")
    print("---------------------------\n")

def show_voter_list(data):
    """Only admin can view voter list."""
    if not data["voters"]:
        print("⚠️ No voters registered yet.")
        return
    print("\n--- Registered Voters (Admin Only) ---")
    for v in data["voters"]:
        print(f"🧾 ID: {v['id']} | Name: {v['name']}")
    print("--------------------------------------\n")

def show_results(data):
    if not data["votes"]:
        print("⚠️ No votes recorded yet.\n")
        return
    print("\n======= Election Results =======")
    for name, count in data["votes"].items():
        print(f"{name}: {count} votes")
    print("================================\n")

def admin_panel(data):
    password = "india123"  # simple admin password
    entered = input("Enter admin password: ")
    if entered != password:
        print("❌ Wrong password! Returning to main menu.\n")
        return

    while True:
        print("\n--- Admin Panel ---")
        print("1. Add Candidates")
        print("2. Add Voters")
        print("3. View Candidate List")
        print("4. View Voter List (Admin Only)")
        print("5. View Results")
        print("6. Clear All Data")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_candidates(data)
        elif choice == "2":
            add_voters(data)
        elif choice == "3":
            show_candidates(data)
        elif choice == "4":
            show_voter_list(data)
        elif choice == "5":
            show_results(data)
        elif choice == "6":
            confirm = input("⚠️ Type 'CLEAR' to delete all data: ")
            if confirm == "CLEAR":
                data["candidates"].clear()
                data["votes"].clear()
                data["voters"].clear()
                data["voted"].clear()
                save_data(data)
                print("✅ All data cleared successfully.")
        elif choice == "7":
            break
        else:
            print("❌ Invalid choice, try again.")

# ---------- Voter Functions ----------
def voting(data):
    """Only registered voters can vote once."""
    if not data["candidates"]:
        print("⚠️ No candidates available. Admin must add candidates first.")
        return

    if not data["voters"]:
        print("⚠️ No registered voters. Admin must register voters first.")
        return

    voter_id = input("Enter your Voter ID: ").strip()
    voter_name = input("Enter your Name: ").strip()

    # ✅ Check if registered voter
    registered = any(v["id"] == voter_id for v in data["voters"])
    if not registered:
        print("❌ You are not a registered voter.")
        return

    # ✅ Check if already voted
    already_voted = any(v["id"] == voter_id for v in data["voted"])
    if already_voted:
        print("⚠️ You have already voted! Each voter can vote only once.\n")
        return

    show_candidates(data)

    try:
        choice = int(input("Enter the candidate number you want to vote for: "))
        if 1 <= choice <= len(data["candidates"]):
            voted_for = data["candidates"][choice - 1]
            data["votes"][voted_for] += 1
            data["voted"].append({"id": voter_id, "name": voter_name, "voted_for": voted_for})
            save_data(data)
            print(f"✅ Thank you {voter_name}! Your vote for '{voted_for}' has been recorded.\n")
        else:
            print("❌ Invalid candidate number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# ---------- Main Menu ----------
def main_menu():
    data = load_data()

    while True:
        print("\n===============================")
        print("🇮🇳  INDIAN VOTING SYSTEM  🇮🇳")
        print("===============================")
        print("1. Admin Panel")
        print("2. View Candidate List")
        print("3. Cast Vote")
        print("4. Show Results")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_panel(data)
        elif choice == "2":
            show_candidates(data)
        elif choice == "3":
            voting(data)
        elif choice == "4":
            show_results(data)
        elif choice == "5":
            print("🙏 Thank you for using the Indian Voting System!")
            break
        else:
            print("❌ Invalid choice, try again.")

# ---------- Run Program ----------
if __name__ == "__main__":
    main_menu()
