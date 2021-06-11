def solution(m, musicinfos):
    answer = [0, "(None)"]
    m = replacing_str(m)
    print(m)
    for val in musicinfos:
        music = val.split(",")
        minute = (int(music[1].split(":")[0]) - int(music[0].split(":")[0])) * 60
        second = int(music[1].split(":")[1]) - int(music[0].split(":")[1])
        time = minute + second

        m_info = replacing_str(music[3])
        length = len(m_info)
        if time < length:
            info = m_info[:time]
        else:
            p = (time - length) // length
            n = (time - length) % length
            info = m_info + p * m_info + m_info[:n]

        if m in info and answer[0] < time:
            answer = [time, music[2]]

    return answer[-1]

def replacing_str(string):
    encode = ["C#", "D#", "F#", "G#", "A#"]
    decode = ['c', 'd', 'f', 'g', 'a']

    for en, de in zip(encode, decode):
        if en in string:
            string = string.replace(en, de)

    return string
