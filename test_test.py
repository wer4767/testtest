# import fitz
# path = "C:\\Users\\admin\Desktop\\RPA 시스템\\M-20240422-16 필증.pdf"
# doc = fitz.open(path)
# for page in doc:
#     text = page.get_text()
#     print(text)



import fitz  # PyMuPDF

# PDF 파일 경로
pdf_file = "C:\\Users\\admin\Desktop\\RPA 시스템\\M-20240422-16 필증.pdf"

# PDF 파일 열기
doc = fitz.open(pdf_file)

# 추출된 텍스트를 저장할 변수 초기화
extracted_text = ''

# 페이지별로 텍스트 추출
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()

    # 특정 문자열('C/S구분') 찾기
    index = text.find('C/S구분')
    if index != -1:
        # 'C/S구분' 다음에 나오는 텍스트 추출
        text_after_keyword = text[index + len('C/S구분'):].strip()   ##### strip() = 공백제거 
        # 공백을 기준으로 텍스트를 나누고 앞에서부터 10개의 텍스트만 추출
        extracted_text = ' '.join(text_after_keyword.split()[:1])
        break  # 텍스트를 찾았으므로 반복문 종료

# 추출된 텍스트 출력
print(extracted_text)

# 리소스 정리
doc.close()