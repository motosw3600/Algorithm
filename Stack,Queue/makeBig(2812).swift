import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let K = input[1]

let num = readLine()!
var stack: [String] = []

for (idx, s) in num.enumerated() {
    while stack.count > 0 {
        if stack.count + N - idx - 1 >= N - K {
            if stack.count > 0 && Int(stack.last!)! < Int(String(s))! {
                stack.removeLast()
            } else {
                break
            }
        } else {
            break
        }
    }
    if stack.count < N - K {
        stack.append(String(s))
    }
}

print(stack.joined())
