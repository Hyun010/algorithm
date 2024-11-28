from collections import defaultdict

def solution(enroll, referral, seller, amount):
    profit = defaultdict(int) #이익 딕셔너리
    #추천인 매핑
    referral_map = {name: ref for name, ref in zip(enroll, referral)}
    profit_per_toothbrush = 100 #이익 원가

    for s, a in zip(seller, amount):
        total_profit = a * profit_per_toothbrush #현재 총 이득
        current_seller = s #현재사람
        while current_seller != "-": #현재 이득 정산
            share = total_profit // 10 #10%
            profit[current_seller] += total_profit - share #현재사람 이득정산
            if share==0:
                break
            total_profit = share #다음 사람 정산금
            #다음 추천인
            current_seller = referral_map.get(current_seller, "-")
    return [profit[name] for name in enroll]