def fun_dist_bottom(seg1:ImageSegment, seg:ImageSegment):
    b = seg1.y_bottom_right # < t
    t = seg.y_top_left
    if seg1.x_bottom_right < seg.x_top_left or seg.x_bottom_right < seg1.x_top_left:
        return np.inf
    if b >= t:
        return np.inf
    else:
        return t-b
        
    
    
dists_bottom = []
for j, seg1 in enumerate(segments):
    dist_bottom = [fun_dist_bottom(seg1, seg) for seg in segments]
    if min(dist_bottom) == np.inf:
        continue
    k = np.argmin(dist_bottom)
    
    dists_bottom.append((j, k))

dists_top = [(d[1], d[0]) for d in dists_bottom]
