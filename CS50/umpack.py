import argparse
import sys


def parse_args():
    parse = argparse.ArgumentParser(description="Unpacking learn")
    parse.add_argument('galleons', type=int, help='number of galleons')
    parse.add_argument('sickles', type=int, help='number of sickles')
    parse.add_argument('knuts', type=int, help='number of knuts')
    args = parse.parse_args()   # 解析参数对象获得解析对象
    return args


def total(galleons, sickles, knuts):
    return (galleons*17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
print(total(*coins), "Knuts")
"""
unpacking
    *
    total(coins) can not pass
    but with '*' pass!
"""

if __name__ == "__main__":
    # args = parse_args()
    if len(sys.argv) < 4:
        raise ValueError("Plz input 3 elem!")
    galleons = int(sys.argv[1])
    sickles = int(sys.argv[2])
    knuts = int(sys.argv[3])
    print(total(galleons, sickles, knuts), "Knuts")
