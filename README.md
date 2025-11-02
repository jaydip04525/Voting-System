# Indian Voting System (Beginner Level with JSON)

A simple **command-line voting system** built using **Python**.  
It simulates a real Indian-style election system where **voters**, **candidates**, and **admins** interact under clear rules.

---

## ✨ Features

✅ Beginner-friendly Python code  
✅ JSON-based data storage (no database needed)  
✅ Admin login to manage election data  
✅ Register voters (10-digit unique voter ID required)  
✅ Allow duplicate voter names but not duplicate IDs  
✅ Each voter can **vote only once**  
✅ Public can view candidate list and results  
✅ Only admin can see voter list  
✅ Prevents invalid or repeated votes

---

## 🧠 How It Works

| Role | Permissions |
|------|--------------|
| **Admin** | Add candidates, register voters, view all voters, clear data, and view results |
| **Voter** | View candidate list, vote once using their voter ID |
| **Public** | View candidate list and final results |

---

## 🗂️ Project Structure

📁 Indian-Voting-System/

├── voting_system.py # Main Python file

├── voting_data.json # Stores all candidates, voters, and votes

├── README.md # Documentation file
