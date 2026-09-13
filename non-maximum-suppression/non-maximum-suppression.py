def nms(boxes: list, scores: list, iou_threshold: float) -> list:
    """
    Returns a list of retained indices.
    """
    # Write code here

    def iou(a, b):
        xL = max(a[0], b[0])
        xR = min(a[2], b[2])
        yT = max(a[1], b[1])
        yB = min(a[3], b[3])

        inter = max(0, xR - xL) * max(0, yB - yT)
            
        area_a = (a[2] - a[0]) * (a[3] - a[1])
        area_b = (b[2] - b[0]) * (b[3] - b[1])
    
        iou = inter / (area_a + area_b - inter)
        return iou
    
    
    if not boxes:
        return []

    sort = sorted(range(len(boxes)), key=lambda i: scores[i], reverse=True)

    res = []
    while sort:
        current = sort.pop(0)
        res.append(current)

        sort = [i for i in sort if iou(boxes[current], boxes[i]) < iou_threshold]
    return res