import pandas as pd
import json

# Read CSV
df = pd.read_csv("employees.csv")

print("Full Data:")
print(df)

# IT Employees
print("\nIT Employees:")
print(df[df["dept"] == "IT"])

# Salary > 50000
print("\nSalary Greater Than 50000:")
print(df[df["salary"] > 50000])

# Gmail Users Count
gmail_users = df[df["email"].str.endswith("@gmail.com")]
print("\nGmail Users Count:", len(gmail_users))

# Inactive Users > 30 days
inactive = df[df["last_login_days"] > 30]
print("\nInactive Users:")
print(inactive)

# Save inactive users
inactive.to_csv("inactive.csv", index=False)

# Avg salary by department
print("\nAverage Salary By Department:")
print(df.groupby("dept")["salary"].mean())

# Summary JSON
summary = {
    "total_users": len(df),
    "gmail_users": len(gmail_users),
    "inactive_users": len(inactive),
    "highest_salary": int(df["salary"].max())
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("\nsummary.json created")
