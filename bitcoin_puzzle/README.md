# Bitcoin Puzzle

In 2015, in order to show the hugeness of the private key space (or maybe just for fun), someone created a "puzzle" where he chose keys in a certain smaller space and sent increasing amounts to each of those keys like this:

20 ≤ random key < 21 — 0.001 BTC <br>
21 ≤ random key < 22 — 0.002 BTC <br>
23 ≤ random key < 23 — 0.003 BTC <br>
... <br>
2255 ≤ random key < 2256 — 0.256 BTC <br>
(total 32.896 BTC)

As of October 2022, first 65, #70, #75, #80, #85, #90, #95, #100, #105, #110, #115 addresses have been cracked. People are still trying to crack #66 address, which requires scanning 36,893,488,147,419,103,231 keys.

This python script tries to guess #66 address in a random manner.
