t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    
    x = list(map(int, input().split()))
    
    minval = min(abs(s-x[0]), abs(s-x[n-1]));
    maxval = max(abs(s-x[0]), abs(s-x[n-1]));
    
    if (s <= x[n-1] and s>= x[0]):
        min_steps = 2*minval + maxval
    elif (s < x[0] or s > x[n-1]):
        min_steps = maxval
    
    print(min_steps)