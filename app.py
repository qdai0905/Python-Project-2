import streamlit as st
import pandas as pd
import plotly.express as px

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Instagram User Analysis",
    page_icon="📸",
    layout="wide"
)

# ===================== LOAD DATA =====================
df = pd.read_excel(r"C:\Quang Dai\R\Dataset.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

# ===================== SIDEBAR =====================
st.sidebar.title("📊 Instagram Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    ["Overview", "User Behavior", "Engagement Analysis", "Content Insights"]
)

# ===================== OVERVIEW =====================
if menu == "Overview":
    st.title("📸 Instagram User Analysis Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Users", len(df))
    col2.metric("Avg Engagement", round(df["user_engagement_score"].mean(), 2))
    col3.metric("Avg Daily Time (min)", round(df["daily_active_minutes_instagram"].mean(), 1))

    st.subheader("Age Distribution")
    fig = px.histogram(df, x="age", nbins=20)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Gender Distribution")
    fig = px.pie(df, names="Gender")
    st.plotly_chart(fig, use_container_width=True)

# ===================== USER BEHAVIOR =====================
elif menu == "User Behavior":
    st.title("👤 User Behavior Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Daily Usage Time")
        fig = px.box(df, y="daily_active_minutes_instagram")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Session Length")
        fig = px.box(df, y="average_session_length_minutes")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Urban vs Rural Usage")
    fig = px.bar(
        df.groupby("urban_rural")["daily_active_minutes_instagram"].mean().reset_index(),
        x="urban_rural",
        y="daily_active_minutes_instagram",
        color="urban_rural"
    )
    st.plotly_chart(fig, use_container_width=True)

# ===================== ENGAGEMENT =====================
elif menu == "Engagement Analysis":
    st.title("🔥 Engagement Analysis")

    st.subheader("Engagement vs Followers")
    fig = px.scatter(
        df,
        x="Followers count",
        y="user_engagement_score",
        color="content_type_preference",
        size="posts_created_per_week"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Posts per Week vs Engagement")
    fig = px.bar(
        df,
        x="posts_created_per_week",
        y="user_engagement_score",
        color="content_type_preference"
    )
    st.plotly_chart(fig, use_container_width=True)

# ===================== CONTENT =====================
elif menu == "Content Insights":
    st.title("🎥 Content Insights")

    st.subheader("Content Type Preference")
    fig = px.pie(df, names="content_type_preference")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Feature Usage (Feed, Explore, Reels)")
    features = ["Feed", "Explore", "Reels", "Messages"]

    df_melt = df[features].melt(var_name="Feature", value_name="Usage")

    fig = px.box(df_melt, x="Feature", y="Usage", color="Feature")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Stress vs Instagram Usage")
    fig = px.scatter(
        df,
        x="daily_active_minutes_instagram",
        y="perceived_stress_score",
        color="diet_quality"
    )
    st.plotly_chart(fig, use_container_width=True)