#!/usr/bin/env python
# coding: utf-8

# ## INPUT DATA TABLE

# ### REVIEW DATA TABLE

# In[1]:


# loading in lybrary
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# DB File 
Dbfile ='olist.db'

# NAMA FILE IMPORT
dbfile = 'olist.db'
# CONNECT SQL
con = sqlite3.connect(dbfile)

# CURSOR
cur = con.cursor()

# ISI TABEL
DATA_TABLE = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# KELUARIN ISI TABEL
print(DATA_TABLE)


# ### CUSTOMER TABLE

# In[4]:


data_customer = pd.read_sql_query('SELECT * FROM olist_order_customer_dataset', con)
data_customer.set_index("index", inplace=True)
data_customer.head()


# ### ORDER TABEL

# In[4]:


data_order = pd.read_sql_query('SELECT * FROM olist_order_dataset', con)
data_order.set_index("index", inplace=True)
data_order.head()


# ### ORDER REVIEW TABLE

# In[5]:


df_reviews = pd.read_sql_query('SELECT * FROM olist_order_reviews_dataset', con)
df_reviews.set_index("index", inplace=True)
df_reviews.head()


# ### PAYMENTS TABLE

# In[6]:


df_payments = pd.read_sql_query('SELECT * FROM olist_order_payments_dataset', con)
df_payments.set_index("index", inplace=True)
df_payments.head()


# ### ITEMS TABLE

# In[7]:


df_items = pd.read_sql_query('SELECT * FROM olist_order_items_dataset', con)
df_items.set_index("index", inplace=True)
df_items.head()


# ### PRODUCTS TABLE

# In[8]:


df_products = pd.read_sql_query('SELECT * FROM olist_products_dataset', con)
df_products.set_index("index", inplace=True)
df_products.head()


# ### SELLERS TABLE

# In[9]:


df_sellers = pd.read_sql_query('SELECT * FROM olist_sellers_dataset', con)
df_sellers.set_index("index", inplace=True)
df_sellers.head()


# ### GEOLOCATION TABLE

# In[10]:


df_geolocation = pd.read_sql_query('SELECT * FROM olist_geolocation_dataset', con)
df_geolocation.set_index("index", inplace=True)
df_geolocation.head()


# ### PRODUCT CATEGORY TABLE

# In[11]:


df_Category = pd.read_sql_query('SELECT * FROM product_category_name_translation', con)
df_Category.set_index("index", inplace=True)
df_Category.head()


# # EXPLORATORY DATA
# 
# ### OBJECTIVE
# 
# 1. Mengetahui Product apa yang paling banyak di pesan 
# 2. Mengetahui total value dari masing-masing Product
# 3. Mengetahui Daerah dengan penjualan tertinggi

# ### Table Preparation

# ##### Checking Null (TABLE ITEMS)

# In[12]:


df_items.isna().sum()


# ##### Checking Duplicates (TABLE ITEMS)

# In[13]:


df_items[df_items.duplicated(keep=False)]


# ##### Checking Null (TABLE PRODUCTS)

# In[14]:


df_products.isna().sum()


# ##### Checking Duplicates (TABLE PRODUCTS)

# In[15]:


df_products[df_products.duplicated(keep=False)]


# ## OBJECTIVE 1 ( Mengetahui Product apa yang paling banyak di pesan )

# ##### PENGGABUNGAN DATA

# In[16]:


# Menggabungkan tabel items, products
TABLE1 = pd.merge(df_items, df_products, on="product_id", how="left")

TABLE1.head()


# In[17]:


TABLE2 = TABLE1.rename({"product_category_name":"product_category", "order_id":"order_counts"}, axis=1)
TABLE2 = TABLE2[["product_category","order_counts"]].groupby("product_category").count()
TABLE2 = TABLE2.sort_values("order_counts", ascending=False).reset_index()

TABLE2


# In[18]:


f, ax = plt.subplots(figsize=(10, 15))

sns.barplot(y="product_category", x="order_counts", data=TABLE2, color="r")
sns.set_style("whitegrid")

ax.set( ylabel="Product Category", xlabel="order", title="Data Order dari Masing-masing Product Category")

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)


# ## OBJECTIVE 2 ( Mengetahui total value dari masing-masing Product )

# ##### PENGGABUNGAN DATA

# In[19]:


TABLE3 = pd.merge(TABLE1, df_payments, on="order_id", how="left")
TABLE3


# In[20]:


TABLE4 = TABLE3.rename({"product_category_name":"product_category", "payment_value":"value"}, axis=1)
TABLE4 = TABLE4[["product_category","value"]].groupby("product_category").count()
TABLE4 = TABLE4.sort_values("value", ascending=False).reset_index()

TABLE4


# In[21]:


f, ax = plt.subplots(figsize=(10, 15))

sns.barplot(y="product_category", x="value", data=TABLE4, color="g")
sns.set_style("whitegrid")

ax.set( xlabel="value", ylabel="Product_Category", title="Data Value untuk masing-masing Product Category")

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)


# ### OBJECTIVE 3 ( Mengetahui Daerah dengan penjualan tertinggi )

# ##### PENGGABUNGAN DATA

# In[22]:


TABLE5 = pd.merge(data_order, data_customer, on="customer_id", how="left")
TABLE5


# In[23]:


TABLE6 = TABLE5.rename({"customer_state":"Daerah", "order_id":"order_counts"}, axis=1)
TABLE6 = TABLE6[["Daerah","order_counts"]].groupby("Daerah").count()
TABLE6 = TABLE6.sort_values("order_counts", ascending=False).reset_index()

TABLE6


# In[24]:


f, ax = plt.subplots(figsize=(10, 15))

sns.barplot(x="Daerah", y="order_counts", data=TABLE6, color="grey")
sns.set_style("whitegrid")

ax.set( xlabel="Daerah", ylabel="order_counts", title="Data daerah dengan penjualan paling tinggi")

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)


# In[ ]:




