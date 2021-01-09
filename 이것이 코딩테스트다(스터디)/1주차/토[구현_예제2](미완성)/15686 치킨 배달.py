"""
모든 집과 모든 치킨집의 치킨 거리를 구한다.
모든 집과 임의의 치킨집의 거리를 더 하면 해당 치킨 집의 총 치킨 거리를 알 수 있다.

치킨 거리가 1인 집의 개수
치킨 거리가 2인 집의 개수
치킨 거리가 3인 집의 개수
치킨 거리가 4인 집의 개수
치킨 거리가 5인 집의 개

"""
n , m = map(int, input().split())

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

