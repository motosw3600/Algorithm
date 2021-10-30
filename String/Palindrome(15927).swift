import Foundation

let string = readLine()!.map { String($0) }
let size = string.count
var answer = false
var isPalindrome = false

for i in (0..<size / 2) {
    if string[i] != string[size - 1 - i] {
        answer = true
        break
    } else if (string[i] != string[i+1]) {
        isPalindrome = true
    }
}

if answer {
    print(size)
} else {
    if isPalindrome {
        print(size - 1)
    } else {
        print(-1)
    }
}
