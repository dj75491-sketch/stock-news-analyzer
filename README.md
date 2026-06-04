# stock-news-analyzer
# 관심 종목 뉴스 자동 요약 및 투자 영향 분석 프로그램

## 1. 프로젝트 이름
관심 종목 뉴스 자동 요약 및 투자 영향 분석 프로그램

---

## 2. 한 문장 설명
관심 종목의 최신 뉴스를 자동으로 수집하고, 핵심 키워드를 기반으로 투자 영향도를 분석하여 정리해주는 Python 기반 프로그램이다.

---

## 3. 만들게 된 이유 및 해결하려는 문제

평소 국내 ETF와 해외 ETF에 관심이 많아 관련 뉴스를 자주 찾아보지만, 여러 사이트를 직접 방문해 뉴스를 확인하는 과정이 번거롭고 시간이 많이 소요되었다. 또한 뉴스가 많아 중요한 내용을 빠르게 파악하기 어렵고, 투자에 긍정적인지 부정적인지를 직접 판단해야 하는 불편함이 있었다.

이 프로젝트는 관심 종목의 뉴스를 자동으로 수집하고, 핵심 키워드를 기반으로 뉴스 내용을 정리 및 분석하여 투자 정보를 보다 효율적으로 확인할 수 있도록 돕기 위해 기획하였다.

---

## 4. 핵심 기능

### MUST 기능

#### 1) 관심 종목 뉴스 자동 수집
- Yahoo Finance 또는 네이버 금융 뉴스 수집
- 종목별 최신 뉴스 제목 및 링크 조회
- 종목별 뉴스 목록 출력

#### 2) 키워드 기반 투자 영향 분석
- 뉴스 제목 내 긍정·부정 키워드 탐색
- 투자 영향도를 긍정 / 부정 / 중립으로 분류
- 핵심 키워드 출력

#### 3) 뉴스 결과 저장 기능
- 뉴스 데이터를 json 또는 txt 파일로 저장
- 날짜별 기록 저장 가능

---

### NICE 기능

#### 4) 종목별 뉴스 기록 조회
- 저장된 이전 뉴스 기록 다시 확인

#### 5) 뉴스 중요도 분류
- 키워드 개수에 따라 중요도 상 / 중 / 하 출력

#### 6) 간단한 통계 기능
- 긍정/부정 뉴스 개수 출력
- 가장 많이 등장한 키워드 분석

---

### LATER 기능

#### 7) AI API 기반 뉴스 요약 기능
- OpenAI API 또는 Claude API 활용
- 뉴스 핵심 내용을 3줄 이내로 자동 요약

#### 8) AI 기반 투자 영향 분석 고도화
- 단순 키워드 분석이 아닌 문맥 기반 감정 분석

#### 9) 카카오톡 알림 기능
- 중요 뉴스 자동 알림 전송

#### 10) 주가 데이터 연동 기능
- 뉴스 발생 시점의 주가 데이터 비교 분석

---

## 5. 예상 사용자
- 주식 및 ETF 투자에 관심 있는 사용자
- 여러 종목 뉴스를 빠르게 확인하고 싶은 개인 투자자
- 프로그램 제작자인 본인

---

## 6. 결과물 형태
CLI 기반 프로그램

---

## 7. 사용할 Python 개념 및 기술

### Python 개념
- 변수
- 리스트
- 딕셔너리
- 조건문
- 반복문
- 함수
- 문자열 처리
- 파일 입출력
- 예외 처리

---

## 8. 예상 프로그램 흐름

```text
관심 종목 선택
        ↓
뉴스 자동 수집
        ↓
키워드 분석
        ↓
긍정 / 부정 / 중립 분류
        ↓
결과 출력 및 저장

```

---

## 9. 코드 작성

