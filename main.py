from news import find_news
from analyzer import print_news, get_score


def main():

    print("--------------------------------------------------------")
    print("                  관심종목 뉴스 분석기")
    print("--------------------------------------------------------")

    ticker = input("관심 종목의 티커 입력 (예: AAPL, MSFT, TSLA): ")
    ticker = ticker.upper()

    news_list = find_news(ticker)

    news_list = news_list[:20]

    total_score = print_news(news_list)

    print("\n[종합 결과]")
    print("종합 점수:", total_score)
    print("결과:", get_score(total_score))


if __name__ == "__main__":
    main()
