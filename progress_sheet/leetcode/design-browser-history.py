class Node:
    def __init__(self, val,next=None, prev=None):
        self.val = val
        self.next = next
        self.prev= prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=Node(homepage)

    def visit(self, url: str) -> None:
        newPage=Node(url,None,self.homepage)
        self.homepage.next=newPage
        self.homepage=self.homepage.next

    def back(self, steps: int) -> str:
        # curr=self.homepage
        i=0
        while self.homepage.prev and i<steps:
            self.homepage=self.homepage.prev
            i+=1
        return self.homepage.val
    def forward(self, steps: int) -> str:
        # curr=self.homepage
        i=0
        while self.homepage.next and i<steps:
            self.homepage=self.homepage.next
            i+=1
        return self.homepage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)