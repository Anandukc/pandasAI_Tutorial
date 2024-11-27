# # # from dotenv import load_dotenv
# # # import os
# # # import streamlit as st
# # # import pandas as pd
# # # from pandasai.llm import OpenAI

# # # #load env fille
# # # load_dotenv()

# # # API_KEY = os.environ['OPENAI_API_KEY']

# # # st.title("Data Visualization Using PandasAI")

# # # uploaded_file= st.file_uploader("upload your csv for analysing and visulization", type=['csv'])

# # # if uploaded_file is not None:
# # #     df = pd.read_csv(uploaded_file)
# # #     st.write(df.head(3))

# # #     prompt = st.text_area("Enter your question")

# # #     if st.button("Generate"):
# # #         if prompt:
# # #             st.write("AI GENERATING RESPONSE , PLEASE WAIT")
# # #         else:
# # #             st.warning("please enter a prompt.")


# # from dotenv import load_dotenv
# # from langchain_openai import ChatOpenAI

# # # Load environment variables from .env
# # load_dotenv()

# # # Create a ChatOpenAI model
# # model = ChatOpenAI(model="gpt-4o")

# # # Invoke the model with a message
# # result = model.invoke("What is 81 divided by 9?")
# # print("Full result:")
# # print(result)
# # print("Content only:")
# # print(result.content)
# import os
# import pandas as pd
# from pandasai import SmartDataframe, Agent
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_groq import ChatGroq
# from pandasai.llm import OpenAI
# from pandasai.llm import AzureOpenAI
# from pandasai.llm import GoogleVertexAI
# import seaborn as sns

# openai_llm = OpenAI(
#     api_token="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",
# )


# df = pd.DataFrame({
#     "country": [
#         "United States",
#         "United Kingdom",
#         "France",
#         "Germany",
#         "Italy",
#         "Spain",
#         "Canada",
#         "Australia",
#         "Japan",
#         "China",
#     ],
#     "gdp": [
#         19294482071552,
#         2891615567872,
#         2411255037952,
#         3435817336832,
#         1745433788416,
#         1181205135360,
#         1607402389504,
#         1490967855104,
#         4380756541440,
#         14631844184064,
#     ],
#     "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12],
# })
# # azure_llm = AzureOpenAI(
# #     api_token="my-azure-openai-api-key",
# #     azure_endpoint="my-azure-openai-api-endpoint",
# #     api_version="2023-05-15",
# #     deployment_name="my-deployment-name"
# # )

# # vertexai_llm = GoogleVertexAI(
# #   project_id="generative-ai-training",
# #   location="us-central1",
# #   model="text-bison@001"
# # )

# df1 = SmartDataframe(df, config={"llm": openai_llm})
# # df2 = SmartDataframe(df, config={"llm": azure_llm})
# # df3 = SmartDataframe(df, config={"llm": vertexai_llm})

# print(df1.chat("Plot a pie chart of the gdp by country"))
# # print(df2.chat("Which one is the unhappiest country?"))
# # print(df3.chat("What is the sum of the GDP of the 2 unhappiest countries?"))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# # Load environment variables from .env
# load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini", openai_api_key="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")
# Invoke the model with a message
result = model.invoke("can you give me a bar plot and send me link for the following data The most populated countries in the world in 2024 are India: 1,450,935,791 people,China: 1,419,321,278 people,United States: 345,426,571 people ,Indonesia: 283,487,931 peopl ")
print("Full result:")
print(result)
print("Content only:")
print(result.content)