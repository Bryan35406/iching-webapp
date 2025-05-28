import functions_framework
from flask import Flask
import sys
import os

# 현재 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(__file__))

# 기존 Flask 앱 import
from app import app

@functions_framework.http
def flask_app(request):
    """Firebase Functions용 Flask 앱 래퍼"""
    with app.request_context(request.environ):
        return app.full_dispatch_request() 