from sys import stdin

n = int(stdin.readline())
tree = {}

#init
for _ in range(n):
	node,leftNode,rightNode = stdin.readline().rstrip().split()
	tree[node]=[leftNode,rightNode]
#Root,Left,Right
def preorder(tree,node):
	print(node,end='')
	if tree[node][0] != '.':#left
		preorder(tree,tree[node][0])
	if tree[node][1] != '.':#right
		preorder(tree,tree[node][1])
#Left,Root,Right
def inorder(tree,node):
	if tree[node][0] != '.':#left
		inorder(tree,tree[node][0])
	print(node,end='')
	if tree[node][1] != '.':#right
		inorder(tree,tree[node][1])
#Left,Right,Root
def postorder(tree,node):
	if tree[node][0] != '.':#left
		postorder(tree,tree[node][0])
	if tree[node][1] != '.':#right
		postorder(tree,tree[node][1])
	print(node,end='')
	
preorder(tree,'A')
print()
inorder(tree,'A')
print()
postorder(tree,'A')