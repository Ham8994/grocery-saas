import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= AUTH =================
USER = "admin"
PASS = "1234"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():
    st.title("🔐 Login to Grocery SaaS")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USER and password == PASS:
            st.session_state.logged_in = True
            st.success("Login successful")
        else:
            st.error("Invalid credentials")


# ================= AI RECOMMENDER =================
def recommend(df, budget=150):
    filtered = df[df["Price"] <= budget].copy()

    if filtered.empty:
        return filtered

    filtered["Score"] = filtered["Price_per_100g"]
    filtered = filtered.sort_values("Score")

    return filtered


# ================= APP =================
def app():

    st.set_page_config(page_title="Grocery SaaS", layout="wide")
    st.title("🔥 Grocery AI SaaS Dashboard")

    # ---------------- FILE UPLOAD ----------------
    st.sidebar.header("📂 Upload CSV")
    file = st.sidebar.file_uploader("Upload your receipt CSV", type=["csv"])

    data = {
        "Product": ["Coke", "Pepsi", "Juice", "Milk", "Biscuits"],
        "Price": [120, 115, 140, 180, 80],
        "Weight": [500, 500, 1000, 1000, 200],
        "Sugar": [53, 54, 22, 5, 18]
    }

    df = pd.DataFrame(data)

    if file:
        df = pd.read_csv(file)

    # Feature engineering
    if "Price_per_100g" not in df.columns:
        df["Price_per_100g"] = df["Price"] / df["Weight"] * 100

    # ---------------- SIDEBAR ----------------
    option = st.sidebar.selectbox(
        "Choose Feature",
        ["Dashboard", "Best Product", "Worst Product", "Search", "AI Recommend"]
    )

    budget = st.sidebar.slider("💰 Set Budget", 50, 500, 150)

    best = df.loc[df["Price_per_100g"].idxmin()]
    worst = df.loc[df["Price_per_100g"].idxmax()]

    # ---------------- DASHBOARD ----------------
    if option == "Dashboard":
        st.subheader("📊 Full Dataset")
        st.dataframe(df)

        st.subheader("📈 Price Comparison")

        fig, ax = plt.subplots()
        ax.bar(df["Product"], df["Price_per_100g"])
        st.pyplot(fig)

    # ---------------- BEST ----------------
    elif option == "Best Product":
        st.subheader("🏆 Best Value Product")
        st.dataframe(pd.DataFrame([best]))

    # ---------------- WORST ----------------
    elif option == "Worst Product":
        st.subheader("💸 Worst Value Product")
        st.dataframe(pd.DataFrame([worst]))

    # ---------------- SEARCH ----------------
    elif option == "Search":
        q = st.text_input("Search Product")

        if q:
            res = df[df["Product"].str.lower().str.contains(q.lower())]
            st.dataframe(res)

            if not res.empty:
                fig, ax = plt.subplots()
                ax.bar(res["Product"], res["Price_per_100g"])
                st.pyplot(fig)

    # ---------------- AI RECOMMEND ----------------
    elif option == "AI Recommend":
        st.subheader("🤖 AI Smart Recommendations")

        result = recommend(df, budget)

        if result.empty:
            st.warning("No products found under this budget")
        else:
            st.dataframe(result)

            fig, ax = plt.subplots()
            ax.bar(result["Product"], result["Price_per_100g"])
            st.pyplot(fig)


# ================= RUN =================
if not st.session_state.logged_in:
    login()
else:
    app()
