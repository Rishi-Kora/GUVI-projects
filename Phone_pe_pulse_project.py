#!/usr/bin/env python
# coding: utf-8

# In[3]:


path1 = "pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path1)

col1 = {'State': [], 'Year': [], 'Quater': [], 'Transaction_type': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in Agg_state_list:
    p_i = path1 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            A = json.load(Data)
            for z in A['data']['transactionData']:
                Name = z['name']
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']
                col1['Transaction_type'].append(Name)
                col1['Transaction_count'].append(count)
                col1['Transaction_amount'].append(amount)
                col1['State'].append(i)
                col1['Year'].append(j)
                col1['Quater'].append(int(k.strip('.json')))

df_aggregated_transaction = pd.DataFrame(col1)

print(df_aggregated_transaction)

df_aggregated_transaction.head()


# In[4]:


pip install streamlit


# In[5]:


import streamlit as st
from PIL import Image
import json
from streamlit_option_menu import option_menu
import subprocess
import plotly.express as px
import pandas as pd
import sqlite3
import requests
import os
import base64


# In[7]:


def os():
    path1 = "pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path1)

col1 = {'State': [], 'Year': [], 'Quater': [], 'Transaction_type': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in Agg_state_list:
    p_i = path1 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            A = json.load(Data)
            for z in A['data']['transactionData']:
                Name = z['name']
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']
                col1['Transaction_type'].append(Name)
                col1['Transaction_count'].append(count)
                col1['Transaction_amount'].append(amount)
                col1['State'].append(i)
                col1['Year'].append(j)
                col1['Quater'].append(int(k.strip('.json')))

df_aggregated_transaction = pd.DataFrame(col1)

print(df_aggregated_transaction)

df_aggregated_transaction.head()


# In[8]:


path2 = 'pulse/data/aggregated/user/country/india/state/'
user_list = os.listdir(path2)

col2 = {'State': [], 'Year': [], 'Quater': [], 'brands': [], 'Count': [],
        'Percentage': []}
for i in user_list:
    p_i = path2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            B = json.load(Data)
            try:
                for w in B["data"]["usersByDevice"]:
                    brand_name = w["brand"]
                    count_ = w["count"]
                    ALL_percentage = w["percentage"]
                    col2["brands"].append(brand_name)
                    col2["Count"].append(count_)
                    col2["Percentage"].append(ALL_percentage)
                    col2["State"].append(i)
                    col2["Year"].append(j)
                    col2["Quater"].append(int(k.strip('.json')))
            except:
                pass
df_aggregated_user = pd.DataFrame(col2)
print(df_aggregated_user)
df_aggregated_user.head()

df_aggregated_user.isnull().sum()


# In[9]:


path3 ="pulse/data/map/transaction/hover/country/india/state/"
hover_list = os.listdir(path3)

col3 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'count': [],
        'amount': []}
for i in hover_list:
    p_i = path3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            C = json.load(Data)
            for x in C["data"]["hoverDataList"]:
                District = x["name"]
                count = x["metric"][0]["count"]
                amount = x["metric"][0]["amount"]
                col3["District"].append(District)
                col3["count"].append(count)
                col3["amount"].append(amount)
                col3['State'].append(i)
                col3['Year'].append(j)
                col3['Quater'].append(int(k.strip('.json')))
df_map_transaction = pd.DataFrame(col3)
print(df_map_transaction)
df_map_transaction.head()

df_map_transaction.isnull().sum()


# In[10]:


path4 = 'pulse/data/map/user/hover/country/india/state/'
map_list = os.listdir(path4)

col4 = {"State": [], "Year": [], "Quater": [], "District": [],
        "RegisteredUser": []}
for i in map_list:
    p_i = path4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            D = json.load(Data)

            for u in D["data"]["hoverData"].items():
                district = u[0]
                registereduser = u[1]["registeredUsers"]
                col4["District"].append(district)
                col4["RegisteredUser"].append(registereduser)
                col4['State'].append(i)
                col4['Year'].append(j)
                col4['Quater'].append(int(k.strip('.json')))
df_map_user = pd.DataFrame(col4)
df_map_user.head()


# In[11]:


path5 = "pulse/data/top/transaction/country/india/state/"
TOP_list = os.listdir(path5)

col5 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in TOP_list:
    p_i = path5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            E = json.load(Data)
            for z in E['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                col5['District'].append(Name)
                col5['Transaction_count'].append(count)
                col5['Transaction_amount'].append(amount)
                col5['State'].append(i)
                col5['Year'].append(j)
                col5['Quater'].append(int(k.strip('.json')))
df_top_transaction = pd.DataFrame(col5)
df_top_transaction.head()


path6 = "pulse/data/top/user/country/india/state/"
USER_list = os.listdir(path6)


# In[12]:


col6 = {'State': [], 'Year': [], 'Quater': [], 'District': [],
        'RegisteredUser': []}
for i in USER_list:
    p_i = path6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            F = json.load(Data)
            for t in F['data']['pincodes']:
                Name = t['name']
                registeredUser = t['registeredUsers']
                col6['District'].append(Name)
                col6['RegisteredUser'].append(registeredUser)
                col6['State'].append(i)
                col6['Year'].append(j)
                col6['Quater'].append(int(k.strip('.json')))
df_top_user = pd.DataFrame(col6)
df_top_user.head()


# In[13]:


combined_df = pd.concat([df_aggregated_transaction,df_aggregated_user,df_map_transaction,df_map_user,df_top_transaction,df_top_user])


# In[14]:


combined_df.drop_duplicates(inplace=True)


# In[15]:


combined_df =combined_df.rename(columns={'count': 'count1'})


# In[16]:


print(combined_df)


# In[17]:


import sqlite3


# In[ ]:


conn = sqlite3.connect('phonepe_dashboard.db')


# In[19]:


def combined_df():
    combined_df.to_sql('phonepe_database', conn , if_exists='replace')


# In[21]:


def conn():
    conn.commit()
cursor=conn.cursor()


# In[22]:


st.set_page_config(page_title='PhonePe Pulse Data Visualization and Exploration', page_icon=':phonepe:', layout='wide')
st.title('PhonePe Pulse Data Visualization and Exploration')


# In[23]:


def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)


# In[24]:


import streamlit as st
from PIL import Image
import urllib.request
from io import BytesIO


# In[25]:


menu_items = ["About","Search","Home","Basic insights"]
menu_icons = ["🔍","🏠","📊","ℹ️"]
default_index = 0
select = st.sidebar.selectbox("Menu", menu_items, index=default_index)


# In[26]:


if select == "About":
    st.title("ABOUT")
    st.write("----")
    st.subheader("Welcome")
    st.write("This project aims to create a Streamlit App for the visualization and exploration of PhonePe Pulse Data. The App enables users to visualize and explore various insights based on the PhonePe Pulse Data. The App also provides a search section where a user can search for any transaction by providing details such as transaction ID, mobile number or bank reference number.")
    st.write("The datasets used here are for academic purposes only and belongs to no company or institution.Below you can find the dataframe of phonepe pulse data")
    st.dataframe(combined_df)


# In[28]:


st.write("Saving dataframe as csv")
csv = combined_df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="combined_df.csv">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)


