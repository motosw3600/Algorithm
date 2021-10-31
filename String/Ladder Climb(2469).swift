import Foundation

let k = Int(readLine()!)!
let n = Int(readLine()!)!

//let alpha = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
//let endIndex = alpha.index(alpha.startIndex, offsetBy: k)
//let startAlpha = String(alpha[..<endIndex])
//var start = startAlpha.map { String($0) }

let resultAlpha = readLine()!
var end = resultAlpha.map { String($0) }
var start = end.sorted()

var result = Array(repeating: "*", count: k-1)

var up: [[String]] = []
var down: [[String]] = []
var flag = true

for _ in (0..<n) {
    let row = readLine()!.map { String($0) }
    if row.contains("?") {
        flag.toggle()
    }

    if flag {
        up.append(row)
    } else {
        down.append(row)
    }
}

for data in up {
    for i in (0..<k-1) {
        if data[i] == "-" {
            start.swapAt(i, i+1)
        }
    }
}

for data in down.reversed() {
    for i in (0..<k-1) {
        if data[i] == "-" {
            end.swapAt(i, i+1)
        }
    }
}

for i in (0..<k-1) {
    if start[i] == end[i+1] && start[i+1] == end[i] {
        result[i] = "-"
        start.swapAt(i, i+1)
    }
}

if start != end {
    print(Array(repeating: "x", count: k-1).joined())
} else {
    print(result.joined())
}
