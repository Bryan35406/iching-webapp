#!/usr/bin/env python3
"""
주역 괘 해석 파일 업데이트 스크립트

사용법:
1. /Users/bpark/Desktop/0_Python/주역/해석/ 폴더에서 괘 파일들을 수정
2. 이 스크립트를 실행하여 웹앱 폴더로 복사

python update_hexagram_files.py
"""

import os
import shutil
from pathlib import Path

def update_hexagram_files():
    """괘 해석 파일들을 원본 폴더에서 웹앱 폴더로 복사"""
    
    # 경로 설정
    source_dir = Path("/Users/bpark/Desktop/0_Python/주역/해석")
    target_dir = Path("/Users/bpark/Desktop/0_Python/주역/iching-webapp/해석")
    
    print("🔄 주역 괘 해석 파일 업데이트 시작...")
    print(f"📁 원본 폴더: {source_dir}")
    print(f"📁 대상 폴더: {target_dir}")
    
    # 폴더 존재 확인
    if not source_dir.exists():
        print(f"❌ 원본 폴더가 존재하지 않습니다: {source_dir}")
        return False
        
    if not target_dir.exists():
        print(f"❌ 대상 폴더가 존재하지 않습니다: {target_dir}")
        return False
    
    # .docx 파일들 찾기
    docx_files = list(source_dir.glob("*.docx"))
    
    if not docx_files:
        print("❌ 원본 폴더에 .docx 파일이 없습니다.")
        return False
    
    print(f"📋 발견된 파일 수: {len(docx_files)}개")
    
    # 파일 복사
    copied_count = 0
    updated_files = []
    
    for source_file in docx_files:
        target_file = target_dir / source_file.name
        
        try:
            # 파일 복사
            shutil.copy2(source_file, target_file)
            copied_count += 1
            updated_files.append(source_file.name)
            print(f"✅ 복사 완료: {source_file.name}")
            
        except Exception as e:
            print(f"❌ 복사 실패: {source_file.name} - {e}")
    
    print(f"\n🎉 업데이트 완료!")
    print(f"📊 총 {copied_count}개 파일 복사됨")
    
    if updated_files:
        print("\n📝 업데이트된 파일 목록:")
        for filename in sorted(updated_files):
            print(f"   - {filename}")
    
    print("\n💡 서버를 재시작하여 변경사항을 반영하세요:")
    print("   pkill -f 'python app.py' && python app.py")
    
    return True

if __name__ == "__main__":
    update_hexagram_files() 