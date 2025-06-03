#!/usr/bin/env python3
"""
주역 괘 파일 간편 업데이트 도구

사용법: python update.py
"""

import subprocess
import sys

def main():
    print("🔄 주역 괘 파일 업데이트 중...")
    
    try:
        # 1. 파일 업데이트
        subprocess.run([sys.executable, "update_hexagram_files.py"], check=True)
        
        print("\n🔃 서버 재시작 중...")
        
        # 2. 서버 중지
        subprocess.run(["pkill", "-f", "python app.py"], check=False)
        
        # 3. 서버 시작 (백그라운드)
        subprocess.Popen([sys.executable, "app.py"])
        
        print("✅ 모든 작업 완료!")
        print("🌐 웹사이트: http://localhost:5001")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 오류 발생: {e}")
    except KeyboardInterrupt:
        print("\n❌ 사용자에 의해 중단됨")

if __name__ == "__main__":
    main() 