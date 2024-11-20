#강도에 따른 누적값
def chunk_hardness(chunk):
    return sum(25 if m == "diamond" else 5 if m == "iron" else 1 for m in chunk)

def solution(picks, minerals):
    #곡괭이:광물:피로도 매핑
    fatigue_costs = {
        "diamond": {"diamond": 1, "iron": 1, "stone": 1},
        "iron": {"diamond": 5, "iron": 1, "stone": 1},
        "stone": {"diamond": 25, "iron": 5, "stone": 1},
    }
    
    # Step 1: 광물을 5개씩 묶음으로 나누기
    total_pick=sum(picks)
    chunks = [minerals[i:i + 5] for i in range(0, len(minerals),5)][:total_pick]
    chunks.sort(key=chunk_hardness, reverse=True) #역순 처리(최소의 조건을 위해)
    answer = 0
    for chunk in chunks:
        #곡괭이 선택(다이아-철-돌)->최소를 위해
        if picks[0] > 0: #다이아몬드 곡괭이
            pickaxe = "diamond"
            picks[0] -= 1
        elif picks[1] > 0: #철 곡괭이
            pickaxe = "iron"
            picks[1] -= 1
        elif picks[2] > 0: #돌 곡괭이
            pickaxe = "stone"
            picks[2] -= 1
        else: #곡괭이X
            break 
        for mineral in chunk: #피로도 계산
            answer += fatigue_costs[pickaxe][mineral]
    return answer