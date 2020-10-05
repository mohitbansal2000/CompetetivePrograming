n = int(input())
b,h=map(int,input().split())
a = [int(x) for x in input().split()]
con=10**9+7
s1=sum(a)
s1=s1*b*h
def max_rect(bar):  
    stack = list() 
    max_area = 0 
    index = 0
    while index < len(bar): 
        if (not stack) or (bar[stack[-1]] <= bar[index]): 
            stack.append(index) 
            index += 1
  
        else:             
            top_of_stack = stack.pop() 
  
            area = (bar[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index))
            max_area = max(max_area, area) 
  
    while stack: 
          
        top_of_stack = stack.pop() 
  
        area = (bar[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
   
        max_area = max(max_area, area)
        
    return max_area*b*h

print((s1%con-max_rect(a)%con)%con)

"""
7

1 1

6 7 3 4 5 1 3

14
"""