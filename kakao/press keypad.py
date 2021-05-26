def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    nums = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]

    l_hand = [0, 3]
    m_hand = [0, 0]
    r_hand = [2, 3]

    for i in numbers:
        if i in nums[0]:
            answer += 'L'
            l_hand = [0, nums[0].index(i)]
        elif i in nums[2]:
            answer += 'R'
            r_hand = [2, nums[2].index(i)]
        else:
            m_hand = [1, nums[1].index(i)]
            l_dis = abs(m_hand[0] - l_hand[0]) + abs(m_hand[1] - l_hand[1])
            r_dis = abs(m_hand[0] - r_hand[0]) + abs(m_hand[1] - r_hand[1])
            if hand == "right":
                if l_dis < r_dis:
                    answer += 'L'
                    l_hand = m_hand
                else:
                    answer += 'R'
                    r_hand = m_hand
            elif hand == "left":
                if r_dis < l_dis:
                    answer += 'R'
                    r_hand = m_hand
                else:
                    answer += 'L'
                    l_hand = m_hand

    return answer