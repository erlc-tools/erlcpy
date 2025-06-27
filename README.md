<h1 align="center">ERLC-py</h1>

<h3 align="center">A python library to communicate with the PRC Private Server API*</h3>
<p align="center">This is a copy of 0xRaptor/erlc but in python!</p>

<h5>Setting Up</h5>

Setting up is super simple:
```py
# main.py
import erlc

client = erlc.Client({
    "globalToken": '< PUT YOUR GLOBAL TOKEN HERE >'
})
client.config() # You must call to save your changes.
```