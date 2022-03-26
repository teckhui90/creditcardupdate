#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib


# In[4]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return(render_template("index.html", result1="1", result2="1", result3="1"))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




