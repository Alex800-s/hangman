class Square():
    square_list = []

    def __init__(self, x, y, z, q):
        self.side_x = x
        self.side_y = y
        self.side_z = z
        self.side_q = q
        self.square_list.append((self.side_x,
                                 self.side_y,
                                 self.side_z,
                                 self.side_q))
    def sq(self):
        return self.side_x,self.side_x,self.side_x,self.side_x
    def tr(self):
        return self.side_x,self.side_y,self.side_x,self.side_y

squar = Square(12,23,4,5)
print("Стороны квадрата равны:",squar.sq())
print("Стороны прямоугольника равны:",squar.tr())


