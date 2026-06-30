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
