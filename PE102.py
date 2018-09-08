raw_text = [list(map(int, i.split(','))) for i in open('p102_triangles.txt').readlines()]
triangles = [[(i[0], i[1]), (i[2], i[3]), (i[4], i[5])] for i in raw_text]


def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1]) < 0


def origin_in_triangle(p1, p2, p3):
    origin = (0, 0)
    b1 = sign(origin, p1, p2)
    b2 = sign(origin, p2, p3)
    b3 = sign(origin, p3, p1)

    return (b1 == b2) and (b2 == b3)


count = 0
for t in triangles:
    if origin_in_triangle(t[0], t[1], t[2]):
        count += 1

print(count)
