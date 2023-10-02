class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        ca = 0
        cb = 0
        for i in range(len(colors)-2):
            if colors[i] == colors[i+1] == colors[i+2] == "A":
                ca+=1
            if colors[i] == colors[i+1] == colors[i+2] == "B":
                cb+=1
        print(ca,cb)
        if ca>cb:
            return True
        return False
        