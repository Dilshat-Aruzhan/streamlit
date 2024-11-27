import streamlit as st
import pandas as pd
import numpy as np
class project1:
    def init(self):
        pass
    def app(self):
        st.title('Creation of DataFrame')

        def load_data(file):
            if file is not None:
                data = pd.read_csv(file)
                return data
            return None
        upload = st.file_uploader("choose csv file")
        if upload is not None:
            df = load_data(upload)
            st.dataframe(df, height=400, width=600)

            column = st.selectbox("Choose a column for filtering", df.columns)

            unique_values = df[column].unique()
            selected_values = st.multiselect(f"Select values for {column}", options=unique_values,
                                             default=unique_values)

            filtered_df = df[df[column].isin(selected_values)]

            st.dataframe(filtered_df, height=400, width=600)

        st.markdown("""<style>
                     h1 {
                     color: green;
                     font-size:18px;
                     text-align:center;
                     }
                     </style>""", unsafe_allow_html=True)