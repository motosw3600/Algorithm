let string = "orange purple" // erunge parplo
let vowel = "aeiou"

let values: [(Int, String)] = Array(string).enumerated()
                            .filter { vowel.contains($0.element) }
                            .map { ($0.offset, String($0.element)) }

let indexs = values.map { $0.0 }
let sValues = values.map { $0.1 }.reversed()
var dics: [Int: String] = [:]

zip(indexs, sValues).forEach { idx, val in
    dics[idx] = val
}

var result: [String] = []

Array(string).enumerated().forEach { (idx, val) in
    guard let element = dics.keys.contains(idx) ? dics[idx] : String(val) else { return }
    result.append(element)
}

print(result.joined())
