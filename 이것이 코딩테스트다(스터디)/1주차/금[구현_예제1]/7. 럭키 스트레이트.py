"""
반으로 나눠서 더한 후 비교
"""
n = list(map(int, input()))
mid = len(n)//2
print("LUCKY" if sum(n[:mid]) == sum(n[mid:]) else "READY")
