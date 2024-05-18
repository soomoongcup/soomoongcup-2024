from __future__ import annotations

from typing import List, Iterator


def ipv4_to_bits(ipv4: str) -> str:
    b = 0
    octets = ipv4.split('.')
    for p in map(int, octets):
        b = (b << 8) | p
    return f'{b:032b}'


def bits_to_ipv4(bits: str) -> str:
    b = int(bits, base=2)
    octets_rev = []
    for i in range(4):
        octets_rev.append(f'{b & 0xFF}')
        b >>= 8
    return '.'.join(reversed(octets_rev))


class Node:
    def __init__(self) -> None:
        self.is_endpoint = False
        self.lnode = None
        self.rnode = None

    def add_address(self, address: str):
        ipv4, sbm = address.split('/')
        bits = ipv4_to_bits(ipv4)[:int(sbm)]
        self._add(bits)

    def _add(self, bits: str) -> bool:
        if not bits:
            self.is_endpoint = True
            self.lnode = None
            self.rnode = None
            return

        if self.lnode is None:
            self.lnode = Node()
        if self.rnode is None:
            self.rnode = Node()

        if bits[0] == '0':
            self.lnode._add(bits[1:])
        if bits[0] == '1':
            self.rnode._add(bits[1:])

        if self.lnode.is_endpoint and self.rnode.is_endpoint:
            self.is_endpoint = True

    def search(self, bits='') -> Iterator[str]:
        # dfs
        if self.is_endpoint:
            sbm = len(bits)
            yield bits_to_ipv4(bits + '0'*(32-sbm)) + '/' + str(sbm)
            return
        if self.lnode is not None:
            for address in self.lnode.search(bits+'0'):
                yield address
        if self.rnode is not None:
            for address in self.rnode.search(bits+'1'):
                yield address


def solve(addresses: List[str]) -> List[str]:
    root = Node()
    for address in addresses:
        root.add_address(address)
    return [*root.search()]


if __name__ == '__main__':
    from pathlib import Path

    DIR_PATH = Path(__file__).parent

    for TESTCASE_ID in ('1', '2'):
        DATA_PATH = DIR_PATH / 'data' / 'secret' / f'subtask{TESTCASE_ID}'
        with open(DATA_PATH / '1.in', 'r') as fin:
            T = int(fin.readline())
            for t in range(T):
                N = int(fin.readline())
                ADDRESS = []
                for i in range(N):
                    ADDRESS.append(fin.readline())
                OUTPUT = solve(ADDRESS)
                print(OUTPUT[:10])
