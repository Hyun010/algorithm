from collections import defaultdict

def solution(genres, plays):
    genre_play_count = defaultdict(int) # 장르별 재생 횟수를 저장할 딕셔너리
    genre_songs = defaultdict(list)  # 각 장르별 노래 정보를 저장할 딕셔너리
    answer = []
    
    # 장르와 재생 횟수를 기반으로 데이터 구조를 구축
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play  # 장르별 총 재생 횟수 추가
        genre_songs[genre].append((idx, play))  # (노래 고유번호, 재생 횟수) 추가
    # 장르를 총 재생 횟수로 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)
    # 각 장르에 대해 가장 많이 재생된 두 곡을 선택
    for genre, _ in sorted_genres:
        # 해당 장르의 노래를 재생 횟수로 내림차순 정렬, 고유번호 오름차순 정렬
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[1], x[0])) 
        answer.extend([song[0] for song in sorted_songs[:2]]) # 최대 두 곡을 베스트 앨범에 추가
    return answer