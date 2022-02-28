from tkinter import * # tkinter의 모든 정의를 임포트한다.
import random

class DeckOfCardsGUI:
    def __init__(self):
        window = Tk() # 창을 생성한다.
        window.title("카드를 랜덤하게 뽑는다.") # 제목을 설정한다.

        self.imageList = [] # 카드의 이미지를 저장한다.
        for i in range(1, 53):
            self.imageList.append(PhotoImage(file = "image/card/"
                   + str(i) + ".gif"))

        frame = Frame(window) # 4장의 카드 라벨을 담을 수 있는 프레임을 만든다.
        frame.pack()

        self.labelList = [] # 4장의 카드 라벨 리스트
        for i in range(4):
            self.labelList.append(Label(frame,
                image = self.imageList[i]))
            self.labelList[i].pack(side = LEFT)

        Button(window, text = "섞기",
            command = self.shuffle).pack()

        window.mainloop() # 이벤트 루프를 생성한다.

    # 4장의 카드를 랜덤하게 선택한다.
    def shuffle(self):
        random.shuffle(self.imageList)
        for i in range(4):
            self.labelList[i]["image"] = self.imageList[i]

DeckOfCardsGUI() # GUI를 생성한다.
