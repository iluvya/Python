#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script tries to solve bitcoin puzzle in a random manner

https://privatekeys.pw/puzzles/bitcoin-puzzle-tx
13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so - closest unsolved puzzle
"""

from bitcoinaddress import Wallet
import random
import multiprocessing


def run():
    private_key_range_from = 2**65
    private_key_range_to = 2**66-1
    while True:
        random_key_in_range = random.randint(private_key_range_from,
                                             private_key_range_to)
        private_key = format(random_key_in_range, 'x').zfill(64)
        wallet = Wallet(private_key)
        wallet_mainnet = wallet.address.__dict__['mainnet']
        address_compressed = wallet_mainnet.__dict__['pubaddr1c']
        if "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so" == address_compressed:
            with open("key", "w") as file:
                file.write(private_key)
        else:
            pass


if __name__ == "__main__":
    for cpu in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=run).start()
