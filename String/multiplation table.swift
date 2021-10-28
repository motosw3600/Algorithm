import Foundation

let multiplation = (1..<10).map { s1 in
    (1..<10).map { s2 in
        "\(s1) * \(s2) = \(s1 * s2)\n"
    }
}

print(multiplation.joined().joined())