from docx import Document
from pathlib import Path

# 1괘.docx 파일 읽기
doc_path = Path("해석/1괘.docx")

if doc_path.exists():
    try:
        doc = Document(doc_path)
        content = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                content.append(paragraph.text)
        
        print("=== 1괘 해석 내용 ===")
        print('\n'.join(content))
        
    except Exception as e:
        print(f"파일을 읽는 중 오류가 발생했습니다: {str(e)}")
else:
    print("1괘.docx 파일을 찾을 수 없습니다.") 