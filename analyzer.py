from keywords import PLUS_KEYWORDS, MINUS_KEYWORDS
from utils import clean_word


# 뉴스 제목+요약에서 키워드 탐색 및 점수 계산
def analyze_news(title, summary):

    text = title + " " + summary
    words = text.split()

    score = 0

    for word in words:

        word = clean_word(word)

        if word in PLUS_KEYWORDS:
            score += PLUS_KEYWORDS[word]

        if word in MINUS_KEYWORDS:
            score += MINUS_KEYWORDS[word]

    return score


# 종합 점수 기준
def get_score(score):

    if score >= 21:
        return "매우 긍정"

    elif score >= 6:
        return "긍정"

    elif score >= -5:
        return "보통"

    elif score >= -20:
        return "부정"

    else:
        return "매우 부정"


# 뉴스 출력
def print_news(news_list):

    total_score = 0

    print("\n[뉴스 분석 결과]")

    for i in range(len(news_list)):

        title = news_list[i]["title"]
        summary = news_list[i]["summary"]

        result = analyze_news(title, summary)

        total_score += result

        print("\n뉴스", i + 1)
        print("제목:", title)

        if summary != "":
            print("요약:", summary)

        print("점수:", result)

    return total_score
