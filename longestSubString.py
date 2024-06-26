
from collections import deque

def main():
    a = "abcabcbb"   
    result = lengthOfLongestSubstring(a)
    print(result) 
    
def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    q = deque()
    for c in s:
        if c in q:
            while q.popleft() != c:
                pass
        q.append(c)
        res = max(res, len(q))
        
    return res
    
    
if __name__ == "__main__":
    main()