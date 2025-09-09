import pandas as pd
import random

# ------------------ Expense Categorization ------------------
def categorize_transactions(df):
    categories = {
        "Food 🍔": ["zomato", "swiggy", "restaurant", "food", "pizza", "burger"],
        "Shopping 🛍️": ["myntra", "amazon", "flipkart", "ajio", "shopping", "store"],
        "Travel 🚗": ["uber", "ola", "rapido", "train", "flight", "bus"],
        "Subscriptions 🎶": ["spotify", "netflix", "prime", "hotstar", "subscription"],
        "Bills 💡": ["electricity", "water", "bill", "recharge", "gas", "upi"],
    }

    df["Category"] = "Misc 🌀"
    for category, keywords in categories.items():
        for keyword in keywords:
            mask = df["Description"].str.contains(keyword, case=False, na=False)
            df.loc[mask, "Category"] = category
    return df

# ------------------ Monthly Summary ------------------
def monthly_summary(df):
    return df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum().reset_index()

# ------------------ Category Breakdown ------------------
def category_breakdown(df):
    return df.groupby("Category")["Amount"].sum().reset_index()

# ------------------ Top Vendors ------------------
def top_vendors(df, n=5):
    return df.groupby("Description")["Amount"].sum().nlargest(n).reset_index()

# ------------------ Anomaly Detection ------------------
def detect_anomalies(df):
    mean = df["Amount"].mean()
    std = df["Amount"].std()
    return df[df["Amount"] > mean + 2 * std]

# ------------------ Roast Generator ------------------
def generate_roast_summary(df):
    total_spent = df["Amount"].sum()
    top_category = df.groupby("Category")["Amount"].sum().idxmax()
    top_vendor = df.groupby("Description")["Amount"].sum().idxmax()

    roasts = [
        f"Bruh 💸 you spent ₹{int(total_spent)} this month. Even Ambani is shook rn.",
        f"Your fav hobby = burning money on {top_category}. 🔥",
        f"Why is {top_vendor} draining your wallet like it's Netflix autoplay? 📉",
        f"Your expenses look like a horror movie, and the villain is YOU. 😭"
    ]
    return random.choice(roasts)
