import operator

# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3


'''
genres : [classic, pop, classic, classic, pop]
plays  : [500,     600,  150,     800,   2500]
retrun : [4,       1,    3,       0]
'''

'''
tmp = sorted(tmp, key = lambda e: (e[2], -e[0]), reverse=True)[:2]
'''

def solution(genres, plays):
    answer = []
    rank_list = {}
    info_list = []

    for genre, play in zip(genres, plays):
        if not genre in rank_list:
            rank_list[genre] = 0
            pass
        rank_list[genre] += play
    rank_list = sorted(rank_list.items(), key=lambda item:item[1], reverse=True)
    # 각 정보에 인덱스 추가 -> info_list
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        info_list.append((idx, genre, play))

    tmp = []
    for rank in list(rank_list):
        #print(rank[0]) # pop - classic - wow / rank순으로
        for info in info_list:
            if info[1] == rank[0]:
                tmp.append(info)
        if len(tmp) >= 2:
            tmp = sorted(tmp, key=lambda t:t[2], reverse=True)[:2]
        for (a, _, _) in tmp:
            answer.append(a)
        tmp = []
    return answer

if __name__ == "__main__":
    input_genres = ["classic", "pop", "classic", "classic", "pop", "wow"]
    input_plays = [500, 600, 150, 800, 2500, 100]

    a = solution(input_genres, input_plays)
    print("answer : ", a)