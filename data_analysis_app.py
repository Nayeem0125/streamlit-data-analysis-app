import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Simple Data Analysis App")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Display basic information about the dataset
        st.subheader("Dataset Information")
        st.write(f"Number of rows: {df.shape[0]}")
        st.write(f"Number of columns: {df.shape[1]}")
        
        # Display the first few rows of the dataset
        st.subheader("Preview of the Dataset")
        st.write(df.head())
        
        # Display summary statistics
        st.subheader("Summary Statistics")
        st.write(df.describe())
        
        # Column selection for visualization
        st.subheader("Data Visualization")
        column = st.selectbox("Select a column for visualization", df.columns)
        
        # Create a histogram
        fig, ax = plt.subplots()
        ax.hist(df[column], bins=20)
        ax.set_title(f"Histogram of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
        
        # Create a box plot
        fig, ax = plt.subplots()
        sns.boxplot(x=df[column], ax=ax)
        ax.set_title(f"Box Plot of {column}")
        st.pyplot(fig)

if __name__ == "__main__":
    main()
