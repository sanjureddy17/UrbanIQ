import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="UrbanIQ - Smart City Score",
    page_icon="🏙️",
    layout="wide"
)

# Title
st.title("🏙️ UrbanIQ - Bengaluru CityLife Score")

st.write(
    "Smart decision platform to compare Bengaluru locations "
    "based on lifestyle factors."
)

# Load data
city_df = pd.read_csv("data/citylife_scores.csv")

# Location selection
location = st.selectbox(
    "Select a location",
    city_df["location"].unique()
)

# Selected area data
area = city_df[city_df["location"] == location].iloc[0]

# Display score
st.subheader("⭐ CityLife Score")

st.metric(
    "Overall Score",
    round(area["citylife_score"], 2)
)

# Individual scores

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🚇 Metro", area["metro_score"])

    st.metric("🏥 Healthcare", area["healthcare_score"])

with col2:
    st.metric("🏫 Education", area["education_score"])

    st.metric("🌱 Environment", area["environment_score"])

with col3:
    st.metric("🚦 Traffic", area["traffic_score"])

st.subheader("🏆 Top Bengaluru Areas")

top_areas = city_df.sort_values(
    "citylife_score",
    ascending=False
).head(10)

st.bar_chart(
    top_areas.set_index("location")["citylife_score"]
)