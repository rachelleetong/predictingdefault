#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib


# In[2]:


#Flask (backend)
from flask import Flask
app = Flask(__name__)
from flask import request, render_template

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        model=joblib.load("CreditDefault")
#normalising the inputs
        pred=model.predict([[((float(income)-45136.87597485758)/14423.382398409489),
                             ((float(age)-34.795949606582)/12.838181998141051),
                             ((float(loan)-5591.986694851936)/3174.059368326566)]])
        print(pred)
        s="The predicted default is: " + str(pred[0])
        return(render_template("index.html", default = s))
    else:
        return(render_template("index.html", default = "Predict Default"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




