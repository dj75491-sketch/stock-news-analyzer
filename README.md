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
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


# 긍정 키워드 및 가중치
Plus_Keywords = {
    # 3점
    "growth": 3, "profit": 3, "profits": 3, "profitable": 3,
    "bullish": 3, "surge": 3, "surges": 3,
    # 2점
    "grow": 2, "grows": 2, "revenue": 2, "gain": 2, "gains": 2,
    "rise": 2, "rises": 2, "rising": 2, "jump": 2, "jumps": 2,
    "strong": 2, "strength": 2, "beat": 2, "beats": 2,
    "outperform": 2, "outperforms": 2, "upgrade": 2, "upgraded": 2,
    "buy": 2, "record": 2, "expansion": 2, "recovery": 2,
    "buyback": 2, "optimistic": 2, "approval": 2, "accelerate": 2,
    "accelerates": 2, "momentum": 2, "rally": 2, "rallies": 2,
    "rebound": 2, "rebounds": 2, "improve": 2, "improves": 2,
    "improved": 2, "improvement": 2, "win": 2, "wins": 2,
    "winning": 2, "margin": 2, "margins": 2, "raise": 2,
    "raises": 2, "raised": 2, "boost": 2, "boosts": 2,
    "boosted": 2, "robust": 2, "success": 2, "successful": 2,
    "breakthrough": 2,
    # 1점
    "sales": 1, "earnings": 1, "higher": 1, "demand": 1,
    "partnership": 1, "acquisition": 1, "innovation": 1, "dividend": 1,
    "confidence": 1, "opportunity": 1, "opportunities": 1, "lead": 1,
    "leads": 1, "leading": 1, "launch": 1, "launches": 1,
    "contract": 1, "contracts": 1, "award": 1, "awards": 1,
    "customer": 1, "customers": 1, "cloud": 1, "ai": 1,
    "chip": 1, "chips": 1, "cash": 1, "flow": 1,
    "forecast": 1, "forecasts": 1, "guidance": 1, "target": 1,
    "targets": 1, "savings": 1, "efficiency": 1, "efficient": 1,
    "stable": 1, "stability": 1, "premium": 1, "invest": 1,
    "investment": 1, "investments": 1,
}

# 부정 키워드 및 가중치
Minus_Keywords ={
    # -3점
    "bankruptcy": -3, "crisis": -3, "loss": -3, "losses": -3,
    "plunge": -3, "plunges": -3, "bearish": -3, "lawsuit": -3,
    "fraud": -3, "default": -3, "litigation": -3,
    "cyberattack": -3, "cyberattacks": -3,
    # -2점
    "drop": -2, "drops": -2, "dropped": -2, "fall": -2,
    "falls": -2, "falling": -2, "weak": -2, "weakness": -2,
    "miss": -2, "misses": -2, "downgrade": -2, "downgraded": -2,
    "sell": -2, "probe": -2, "investigation": -2, "warning": -2,
    "warns": -2, "debt": -2, "recession": -2, "layoffs": -2,
    "slump": -2, "decline": -2, "declines": -2, "declining": -2,
    "penalty": -2, "penalties": -2, "fine": -2, "fines": -2,
    "shortage": -2, "shortages": -2, "recall": -2, "recalls": -2,
    "slowdown": -2, "overvalued": -2, "underperform": -2, "underperforms": -2,
    "cancel": -2, "cancels": -2, "cancelled": -2, "suspend": -2,
    "suspended": -2, "closure": -2, "closures": -2, "strike": -2,
    "strikes": -2, "breach": -2, "breaches": -2, "pessimistic": -2,
    # -1점
    "risk": -1, "risks": -1, "regulatory": -1, "inflation": -1,
    "concern": -1, "concerns": -1, "lower": -1, "cut": -1,
    "cuts": -1, "delay": -1, "delays": -1, "delayed": -1,
    "pressure": -1, "pressures": -1, "volatile": -1, "volatility": -1,
    "uncertainty": -1, "uncertain": -1, "problem": -1, "problems": -1,
    "issue": -1, "issues": -1, "challenge": -1, "challenges": -1,
    "competition": -1, "slows": -1, "slow": -1, "expensive": -1,
    "reduce": -1, "reduces": -1, "reduced": -1, "reduction": -1,
    "tariff": -1, "tariffs": -1, "headwind": -1, "headwinds": -1,
    "negative": -1, "fear": -1, "fears": -1,
}


# Yahoo Finance RSS에서 뉴스 수집
def find_news(ticker):
    url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s="
    url = url + urllib.parse.quote(ticker) + "&region=US&lang=en-US"

    news_list = []

    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    response = urllib.request.urlopen(request, timeout=10)
    text = response.read().decode("utf-8", errors="ignore")

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


# 단어 정리
def clean_word(word):
    result = ""
    for char in word:
        if char.isalpha():
            result = result + char.lower()
    return result


# HTML 태그 제거
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


# 뉴스 제목+요약에서 키워드 탐색 및 점수 계산
def analyze_news(title, summary):        # 함수로 만든 이유 : 뉴스마다 같은 분석을 반복해야 하기 떄문.
    text = title + " " + summary        # title과 summary : 뉴스마다 제목과 요약 내용이 다르기 때문.
    words = text.split()        # title + summary : 제목이나 내용에만 주요 내용이 있을 수 있음.
    score = 0                # split() 사용이유 : 문장을 단어 단위로 나누어 키워드에 탐색될 수 있도록 함.

    for word in words:                # for문 사용 : 모든 단어를 하나씩 사용하기 위함.
        word = clean_word(word)        # 문장부호같은 문자를 제외한 clean word를 호출함.
        if word in Plus_Keywords:        # 딕셔너리 : 키워드마다 점수가 다르기 때문
            score += Plus_Keywords[word]

        if word in Minus_Keywords:
            score += Minus_Keywords[word]

    return score


# 종합 점수 기준에 따른 판단 문자열 반환
def get_score(score):        # 계산된 가중치를 점수로 변환
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


# 뉴스 분석 결과 출력 및 총 점수 반환
def print_news(news_list):                # 뉴스를 하나씩 분석하고 전체 점수를 계산한다.
    total_score = 0

    print("\n[뉴스 분석 결과]")

    for i in range(len(news_list)):        # 함수 사용 : 뉴스마다 개수만큼 반복 분석해야 하기 때문
        title = news_list[i]["title"]
        summary = news_list[i]["summary"]
        result = analyze_news(title, summary)        # 뉴스 하나의 점수를 계산하기 위함.
        total_score += result

        print("\n뉴스", i + 1) # 리스트 인덱스는 0부터 시작이지만 1번부터 표한하기 위함.
        print("제목:", title)
        if summary != "":
            print("요약:", summary)
        print("점수:", result)

    return total_score        # 최종 종합 점수를 main 함수로 전달.


# 메인 실행
def main():
    print("--------------------------------------------------------")
    print("                  관심종목 뉴스 분석기")
    print("--------------------------------------------------------")

    ticker = input("관심 종목의 티커 입력 (예: AAPL, MSFT, TSLA): ")
    ticker = ticker.upper()        # 사용자가 소문자를 입력해도 가능하게 함.

    news_list = find_news(ticker)

    news_list = news_list[:20]

    total_score = print_news(news_list)

    print("\n[종합 결과]")
    print("종합 점수:", total_score)
    print("결과:", get_score(total_score))


if __name__ == "__main__":
    main()
```