```python
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


PLUS_KEYWORDS = {
    "growth": 3,
    "grow": 2,
    "grows": 2,
    "profit": 3,
    "profits": 3,
    "profitable": 3,
    "revenue": 2,
    "sales": 1,
    "earnings": 1,
    "gain": 2,
    "gains": 2,
    "rise": 2,
    "rises": 2,
    "rising": 2,
    "jump": 2,
    "jumps": 2,
    "higher": 1,
    "strong": 2,
    "strength": 2,
    "beat": 2,
    "beats": 2,
    "outperform": 2,
    "outperforms": 2,
    "upgrade": 2,
    "upgraded": 2,
    "buy": 2,
    "bullish": 3,
    "record": 2,
    "surge": 3,
    "surges": 3,
    "demand": 1,
    "partnership": 1,
    "expansion": 2,
    "recovery": 2,
    "buyback": 2,
    "optimistic": 2,
    "approval": 2,
    "acquisition": 1,
    "accelerate": 2,
    "accelerates": 2,
    "innovation": 1,
    "dividend": 1,
    "momentum": 2,
    "rally": 2,
    "rallies": 2,
    "rebound": 2,
    "rebounds": 2,
    "improve": 2,
    "improves": 2,
    "improved": 2,
    "improvement": 2,
    "confidence": 1,
    "opportunity": 1,
    "opportunities": 1,
    "lead": 1,
    "leads": 1,
    "leading": 1,
    "launch": 1,
    "launches": 1,
    "contract": 1,
    "contracts": 1,
    "win": 2,
    "wins": 2,
    "winning": 2,
    "award": 1,
    "awards": 1,
    "customer": 1,
    "customers": 1,
    "cloud": 1,
    "ai": 1,
    "chip": 1,
    "chips": 1,
    "margin": 2,
    "margins": 2,
    "cash": 1,
    "flow": 1,
    "forecast": 1,
    "forecasts": 1,
    "guidance": 1,
    "raise": 2,
    "raises": 2,
    "raised": 2,
    "target": 1,
    "targets": 1,
    "boost": 2,
    "boosts": 2,
    "boosted": 2,
    "savings": 1,
    "efficiency": 1,
    "efficient": 1,
    "robust": 2,
    "stable": 1,
    "stability": 1,
    "success": 2,
    "successful": 2,
    "breakthrough": 2,
    "premium": 1,
    "invest": 1,
    "investment": 1,
    "investments": 1,
}

MINUS_KEYWORDS = {
    "bankruptcy": -3,
    "crisis": -3,
    "loss": -3,
    "losses": -3,
    "drop": -2,
    "drops": -2,
    "dropped": -2,
    "fall": -2,
    "falls": -2,
    "falling": -2,
    "plunge": -3,
    "plunges": -3,
    "weak": -2,
    "weakness": -2,
    "miss": -2,
    "misses": -2,
    "downgrade": -2,
    "downgraded": -2,
    "sell": -2,
    "bearish": -3,
    "risk": -1,
    "risks": -1,
    "lawsuit": -3,
    "probe": -2,
    "investigation": -2,
    "regulatory": -1,
    "warning": -2,
    "warns": -2,
    "debt": -2,
    "inflation": -1,
    "recession": -2,
    "layoffs": -2,
    "slump": -2,
    "concern": -1,
    "concerns": -1,
    "decline": -2,
    "declines": -2,
    "declining": -2,
    "lower": -1,
    "cut": -1,
    "cuts": -1,
    "delay": -1,
    "delays": -1,
    "delayed": -1,
    "pressure": -1,
    "pressures": -1,
    "volatile": -1,
    "volatility": -1,
    "uncertainty": -1,
    "uncertain": -1,
    "penalty": -2,
    "penalties": -2,
    "fine": -2,
    "fines": -2,
    "fraud": -3,
    "default": -3,
    "shortage": -2,
    "shortages": -2,
    "recall": -2,
    "recalls": -2,
    "problem": -1,
    "problems": -1,
    "issue": -1,
    "issues": -1,
    "challenge": -1,
    "challenges": -1,
    "competition": -1,
    "slowdown": -2,
    "slows": -1,
    "slow": -1,
    "expensive": -1,
    "overvalued": -2,
    "underperform": -2,
    "underperforms": -2,
    "reduce": -1,
    "reduces": -1,
    "reduced": -1,
    "reduction": -1,
    "cancel": -2,
    "cancels": -2,
    "cancelled": -2,
    "suspend": -2,
    "suspended": -2,
    "closure": -2,
    "closures": -2,
    "strike": -2,
    "strikes": -2,
    "litigation": -3,
    "breach": -2,
    "breaches": -2,
    "cyberattack": -3,
    "cyberattacks": -3,
    "tariff": -1,
    "tariffs": -1,
    "headwind": -1,
    "headwinds": -1,
    "negative": -1,
    "pessimistic": -2,
    "fear": -1,
    "fears": -1,
}


def get_text(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    response = urllib.request.urlopen(request, timeout=10)
    data = response.read()
    return data.decode("utf-8", errors="ignore")


def get_stock_info(ticker):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/"
    url = url + urllib.parse.quote(ticker) + "?range=1d&interval=1d"

    try:
        text = get_text(url)
        data = json.loads(text)
        result = data["chart"]["result"]

        if len(result) == 0:
            return None

        stock = result[0]["meta"]
        price = stock.get("regularMarketPrice", "정보 없음")
        previous_close = stock.get("chartPreviousClose", "정보 없음")
        volume = stock.get("regularMarketVolume", "정보 없음")
        change = "정보 없음"
        change_percent = "정보 없음"
        market_pressure = "정보 없음"

        if price != "정보 없음" and previous_close != "정보 없음":
            change = price - previous_close
            change_percent = change / previous_close * 100
            change = round(change, 2)
            change_percent = round(change_percent, 2)

            if change > 0:
                market_pressure = "매수세 우세 추정"
            elif change < 0:
                market_pressure = "매도세 우세 추정"
            else:
                market_pressure = "매수세/매도세 균형 추정"

        info = {
            "name": stock.get("longName", "정보 없음"),
            "symbol": stock.get("symbol", ticker),
            "price": price,
            "change": change,
            "change_percent": change_percent,
            "volume": volume,
            "market_pressure": market_pressure,
            "currency": stock.get("currency", ""),
        }
        return info

    except Exception as error:
        print("주식 정보를 가져오는 중 오류가 발생했습니다:", error)
        return None


def get_news(ticker):
    url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s="
    url = url + urllib.parse.quote(ticker) + "&region=US&lang=en-US"

    news_list = []

    try:
        text = get_text(url)
        root = ET.fromstring(text)
        items = root.findall(".//item")

        for item in items:
            title_tag = item.find("title")
            link_tag = item.find("link")
            summary_tag = item.find("description")

            if title_tag is not None and title_tag.text is not None:
                news = {
                    "title": title_tag.text,
                    "link": "",
                    "summary": "",
                }

                if link_tag is not None and link_tag.text is not None:
                    news["link"] = link_tag.text

                if summary_tag is not None and summary_tag.text is not None:
                    news["summary"] = remove_html_tags(summary_tag.text)

                news_list.append(news)

        return news_list

    except Exception as error:
        print("뉴스를 가져오는 중 오류가 발생했습니다:", error)
        return []


def clean_word(word):
    result = ""

    for char in word:
        if char.isalpha():
            result = result + char.lower()

    return result


def remove_html_tags(text):
    result = ""
    in_tag = False

    for char in text:
        if char == "<":
            in_tag = True
        elif char == ">":
            in_tag = False
        elif in_tag == False:
            result = result + char

    return result.strip()


def safe_text(text):
    return str(text).encode("cp949", errors="replace").decode("cp949")


def analyze_news_title(title):
    words = title.split()
    found_plus = []
    found_minus = []
    score = 0

    for word in words:
        word = clean_word(word)

        if word in PLUS_KEYWORDS:
            score = score + PLUS_KEYWORDS[word]
            found_plus.append(word)

        if word in MINUS_KEYWORDS:
            score = score + MINUS_KEYWORDS[word]
            found_minus.append(word)

    result = {
        "score": score,
        "plus": found_plus,
        "minus": found_minus,
    }
    return result


def get_score_message(score):
    if score >= 21:
        return "매우 긍정적"
    elif score >= 6:
        return "긍정적"
    elif score >= -5:
        return "중립"
    elif score >= -20:
        return "부정적"
    else:
        return "매우 부정적"


def print_stock_info(info):
    print("\n[주식 정보]")

    if info is None:
        print("주식 정보를 찾을 수 없습니다.")
        return

    print("회사명:", info["name"])
    print("티커:", info["symbol"])
    print("현재가:", info["price"], info["currency"])
    print("변동:", info["change"])
    print("변동률:", info["change_percent"], "%")
    print("최근 장 거래량:", info["volume"])
    print("매수/매도세:", info["market_pressure"])


def print_keyword_table():
    print("\n[점수 가중치 기준]")
    print("3점: 주가나 기업 평가에 강하게 영향을 줄 수 있는 단어")
    print("2점: 긍정/부정 방향이 비교적 뚜렷한 단어")
    print("1점: 관련은 있지만 영향이 약하거나 보조적인 단어")
    print("\n[종합 점수 판단 기준]")
    print("21점 이상: 매우 긍정적")
    print("6점 ~ 20점: 긍정적")
    print("-5점 ~ 5점: 중립")
    print("-20점 ~ -6점: 부정적")
    print("-21점 이하: 매우 부정적")


def print_news_analysis(news_list):
    total_score = 0

    print("\n[뉴스 분석 결과]")

    if len(news_list) == 0:
        print("분석할 뉴스가 없습니다.")
        return 0

    for i in range(len(news_list)):
        title = news_list[i]["title"]
        summary = news_list[i]["summary"]
        analysis_text = title + " " + summary
        result = analyze_news_title(analysis_text)
        total_score = total_score + result["score"]

        print("\n뉴스", i + 1)
        print("제목:", safe_text(title))
        if summary != "":
            print("요약:", safe_text(summary))
        print("점수:", result["score"])

    return total_score


def save_result(ticker, info, news_list, total_score):
    file_name = ticker + "_analysis.txt"

    try:
        file = open(file_name, "w", encoding="utf-8")
        file.write("주식 뉴스 분석 결과\n")
        file.write("====================\n\n")
        file.write("티커: " + ticker + "\n")

        if info is not None:
            file.write("회사명: " + str(info["name"]) + "\n")
            file.write("현재가: " + str(info["price"]) + " " + str(info["currency"]) + "\n")
            file.write("최근 장 거래량: " + str(info["volume"]) + "\n")
            file.write("매수/매도세: " + str(info["market_pressure"]) + "\n")

        file.write("종합 점수: " + str(total_score) + "\n")
        file.write("판단: " + get_score_message(total_score) + "\n\n")

        for i in range(len(news_list)):
            title = news_list[i]["title"]
            summary = news_list[i]["summary"]
            analysis_text = title + " " + summary
            result = analyze_news_title(analysis_text)
            file.write("뉴스 " + str(i + 1) + "\n")
            file.write("제목: " + title + "\n")
            if summary != "":
                file.write("요약: " + summary + "\n")
            file.write("점수: " + str(result["score"]) + "\n")
            file.write("\n")

        file.close()
        print("\n분석 결과가", file_name, "파일로 저장되었습니다.")

    except Exception as error:
        print("파일 저장 중 오류가 발생했습니다:", error)


def main():
    print("주식 뉴스 분석기")
    print("================")
    print("Yahoo Finance에서 주식 정보와 뉴스를 가져와 키워드 점수를 계산합니다.")

    ticker = input("\n티커를 입력하세요. 예: AAPL, MSFT, TSLA: ")
    ticker = ticker.upper().strip()

    if ticker == "":
        print("티커가 입력되지 않았습니다.")
        return

    info = get_stock_info(ticker)
    news_list = get_news(ticker)

    if len(news_list) > 10:
        news_list = news_list[:10]

    print_stock_info(info)
    print_keyword_table()
    total_score = print_news_analysis(news_list)

    print("\n[종합 결과]")
    print("종합 점수:", total_score)
    print("판단:", get_score_message(total_score))

    answer = input("\n결과를 txt 파일로 저장할까요? (y/n): ")

    if answer == "y" or answer == "Y":
        save_result(ticker, info, news_list, total_score)


if __name__ == "__main__":
    main()

```
