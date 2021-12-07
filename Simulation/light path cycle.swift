import Foundation

func solution(_ grid:[String]) -> [Int] {
    let direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    let grids = grid.map { $0.map { String($0) } }
    var visited = Array(repeating: Array(repeating: Array(repeating: false, count: 4), count: grids[0].count), count: grid.count)
    var results: [Int] = []

    for i in (0..<grid.count) {
        for j in (0..<grids[0].count) {
            for k in (0..<4) {
                if visited[i][j][k] { continue }
                var currDir = k
                var nx = i
                var ny = j
                var cnt = 0

                while !visited[nx][ny][currDir] {
                    visited[nx][ny][currDir] = true
                    cnt += 1

                    nx = nx + direction[currDir].0
                    if nx >= grid.count {
                        nx = 0
                    } else if nx < 0 {
                        nx = grid.count - 1
                    }

                    ny = (ny + direction[currDir].1)
                    if ny >= grids[0].count {
                        ny = 0
                    } else if ny < 0 {
                        ny = grids[0].count - 1
                    }

                    if grids[nx][ny] == "R" {
                        currDir = (currDir + 1) % 4
                    }
                    else if grids[nx][ny] == "L" {
                        currDir = (currDir + 3) % 4
                    }
                    if visited[nx][ny][currDir] {
                        if nx == i && ny == j && currDir == k {
                            results.append(cnt)
                        }
                    }
                }
            }
        }
    }

    return results.sorted()
}