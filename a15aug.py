n=int(input())
l1=[n for i in range(n)]
for i in range(n):
    a = input().split()
    for x in range(n):
        if a[x] == "C" :
            l1[x]-=1

def max_sq(cube):  
    stack = list()
    max_area = 0 
    index = 0
    while index < len(cube): 
        if (not stack) or (cube[stack[-1]] <= cube[index]):
            
            stack.append(index) 
            index += 1
        else:             
            top_of_stack = stack.pop() 
  
            area = (cube[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index))
            max_area = max(max_area, area) 
    while stack: 
        top_of_stack = stack.pop() 
  
        area = (cube[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
        max_area = max(max_area, area)
    return int(max_area**0.5)

print(max_sq(l1))
