import streamlit as st
import mlflow.sklearn
import pandas as pd
from datetime import date
import plotly.express as px

# Set the tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Load the trained model
model_uri = "runs:/24bcacda27d84309b6060907e77a1ecc/model"  # Replace with the actual run ID from MLflow
model = mlflow.sklearn.load_model(model_uri)

# Streamlit app title
st.title("Stock Price Prediction App")

# Sidebar for user input
st.sidebar.header("Input Stock Details")
current_date = st.sidebar.date_input("Today's Date", date.today())
company = st.sidebar.selectbox("Select a company:", ["Apple", "Facebook", "Amazon", "Google", "Netflix"])
open_price = st.sidebar.number_input("Open Price", min_value=0.0, value=150.0, step=1.0)
high_price = st.sidebar.number_input("High Price", min_value=0.0, value=155.0, step=1.0)
low_price = st.sidebar.number_input("Low Price", min_value=0.0, value=145.0, step=1.0)
adj_close_price = st.sidebar.number_input("Adjusted Close Price", min_value=0.0, value=148.0, step=1.0)
volume = st.sidebar.number_input("Volume", min_value=0.0, value=1000000.0, step=10000.0)

# Prepare user input for the model
input_data = pd.DataFrame({
    "Open": [open_price],
    "High": [high_price],
    "Low": [low_price],
    "Adj Close": [adj_close_price],
    "Volume": [volume],
})

# Display user input
st.write("### User Input:")
st.write(f'Selected company name is{company}')
st.write(input_data)

# Make predictions
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"### Predicted Close Price: {prediction[0]:.2f}")

# Load dataset
faang_data = pd.read_csv("C:/Users/ragin/Downloads/project-4/filtered_data_iqr.csv")

# Preprocess the dataset
faang_data['Date'] = pd.to_datetime(faang_data['Date'])
faang_data['Year'] = faang_data['Date'].dt.year
faang_data['Year'] = faang_data['Year'].astype(str)
faang_data['Month'] = faang_data['Date'].dt.strftime('%B')  # Month names
faang_data['YearMonth'] = faang_data['Date'].dt.to_period('M').astype(str)  # Year-Month format

# Sidebar filters for dashboard
st.sidebar.header("View the Dashboard of Stock Details")
company = st.sidebar.selectbox("Select a Company", faang_data["Company"].unique())

# Add Year and Month to sidebar as a combined selectbox
year = st.sidebar.selectbox(
    "Select Year ", 
    [None] + list(faang_data['Year'].unique())
)

month = st.sidebar.selectbox(
    "Select Month", [None] + list(faang_data['Month'].unique())
)

# Filter data based on user selection
filtered_data = faang_data[faang_data["Company"] == company]

if year:
    filtered_data = filtered_data[filtered_data['Year'] == year]
if month:
    filtered_data = filtered_data[filtered_data['Month'] == month]

# Display title
st.title(f"FAANG Companies Dashboard - {company}")

# Display the filtered dataset
st.subheader("Filtered Dataset")
st.dataframe(filtered_data)

# Overall Performance
st.subheader(f"Overall Performance of {company}")
overall_avg = filtered_data["Close"].mean()
overall_max = filtered_data["Close"].max()
overall_min = filtered_data["Close"].min()
if not filtered_data.empty:
    st.write(f"**Average Close Price:** {overall_avg:.2f}")
    st.write(f"**Maximum Close Price:** {overall_max:.2f}")
    st.write(f"**Minimum Close Price:** {overall_min:.2f}")
else:
    st.write("No data available for the selected filters.")

# Yearly Report
yearly_report = faang_data[faang_data["Company"] == company].groupby("Year").agg(
    Average_Close=("Close", "mean"),
    Max_Close=("Close", "max"),
    Min_Close=("Close", "min")
).reset_index()
st.subheader(f"Year-Wise Report for {company}")
yearly_report['Year'] = yearly_report['Year'].astype(str)

st.dataframe(yearly_report)

# Monthly Report
monthly_report = faang_data[faang_data["Company"] == company].groupby("Month").agg(
    Average_Close=("Close", "mean"),
    Max_Close=("Close", "max"),
    Min_Close=("Close", "min")
).reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]).reset_index()
st.subheader(f"Month-Wise Report for {company}")
st.dataframe(monthly_report)


# Plot Yearly Data
fig_year = px.line(yearly_report, x="Year", y="Average_Close", title=f"{company} Yearly Average Close Price")
st.plotly_chart(fig_year)

# Plot Monthly Data
fig_month = px.line(monthly_report, x="Month", y="Average_Close", title=f"{company} Monthly Average Close Price")
st.plotly_chart(fig_month)
