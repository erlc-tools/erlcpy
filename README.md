<h1 align="center">ERLC-py</h1>

<p align="center">
    <img src="https://www.codefactor.io/repository/github/erlc-tools/erlcpy/badge" alt="ERLC-py Codefactor Rating" width="100">
</p>

<h3 align="center">A python library to communicate with the PRC Private Server API</h3>
<p align="center">This is a copy of 0xRaptor/erlc but in python!</p>

<h4>Branches</h4>

- **master**: Stable code. Tested and generally known to work.
- **dev**: Probably stable. Tested, but occasionally there are issues. Beta features though.
- **nightly**: Unstable. Untested, most times unfinished features.

<h5>Setting Up</h5>

Setting up is super simple:
```py
# main.py
import erlc

client = erlc.Client(
    globalToken: str | None # Set to None if you do not have a ratelimit key
)
```

