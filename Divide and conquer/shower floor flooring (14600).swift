import Foundation

infix operator **

func **(lhs: Int, rhs: Int) -> Int {
    var n = 1
    for _ in (0..<rhs) {
        n *= lhs
    }
    return n
}

func check(size: Int, x: Int, y: Int) -> Bool {
    for i in (x..<x+size) {
        for j in (y..<y+size) {
            if shower[i][j] != 0 {
                return false
            }
        }
    }
    return true
}

func search(size: Int, x: Int, y: Int) {
    num += 1
    let dSize = size / 2
    if check(size: dSize, x: x, y: y) {
        shower[x+dSize-1][y+dSize-1] = num
    }
    if check(size: dSize, x: x, y: y+dSize) {
        shower[x+dSize-1][y+dSize] = num
    }
    if check(size: dSize, x: x+dSize, y: y) {
        shower[x+dSize][y+dSize-1] = num
    }
    if check(size: dSize, x: x+dSize, y: y+dSize) {
        shower[x+dSize][y+dSize] = num
    }
    if size == 2 { return }
    search(size: dSize, x: x, y: y)
    search(size: dSize, x: x+dSize, y: y)
    search(size: dSize, x: x, y: y+dSize)
    search(size: dSize, x: x+dSize, y: y+dSize)
}

let k = Int(readLine()!)!
let waterspout = readLine()!.split(separator: " ").map{ Int($0)! }
let size = 2 ** k
var shower = Array(repeating: Array(repeating: 0, count: size), count: size)
var num = 0

// 배구수 위치 계산
let x = size - waterspout[1]
let y = waterspout[0] - 1
shower[x][y] = -1

// 탐색
search(size: size, x: 0, y: 0)

// 출력
for i in (0..<size) {
    print(shower[i].map{ String($0) }.joined(separator: " "))
}
