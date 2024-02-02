
import streamlit as st
import os

# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["user"])
st.write("DB password:", st.secrets["password"])
st.write("My cool secrets:", st.secrets["connections.snowflake"]["key"])

# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
