n, m = map(int, input().split())
sample_tc = system_tc = man = 0
sam_right = sys_right = True

for i in range(n):
    sample_tc, man = map(int, input().split())
    if sample_tc != man:    
        sam_right = False
        
for j in range(m):
    system_tc, man = map(int, input().split())
    if system_tc != man:
        sys_right = False
        

if sam_right:
    if sys_right:
        print("Accepted")
    else:
        print("Why Wrong!!!")
else:
    print("Wrong Answer")
        




