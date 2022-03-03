class Node:
    def __init__(self,value,next):
        self.value = value
        self.next=next
    def printNode(self):
        print(self.value,'-',self.next)
        
class LinkedList:
    def __init__(self,a=[]):
        if a==None or a==[]:
            self.head=None
            self.tail= None
            self.size=0
        
        elif isinstance(a, list):
            self.head = None
            self.tail= None
            self.size=0
            for i in a:
                n=Node(i,None)
                if self.head is None:
                    self.head = n
                    self.tail = n
                    self.size+=1
                else:
                    self.tail.next=n
                    self.tail=n
                    self.size+=1
        else:
            self.head = None
            self.tail = None
            self.size=a.size
            n = a.head
            while n is not None:
                new = Node(n.value, None)
                if self.head == None:
                    self.head = new
                    self.tail = new
                else:
                    self.tail.next = new
                    self.tail = new
                n = n.next
        
        
    def printList(self):
        if self.size==0:
            print('Empty List')
        else:
            n=self.head
            while (n is not None):
                n.printNode()
                n=n.next
    def get_size(self):
        return self.size
    def insert(self,elem,index=None):
        if index==None:
            n=Node(elem,None)
            if self.head is None:
                self.head = n
                self.tail = n
                self.size+=1
            else:
                self.tail.next=n
                self.tail=n
                self.size+=1
        else:
            if (index<0 or index > self.size):
                raise IndexError
            n=Node(elem,None)
        
            if index==0:
                n.next=head
                head=n
            else:
                pred=self.nodeAt(index-1)
                n.next=pred.next
                pred.next= n
    def nodeAt(self,index): 
        if (index<0 or index > self.size):
            return None
        n=self.head
        for i in range(index):
            n=n.next
        return n
    def remove(self, deleteKey):
        node = self.head
        while node.value is not deleteKey:
            node = node.next
        node.value = node.next.value
        node.next = node.next.next
        self.size-=1
        return deleteKey
    def clear(self):
        self.size=0
        while (self.head != None):
            temp=self.head
            self.head = self.head.next
            temp=None
        print("All nodes are cleared.")    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    def oddsOut(self):
        n=self.head
        while n is not None:
            if n.value%2!=0:
                self.remove(n.value)
            else:
                n=n.next
    def elementFind(self,key):
        n=self.head
        while n is not None:
            if n.value==key:
                return True
    
            n=n.next
        return False
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
    def reverseRecursive(self,head):
        if (head==None or head.next==None):
            return head
        rests=self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None

        return rests
    def listSort(self):
        n=self.head
        i=n
        while i is not None:
            j=i.next
            while j is not None:
                if i.value>j.value:
                    i.value,j.value=j.value,i.value
                j=j.next
            i=i.next
    def listSum(self):
        n=self.head
        s=0
        while n is not None:
            s+=n.value
            n=n.next
        return s
    
    def rotate(self,direction, k):
        if direction == 'left':
            k=self.get_size()-k
        if k == 0:  
            return 
        current = self.head 
        count = 1 
        while(count <k and current is not None): 
            current = current.next
            count += 1
        if current is None: 
            return
        kthNode = current  
        while(current.next is not None): 
            current = current.next
        current.next = self.head 
        self.head = kthNode.next
        kthNode.next = None
    def getCountRec(self, node): 
        if node==None: 
            return 0
        else: 
            return 1 + self.getCountRec(node.next) 

    def getCount(self): 
        return self.getCountRec(self.head) 
