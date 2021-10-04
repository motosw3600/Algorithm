import Foundation

let info = readLine()!.split(separator: " ").map{ Int($0)! }
let N = info[0]
let M = info[1]
let K = info[2]
var maps: [[[Fire]?]] = Array(repeating: Array(repeating: nil, count: N), count: N)

for _ in (0..<M) {
    let fireball = readLine()!.split(separator: " ").map{ Int($0)! }
    maps[fireball[0] - 1][fireball[1] - 1] = [Fire(m: fireball[2], s: fireball[3], d: fireball[4])]
}

for _ in (0..<K) {
    var tempMap: [[[Fire]?]] = Array(repeating: Array(repeating: nil, count: N), count: N)
    var overlapPoint: [(Int, Int)] = []
    for x in (0..<N) {
        for y in (0..<N) {
            guard let fireArr = maps[x][y] else { continue }
            for i in (0..<fireArr.count) {
                let fire = fireArr[i]
                let direct = move(direct: fire.d)
                var dx = (x + fire.s * direct.0) % N
                var dy = (y + fire.s * direct.1) % N
                if dx < 0 {
                    dx += N
                }
                if dy < 0 {
                    dy += N
                }
                if tempMap[dx][dy] != nil {
                    tempMap[dx][dy]!.append(fire)
                    overlapPoint.append((dx, dy))
                } else {
                    tempMap[dx][dy] = [fire]
                }
            }
        }
    }
    maps = tempMap
    if overlapPoint.count > 0 {
        maps = divideFireBall(maps: maps, points: overlapPoint)
    }
}

let filterMap = maps.map{ $0.compactMap{ $0?.reduce(0){ $0 + $1.m } } }.filter{ $0.count > 0 }
let result = filterMap.map{ $0.reduce(0){ $0 + $1 } }.reduce(0){ $0 + $1 }
print(result)

func divideFireBall(maps: [[[Fire]?]], points: [(Int, Int)]) -> [[[Fire]?]] {
    var divideMap: [[[Fire]?]] = maps

    for point in points {
        guard let map = maps[point.0][point.1] else { break }
        let fireCount = map.count
        let fireMass = map.reduce(0){ $0 + $1.m } / 5
        if fireMass == 0 {
            divideMap[point.0][point.1] = nil
        } else {
            let fireSpeed = map.reduce(0){ $0 + $1.s } / fireCount
            let filterdFire = map.filter{ $0.d % 2 == 0 }
            if filterdFire.count == 0 || filterdFire.count == fireCount {
                divideMap[point.0][point.1] = [0, 2, 4, 6].map{ Fire(m: fireMass, s: fireSpeed, d: $0) }
            }else{
                divideMap[point.0][point.1] = [1, 3, 5, 7].map{ Fire(m: fireMass, s: fireSpeed, d: $0) }
            }
        }
    }
    return divideMap
}

struct Fire {
    var m: Int
    var s: Int
    var d: Int
}


func move(direct: Int) -> (Int, Int) {
    switch direct{
    case 0:
        return (-1, 0)
    case 1:
        return (-1, 1)
    case 2:
        return (0, 1)
    case 3:
        return (1, 1)
    case 4:
        return (1, 0)
    case 5:
        return (1, -1)
    case 6:
        return (0, -1)
    case 7:
        return (-1, -1)
    default:
        return (0, 0)
    }
}
