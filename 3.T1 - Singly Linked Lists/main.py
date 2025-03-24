from Node import Node
from LinkedList import LinkedList


num_list = LinkedList()

node_a = Node(31)
node_b = Node(62)
node_c = Node(11)
node_d = Node(89)
node_e = Node(81)
node_f = Node(10)

num_list.append(node_b)   
num_list.append(node_c)   
num_list.append(node_e)   

num_list.prepend(node_a)  

num_list.insert_after(node_c, node_d)  
num_list.insert_after(node_e, node_f)  

# Output list
print('List after adding nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

num_list.remove_after(node_e)   
num_list.remove_after(None)     


# Output final list
print('List after removing nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()
