#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import library Flask
from flask import Flask, request
from flask_restful import Resource, Api


# In[2]:


# Masukan Data
nama = input("Masukan Nama: ")
email = input("Masukan Email: ")
tgl_lahir = input("Masukan tanggal lahir (DD-MM-YYYY): ")

# Pengolahan tanggal lahir menjadi umur
from datetime import datetime
tgl_lahir = datetime.strptime(tgl_lahir, '%d-%m-%Y')
sekarang = datetime.now()
usia_tahun = sekarang.year-tgl_lahir.year
usia_bulan = sekarang.month-tgl_lahir.month

# Keluaran Data
print ("========================================================")
print ("Nama Anda : "+ nama)
print ("Email Anda : "+ email)
usia ="%d Tahun %d Bulan" % (usia_tahun,usia_bulan)
print("Usia Anda: "+ usia)


# In[3]:


# Inisiasi object
app = Flask(__name__)
api = Api (app)


# In[4]:


identitas={'nama:':nama, 'email:':email,'usia': usia}
identitas


# In[5]:


# Membuat class resource
class ContohResource(Resource):
    # metode get
    def get(self):
        return identitas
    # metode post
    def post(self):
        request.post(data=identitas)
        response = {"msg" : "Data berhasil dimasukan"}
        return response


# In[ ]:


# Setup resource
api.add_resource(ContohResource,"/soal/pretest", methods=["GET","POST"])
if __name__ == "__main__":
    app.run(debug=False, port=5000)

