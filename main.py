import functions_framework
from app import app

@functions_framework.http
def main(request):
    """Firebase Functions용 Flask 앱 엔트리포인트"""
    return app(request.environ, lambda status, headers: None) 