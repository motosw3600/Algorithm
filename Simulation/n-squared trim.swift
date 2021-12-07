import Foundation

func solution(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {

    let left = Int(exactly: left)!
    let right = Int(exactly: right)!

    var result:[Int] = []
    (left..<right + 1).forEach {
        result.append($0 / n > $0 % n ? ($0 / n) + 1 : $0 % n + 1)
    }

    return result
}