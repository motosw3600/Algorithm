import Foundation

let T = Int(readLine()!)!

func postOrder(root: Int, s: Int, e: Int, preOrder: [Int], inOrder: [Int]) {
    for i in (s..<e) {
        if inOrder[i] == preOrder[root] {
            postOrder(root: root+1, s: s, e: i, preOrder: preOrder, inOrder: inOrder)
            postOrder(root: root+i-s+1, s: i+1, e: e, preOrder: preOrder, inOrder: inOrder)
            print(preOrder[root], terminator: " ")
        }
    }
}

for _ in (0..<T) {
    let n = Int(readLine()!)!
    let preOrder = readLine()!.split(separator: " ").map{ Int($0)! }
    let inOrder = readLine()!.split(separator: " ").map{ Int($0)! }
    postOrder(root: 0, s: 0, e: n, preOrder: preOrder, inOrder: inOrder)
    print("")
}
