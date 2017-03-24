import random
import math


class Node:
    def __init__(self, info):  # constructor of class

        self.info = info  # information for node
        self.left = None  # left leef
        self.right = None  # right leef
        self.level = None  # level none defined

    def __str__(self):
        return str(self.info)  # return as string


class searchtree:
    def ortalama(self):
        toplam = 0
        for item in self.depth_list:
            toplam += item
        return toplam / len(self.depth_list)

    def __init__(self):  # constructor of class

        self.root = None
        self.depth_list = []

    def create(self, val):  # create binary search tree nodes

        if self.root == None:

            self.root = Node(val)
            self.depth_list.append(0)

        else:

            current = self.root
            depth = 0
            while 1:

                if val < current.info:
                    depth += 1
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        self.depth_list.append(depth)
                        break

                elif val > current.info:
                    depth += 1
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        self.depth_list.append(depth)
                        break

                else:
                    break

    def bft(self):  # Breadth-First Traversal

        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:

            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

            out.append(str(current_node.info) + " ")

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        print("".join(out))

    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print(node.info)
            self.inorder(node.right)

    def preorder(self, node):

        if node is not None:
            print(node.info)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):

        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.info)


tekrar_sayisi = input("\nTekrar sayısını girin:")
dugum_sayisi = input("\nDüğüm sayısını girin:")
ortalama_list = []
for x in range(int(tekrar_sayisi)):
    tree = searchtree()
    node_list = random.sample(range(1, 100), int(dugum_sayisi))
    for item in node_list:
        tree.create(item)
    print("AĞAÇ:")
    tree.bft()
    toplam = len(tree.depth_list)
    print("DÜĞÜM SAYISI:", toplam, "LOG DÜĞÜM SAYISI:", math.log(toplam))
    print("ORTALAMA:", tree.ortalama())
    ortalama_list.append(tree.ortalama())
toplam = 0
for item in ortalama_list:
    toplam += item
final_ortalama = toplam / len(ortalama_list)
print("FINAL ORTALAMA:", final_ortalama, "LOG DÜĞÜM SAYISI:", math.log(int(dugum_sayisi)))