# In[29]:


video_url = "https://www.youtube.com/watch?v=c_1H6vivsiA&t=6s" # Replace with the URL of your video
st.write("Here's a video about PhonePe Pulse:")
st.video(video_url)


# In[30]:


if select == "Home":
    col1 = st.columns(1)[0]
    st.image(Image.open("phonepe-logo-icon.png"),width = 500)
    col1.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
    col1.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")


# In[31]:


import plotly.express as px
import json


# In[32]:


if select == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["Top 10 states based on year and amount of transaction", 
               "Least 10 states based on type and amount of transaction",
               "Top 10 mobile brands based on percentage of transaction",
               "Top 10 Registered-users based on States and District(pincode)",
               "Top 10 Districts based on states and amount of transaction",
               "Least 10 Districts based on states and amount of transaction",
               "Least 10 registered-users based on Districts and states",
               "Top 10 transactions_type based on states and transaction_amount"]
    choose = st.selectbox("Select the option", options)


# In[34]:


def choose():
    if choose=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM phonepe_database GROUP BY State ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)


# In[36]:


with col2:
            st.title("Top 10 states based on type and amount of transaction")
            st.bar_chart(data=df,x="State",y="Transaction_amount")  
    elif choose=="Least 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM phonepe_database GROUP BY State ORDER BY transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 states based on type and amount of transaction")
            st.bar_chart(data=df,x="State",y="Transaction_amount")
    elif choose=="Top 10 mobile brands based on percentage of transaction":
        cursor.execute("SELECT DISTINCT brands,Percentage FROM phonepe_database GROUP BY brands ORDER BY Percentage DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['brands','Percentage'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 mobile brands based on percentage of transaction")
            st.bar_chart(data=df,x="brands",y="Percentage")
    elif choose=="Top 10 Registered-users based on States and District(pincode)":
        cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM phonepe_database GROUP BY State,District ORDER BY RegisteredUser DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District(pincode)")
            st.bar_chart(data=df,x="State",y="RegisteredUser") 
    elif choose=="Top 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,Transaction_amount FROM phonepe_database GROUP BY State,District ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df,x="State",y="Transaction_amount")  
    elif choose=="Least 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,Transaction_amount FROM phonepe_database GROUP BY State,District ORDER BY Transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df,x="State",y="Transaction_amount",color='red')
    elif choose=="Least 10 registered-users based on Districts and states":
        cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM phonepe_database GROUP BY State,District ORDER BY RegisteredUser ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 registered-users based on Districts and states")
            st.bar_chart(data=df,x="State",y="RegisteredUser")
    elif choose=="Top 10 transactions_type based on states and transaction_amount":
        cursor.execute("SELECT DISTINCT State,Transaction_type,Transaction_amount FROM phonepe_database GROUP BY State,Transaction_type ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_type','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 transactions_type based on states and transaction_amount")
            st.bar_chart(data=df,x="State",y="Transaction_amount")


