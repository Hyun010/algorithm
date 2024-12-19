def generate_combinations(n, discounts):
    if n == 0:
        return [[]] #기본 경우: 빈 리스트 반환
    else:
        combinations = []
        for discount in discounts:
            for combo in generate_combinations(n - 1, discounts):
                combinations.append([discount] + combo) #현재 할인율 추가
        return combinations

def solution(users, emoticons):
    rates = [10, 20, 30, 40] #할인율 목록
    max_users = 0 #최대 가입자 수
    max_revenue = 0 #최대 매출액
    #모든 가능한 할인율 조합 생성
    discount_combinations = generate_combinations(len(emoticons), rates)
    for discounts in discount_combinations:
        total_users = 0 #현재 할인율 조합에서 가입한 사용자 수
        total_revenue = 0 #현재 할인율 조합에서의 총 매출액
        for user in users:
            rate, price_limit = user #사용자의 할인 기준과 가격 한도
            total_cost = 0 #이모티콘 구매 비용
            for i, emoticon_price in enumerate(emoticons):
                #현재 할인율을 적용한 가격
                discounted_price = emoticon_price * (100 - discounts[i]) / 100
                #사용자가 구매할 수 있는 경우
                if discounts[i] >= rate:
                    total_cost += discounted_price
            #사용자가 이모티콘 플러스 서비스에 가입하는지 확인
            if total_cost >= price_limit:
                total_users += 1 #가입자 수 증가
            else:
                total_revenue += total_cost #매출액 증가
        #최대 가입자 수와 매출액 업데이트
        if total_users > max_users or (total_users == max_users and total_revenue > max_revenue):
            max_users = total_users
            max_revenue = total_revenue

    return [max_users, max_revenue]