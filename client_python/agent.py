class agent:
    def _init_(self, id: int, value: float, src: int, dest: int, pos: tuple):
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.pos = pos

    def getId(self):
        return self.id

    def setId(self, i):
        self.id = i

    def getValue(self):
        return self.value

    def setEdge(self, v):
        self.value = v

    def getSrc(self):
        return self.src

    def setSrc(self, s):
        self.src = s

    def getDest(self):
        return self.dest

    def setDest(self, d):
        self.dest = d

    def getPos(self):
        return self.pos

    def setPos(self, p):
        self.pos = p
