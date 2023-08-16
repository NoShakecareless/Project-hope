import argparse
import sys


def parse_args():
    parse = argparse.ArgumentParser(description="Unpacking learn")
    parse.add_argument('-g', '--galleons', default=100, type=int, metavar=" ", required=True, help='number of galleons')
    parse.add_argument('-s', '--sickles', default=50, type=int, metavar=" ", help='number of sickles')
    parse.add_argument('-k', '--knuts', default=25, type=int, required=True, help='number of knuts')
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
    args = parse_args()
    print(total(args.galleons, args.sickles, args.knuts), "Knuts")
