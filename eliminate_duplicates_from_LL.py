from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def removeDuplicates(head) :
    tempHead = head 
    if head is None :
        return None
    while tempHead.next is not None :
        currData = tempHead.data
        nextNode = tempHead.next 
        nextNodeData = nextNode.data
        if currData == nextNodeData :
            tempHead.next = nextNode.next 
        else :
            tempHead = tempHead.next
    return head


def takeInput() :
    head = None
    tail = None

    datas = list(map(int, input().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(input())

while t > 0 :
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1
