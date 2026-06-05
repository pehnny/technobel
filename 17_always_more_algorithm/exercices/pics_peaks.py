def pick_peaks(arr: list[int]) -> dict[str, list[int]]:
    """Three pointers exploration. 
    Triangulate the position of a peak.
    """
    solution: dict[str, list[int]] = {"pos": [], "peaks": []}
    if len(arr) < 3:
        return solution
    
    low, mid, high = 0, 1, 2
    
    for i in range(2, len(arr)-1):
        ldy = arr[mid] - arr[low]
        rdy = arr[high] - arr[mid]
        if rdy > 0:
            low = i-1
            mid = i
            high = i+1
        elif rdy == 0:
            if ldy <= 0:
                low = i-1
                mid = i
                high = i+1
            else:
                high = i+1
        else:
            if ldy <= 0:
                low = i-1
                mid = i
                high = i+1
            else:
                solution["pos"].append(mid)
                solution["peaks"].append(arr[mid])
                low = i-1
                mid = i
                high = i+1
        
    high = len(arr)-1
    ldy = arr[mid] - arr[low]
    rdy = arr[high] - arr[mid]
    if ldy > 0 and rdy < 0:
        solution["pos"].append(mid)
        solution["peaks"].append(arr[mid])
    return solution

def pick_peaks_simplified(arr: list[int]) -> dict[str, list[int]]:
    """Simplified version with one pointer and a memory.
    Plateau are ignored automatically.
    Pointer moves when the function is rising only.
    Peak is saved when the function is decreasing, signaling a local maximum.
    """
    pos: list[int] = []
    peak = -1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            peak = i
        elif arr[i] < arr[i-1] and peak >= 0:
            pos.append(peak)
            peak = -1
    return {"pos": pos, "peaks": [arr[i] for i in pos]}