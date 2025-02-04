import json
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import pandas as pd

from sqlalchemy import create_engine
import numpy as np
from sqlalchemy import text
from openai import OpenAI
import streamlit as st

# Load environment variables from .env file
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")


llm_name = "gpt-4o-mini"
model = ChatOpenAI(api_key=openai_key, model=llm_name)

# call ChatOpenAI class and assign to variable
client = OpenAI(api_key=openai_key)

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

# create a db from csv file

# Path to your SQLite database file
database_file_path = "./db/salary.db"

# Create an engine to connect to the SQLite database
# SQLite only requires the path to the database file
engine = create_engine(f"sqlite:///{database_file_path}")
file_url = "./data/salaries_2023.csv"
os.makedirs(os.path.dirname(database_file_path), exist_ok=True)
df = pd.read_csv(file_url).fillna(value=0)
df.to_sql("salaries_2023", con=engine, if_exists="replace", index=False)

#print(f"Database created successfully! {df}")