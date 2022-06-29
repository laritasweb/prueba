#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cryptography.x509 as cripto


# In[16]:


dir(cripto)


# In[18]:


with open("certificate.cer", "rb") as data:
    byte = data.read()

print(byte)


# In[93]:


from cryptography.hazmat.primitives import serialization


# In[24]:


dir(cert)


# In[19]:


cert= cripto.load_der_x509_certificate(byte)


# In[140]:


cert.subject


# In[135]:


dir(cert.subject)


# In[162]:


for x in cert.subject.__dict__['_attributes']:
    print(x.rfc4514_string().split("=")[1])


# In[163]:


cert.subject.__dict__['_attributes']


# In[98]:


cers=cert.public_key().public_bytes(

   encoding=serialization.Encoding.PEM,

   format=serialization.PublicFormat.SubjectPublicKeyInfo

)


# In[30]:


cert.public_key


# In[31]:


cert.signature


# In[34]:


cert.signature_algorithm_oid


# In[35]:


cert.signature_hash_algorithm


# In[37]:


import base64 as base


# In[54]:


from cryptography.hazmat.primitives.serialization import load_der_private_key 


# In[43]:


with open("llave.key", "rb") as data:
    llave = data.read()

print(llave)


# In[57]:


pss = bytes("Cub34ndC0l0r$",'UTF-8')


# In[59]:





# In[60]:


keys = load_der_private_key(llave, pss)


# In[88]:


keys


# In[80]:


keys


# In[99]:


keyf=keys.public_key().public_bytes(

   encoding=serialization.Encoding.PEM,

   format=serialization.PublicFormat.SubjectPublicKeyInfo

)


# In[100]:


print(cers == keyf )


# In[101]:


display(cers)
display(keyf)

