# 한 팩의 카드를 생성한다.
deck = [x for x in range(0, 52)]

# 종류와 순위 리스트를 생성한다.
suits = ["스페이드", "하트", "다이아몬드", "클로버"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
      "10", "J", "Q", "K"]

# 카드를 섞는다.
import random
random.shuffle(deck)

# 처음 4장의 카드를 출력한다.
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("카드 번호", deck[i], "은/는",  suit, rank, "입니다.")
