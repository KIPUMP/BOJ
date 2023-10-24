class Baseball:
    def __init__(self):
        self.base1 = False
        self.base2 = False
        self.base3 = False
        self.score = 0
        self.ballcount = 0

    def oneCount(self, number):
        if number == 1:  # 볼인 경우
            if self.ballcount == 3:
                if not self.base1:
                    self.base1 = True
                    self.ballcount = 0
                elif not self.base2:
                    self.base2 = True
                    self.ballcount = 0
                elif not self.base3:
                    self.base3 = True
                    self.ballcount = 0
                else:
                    self.ballcount = 0
                    self.score += 1
            else:
                self.ballcount += 1
        elif number == 2:  # 몸에 맞는 공인 경우
            if not self.base1:
                self.base1 = True
                self.ballcount = 0
            elif not self.base2:
                self.base2 = True
                self.ballcount = 0
            elif not self.base3:
                self.base3 = True
                self.ballcount = 0
            else:
                self.ballcount = 0
                self.score += 1
        elif number == 3:  # 폭투인 경우
            if self.ballcount == 3:  # 폭투와 볼넷이 겹칠 때
                if self.base3:
                    self.base3 = False
                    self.score += 1
                if self.base2:
                    self.base2 = False
                    self.base3 = True
                if self.base1:
                    self.base1 = False
                    self.base2 = True
                self.ballcount = 0
                self.base1 = True
            else:
                if self.base3:
                    self.base3 = False
                    self.score += 1
                if self.base2:
                    self.base2 = False
                    self.base3 = True
                if self.base1:
                    self.base1 = False
                    self.base2 = True
                self.ballcount += 1

if __name__ == "__main__":
    N = int(input())
    baseball = Baseball()
    game = list(map(int,input().split()))
    for i in range(N):
        baseball.oneCount(game[i])

    print(baseball.score)
