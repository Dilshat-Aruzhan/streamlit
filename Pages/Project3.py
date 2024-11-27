import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Project3:
    def init(self):
        pass

    def load_data(self, file):
        """Load data from a CSV file."""
        if file is not None:
            data = pd.read_csv(file)
            return data
        return None

    def clean_and_convert_values(self, df, column):
        """Clean numerical values and convert them to float."""
        # Convert to string for processing
        df[column] = df[column].astype(str)

        # Replace commas with dots and remove spaces
        df[column] = df[column].replace({',': '.'}, regex=True)  # Replace comma with dot
        df[column] = df[column].str.replace(r'\s+', '', regex=True)  # Remove spaces

        # Convert to numeric, if conversion fails, set to NaN
        df[column] = pd.to_numeric(df[column], errors='coerce')

        return df

    def plot_bar_chart(self, df, category_column, value_column):
        """Bar chart for categorical data with the mean calculation."""
        # Clean and convert values to numeric
        df = self.clean_and_convert_values(df, value_column)

        # Check if columns have correct types
        if df[category_column].dtype == 'object' or df[category_column].dtype.name == 'category':
            if df[value_column].dtype in ['int64', 'float64']:
                # Group by the categorical column and calculate the mean for each value
                category_mean = df.groupby(category_column)[value_column].mean()

                # Create a color list for each bar
                colors = plt.cm.get_cmap(name="tab20", lut=len(category_mean))

                # Plot bar chart with different colors for each bar
                fig, ax = plt.subplots()
                category_mean.plot(kind='bar', ax=ax, color=colors(np.arange(len(category_mean))))
                ax.set_title(f'Mean {value_column} by {category_column}')
                ax.set_xlabel(category_column)
                ax.set_ylabel(f'Mean {value_column}')
                st.pyplot(fig)

                # Display the mean values for each category
                st.write(f"Mean {value_column} by {category_column}:")
                st.dataframe(category_mean)
            else:
                st.warning(f"{value_column} is not a numeric column. Please select a numeric column for values.")
        else:
            st.warning(f"{category_column} is not a categorical column. Please select a categorical column.")

    def app(self):
        st.title("Creation of DataFrame")

        # File upload
        upload = st.file_uploader("Choose a CSV file")
        if upload is not None:
            df = self.load_data(upload)
            st.dataframe(df, height=400, width=600)

            # Select columns for categorical and numeric data
            category_column = st.selectbox("Choose a column for category (categorical)", df.columns)
            value_column = st.selectbox("Choose a column for values (numeric)", df.columns)

            if category_column and value_column:
                st.subheader(f"Bar Chart and Mean of {value_column} by {category_column}")
                self.plot_bar_chart(df, category_column, value_column)
        else:
            st.warning("Please upload a CSV file")

        st.markdown(
            """
            <style>
            h1 {
                color: green;
                font-size: 18px;
                text-align: center;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )