# --- AI keyword categories ---
categories_keywords = {
   "food": ["pizza", "burger", "restaurant", "coffee"],
   "transport": ["bus", "uber", "taxi", "train"],
   "rent": ["rent", "apartment"],
   "entertainment": ["movie", "game", "netflix"]
}
# --- Function: suggest category (AI idea) ---
def suggest_category(description):
   description = description.lower()
   for category, keywords in categories_keywords.items():
       for word in keywords:
           if word in description:
               return category
   return "other"
# --- Function: calculate total ---
def calculate_total(expenses):
   return sum(expenses.values())
# --- Function: save data to file ---
def save_to_file(expenses):
   with open("expenses.txt", "w") as file:
       for category, amount in expenses.items():
           file.write(f"{category}: {amount}\n")
# --- Function: read data from file ---
def read_from_file():
   try:
       with open("expenses.txt", "r") as file:
           print("\nSaved data:")
           print(file.read())
   except FileNotFoundError:
       print("\nNo previous data found.")
# --- MAIN PROGRAM ---
expenses = {}
print("Welcome to Personal Finance Manager")
# --- Input income ---
income = float(input("Enter your income: "))
# --- Loop to enter multiple expenses ---
while True:
   desc = input("Enter expense description (or 'done' to finish): ")
   if desc.lower() == "done":
       break
   amount = float(input("Enter amount: "))
   # AI suggestion
   category = suggest_category(desc)
   print(f"Suggested category: {category}")
   # Store in dictionary
   if category in expenses:
       expenses[category] += amount
   else:
       expenses[category] = amount
# --- Processing ---
total_expenses = calculate_total(expenses)
balance = income - total_expenses
# --- Output results ---
print("\nTotal expenses:", total_expenses)
print("Remaining balance:", balance)
# --- Conditional logic ---
if balance < 0:
   print("Warning: You are overspending!")
elif balance > income * 0.2:
   print("Good job saving!")
else:
   print("Try to save more money.")
# --- File management ---
save_to_file(expenses)
read_from_file()