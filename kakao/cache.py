from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        if city.upper() in cache:
            answer += 1
            cache.remove(city.upper())
        else:
            answer += 5
        cache.append(city.upper())

    return answer