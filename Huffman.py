import functools
import heapq

z = dict(
    z1=0.26,
    z2=0.19,
    z3=0.14,
    z4=0.11,
    z5=0.1,
    z6=0.08,
    z7=0.07,
    z8=0.05
)
z2 = dict(
    z1z1=0.49,
    z1z2=0.14,
    z2z1=0.14,
    z1z3=0.07,
    z3z1=0.07,
    z2z2=0.04,
    z2z3=0.02,
    z3z2=0.02,
    z3z3=0.01
)
@functools.total_ordering
class Node:
    def __init__(self, k, v, left=None, right=None):
        # ключ, значение и ссылки налево направо
        self.k = k
        self.v = v
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.v < other.v


def huff(d):
    # из нашего дикта делаем ноды
    nodes = [Node(k, v) for k, v in d.items()]
    # структура данных - куча, бинарное сбалансированное дерево - нужна для поиска мин или макс.
    # по сути массив)
    heapq.heapify(nodes)

    # строим дерево
    while len(nodes) > 1:
        right = heapq.heappop(nodes)
        left = heapq.heappop(nodes)

        heapq.heappush(nodes, Node('', right.v + left.v, left, right))

    return to_codes(nodes[0])


def to_codes(node, prefix=""):
    result = {}

    # если есть ключ значит это конец
    if node.k:
        return {node.k: prefix}

    result.update(to_codes(node.left, prefix + '1'))
    result.update(to_codes(node.right, prefix + '0'))

    return result


huffman = huff(z)
for i in huffman:
    print(f"{i} - {huffman[i]}")

print()

huffman = huff(z2)
for i in huffman:
    print(f"{i} - {huffman[i]}")
