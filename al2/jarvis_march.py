# Ջարվիս Մարչի ալգորիթմ
def jarvis_march(points):
    if len(points) < 3:
        return points

    hull = []
    left = min(points)
    p = left

    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            cross = (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])
            if q == p or cross < 0:
                q = r
        p = q
        if p == left:
            break

    return hull