# In[37]:


if select== "Search":
    Topic = ["","Transaction-Type","District","Brand","Top-Transactions","Registered-users"]
    choice_topic = st.selectbox("Search by",Topic)
    
    def type_(type):
        cursor.execute(f"SELECT DISTINCT State,Quater,Year,Transaction_type,Transaction_amount FROM phonepe_database WHERE Transaction_type =  '{type}' ORDER BY State,Quater,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Quater', 'Year', 'Transaction_type', 'Transaction_amount'])
        return df
    def type_year(year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_amount FROM phonepe_database WHERE Year = '{year}' AND  Transaction_type = '{type}' ORDER BY State,Quater,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type', 'Transaction_amount'])
        return df
    def type_state(state,year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_amount FROM phonepe_database WHERE State = '{state}'    AND Transaction_type = '{type}' And Year = '{year}' ORDER BY State,Quater,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type', 'Transaction_amount'])
        return df
    def district_choice_state(_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM phonepe_database WHERE State = '{_state}' ORDER BY State,Year,Quater,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
        return df
    def dist_year_state(year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM phonepe_database WHERE Year = '{year}' AND State = '{_state}' ORDER BY State,Year,Quater,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
        return df
    def district_year_state(_dist,year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM phonepe_database WHERE District = '{_dist}' AND State = '{_state}' AND Year = '{year}' ORDER BY State,Year,Quater,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
        return df
    def brand_(brand_type):
        cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM phonepe_database WHERE brands='{brand_type}' ORDER BY State,Year,Quater,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
        return df
    def brand_year(brand_type,year):
        cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM phonepe_database WHERE Year = '{year}' AND brands='{brand_type}' ORDER BY State,Year,Quater,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
        return df
    def brand_state(state,brand_type,year):
        cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM phonepe_database WHERE State = '{state}' AND brands='{brand_type}' AND Year = '{year}' ORDER BY State,Year,Quater,brands,Percentage ");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
        return df
    def transaction_state(_state):
        cursor.execute(f"SELECT State,Year,Quater,District,Transaction_count,Transaction_amount FROM phonepe_database WHERE State = '{_state}' GROUP BY State,Year,Quater")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def transaction_year(_state,_year):
        cursor.execute(f"SELECT State,Year,Quater,District,Transaction_count,Transaction_amount FROM phonepe_database WHERE Year = '{_year}' AND State = '{_state}' GROUP BY State,Year,Quater")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def transaction_quater(_state,_year,_quater):
        cursor.execute(f"SELECT State,Year,Quater,District,Transaction_count,Transaction_amount FROM phonepe_database WHERE Year = '{_year}' AND Quater = '{_quater}' AND State = '{_state}' GROUP BY State,Year,Quater")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def registered_user_state(_state):
        cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM phonepe_database WHERE State = '{_state}' ORDER BY State,Year,Quater,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
        return df
    def registered_user_year(_state,_year):
        cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM phonepe_database WHERE Year = '{_year}' AND State = '{_state}' ORDER BY State,Year,Quater,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
        return df
    def registered_user_district(_state,_year,_dist):
        cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM phonepe_database WHERE Year = '{_year}' AND State = '{_state}' AND District = '{_dist}' ORDER BY State,Year,Quater,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
        return df


# In[41]:


if choice_topic=="Transaction-Type":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 5 TYPES OF TRANSACTION --")
            transaction_type = st.selectbox("search by", ["Choose an option", "Peer-to-peer payments",
                                                           "Merchant payments", "Financial Services",
                                                           "Recharge & bill payments", "Others"], 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                           'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                           'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                            'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                            'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                            'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
            
        if transaction_type:
            col1,col2,col3, = st.columns(3)
            with col1:
                st.subheader(f'{transaction_type}')
                st.write(type_(transaction_type))
        if transaction_type and choice_year:
            with col2:
                st.subheader(f' in {choice_year}')
                st.write(type_year(choice_year,transaction_type))
        if transaction_type and choice_state and choice_year:
            with col3:
                st.subheader(f' in {choice_state}')
                st.write(type_state(choice_state,choice_year,transaction_type)) 
            
    if choice_topic=="District":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                           'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                           'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                           'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("-- SELECT DISTRICTS --")
            district = st.selectbox("search by", df_map_transaction["District"].unique().tolist())
        if choice_state:
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(f'{choice_state}')
                st.write(district_choice_state(choice_state))
        if choice_year and choice_state:
            with col2:
                st.subheader(f'in {choice_year} ')
                st.write(dist_year_state(choice_year,choice_state))
        if district and choice_state and choice_year:
            with col3:
                st.subheader(f'in {district} ')
                st.write(district_year_state(district,choice_year,choice_state))
            
    if choice_topic=="Brand":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- TYPES OF BRANDS --")
            mobiles = ["",'Xiaomi', 'Vivo', 'Samsung', 'Oppo', 'Realme', 'Apple', 'Huawei', 'Motorola', 'Tecno', 'Infinix',
                        'Lenovo', 'Lava', 'OnePlus', 'Micromax', 'Asus', 'Gionee', 'HMD Global', 'COOLPAD', 'Lyf',
                        'Others']
            brand_type = st.selectbox("search by",mobiles, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                           'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                           'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
        if brand_type:
            col1,col2,col3, = st.columns(3)
            with col1:
                st.subheader(f'{brand_type}')
                st.write(brand_(brand_type))
        if brand_type and choice_year:
            with col2:
                st.subheader(f' in {choice_year}')
                st.write(brand_year(brand_type,choice_year))
        if brand_type and choice_state and choice_year:
            with col3:
                st.subheader(f' in {choice_state}')
                st.write(brand_state(choice_state,brand_type,choice_year))


    if choice_topic=="Top-Transactions":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("--4 Quaters --")
            menu_quater = ["", "1", "2", "3", "4"]
            choice_quater = st.selectbox("Quater", menu_quater, 0)
        if choice_state:
            with col1:
                st.subheader(f'{choice_state}')
                st.write(transaction_state(choice_state))
        if choice_state and choice_year:
            with col2:
                st.subheader(f'{choice_year}')
                st.write(transaction_year(choice_state,choice_year))
        if choice_state and choice_quater:
            with col3:
                st.subheader(f'{choice_quater}')
                st.write(transaction_quater(choice_state,choice_year,choice_quater))
              
        if choice_topic=="Registered-users":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("--4 Quaters --")
            menu_quater = ["", "1", "2", "3", "4"]
            choice_quater = st.selectbox("Quater", menu_quater, 0)
        if choice_state:
            with col1:
                st.subheader(f'{choice_state}')
                st.write(transaction_state(choice_state))
        if choice_state and choice_year:
            with col2:
                st.subheader(f'{choice_year}')
                st.write(transaction_year(choice_state,choice_year))
        if choice_state and choice_quater:
            with col3:
                st.subheader(f'{choice_quater}')
                st.write(transaction_quater(choice_state,choice_year,choice_quater))


# In[42]:


options = ['Total Transaction Count', 'Total Transaction Amount', 'Total Unique Users']
selected_option = st.selectbox('Select a fact or figure:', options)


# In[43]:


if selected_option == 'Total Transaction Count':
    df = combined_df[['Transaction_type', 'Transaction_count']].head(10)
    fig = px.pie(df, values='Transaction_count', names='Transaction_type', title='Top 10 Transaction Types by Count', height=500)
    st.plotly_chart(fig)


# In[44]:


elif selected_option == 'Total Transaction Amount':
    df1 =combined_df[['Transaction_type', 'Transaction_amount']].head(10)
    fig = px.bar(df1, x='Transaction_type', y='Transaction_amount', color='Transaction_type',
                 title='Top 10 Transaction Types by Amount', height=500)
    st.plotly_chart(fig)


# In[45]:


elif selected_option == 'Total Unique Users':
    df2 =combined_df[['brands', 'Percentage']]
    fig = px.bar(df2, x='brands', y='Percentage', color='brands',
                 title='Top 10 States by Unique Users', height=500)
    st.plotly_chart(fig)    


# In[ ]:




