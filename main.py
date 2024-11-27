import pandas as pd
from pandasai import SmartDataframe, Agent
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_groq import ChatGroq
from pandasai.llm import OpenAI
# from pandasai.llm import AzureOpenAI
# from pandasai.llm import GoogleVertexAI
import seaborn as sns

openai_llm = OpenAI(
    api_token="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",
)


df = pd.DataFrame({
    "country": [
        "United States",
        "United Kingdom",
        "France",
        "Germany",
        "Italy",
        "Spain",
        "Canada",
        "Australia",
        "Japan",
        "China",
    ],
    "gdp": [
        19294482071552,
        2891615567872,
        2411255037952,
        3435817336832,
        1745433788416,
        1181205135360,
        1607402389504,
        1490967855104,
        4380756541440,
        14631844184064,
    ],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12],
})


df1 = SmartDataframe(df, config={"llm": openai_llm})


print(df1.chat("Plot a pie chart of the gdp by country"))


