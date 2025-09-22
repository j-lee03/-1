from flask import Flask, render_template
app = Flask(__name__)

users = [
    {"name": "Alice", "username": "alice_in_wonderland"},
    {"name": "Bob", "username": "bob_the_builder"},
    {"name": "Charlie", "username": "charlie_brown"},
    {"name": "David", "username": "david_copperfield"},
    {"name": "Eve", "username": "eve_the_hacker"}
]

@app.route('/')
def index():
    """
    루트 URL('/')에 접속했을 때 호출되는 뷰 함수입니다.
    사용자 목록 데이터를 HTML 템플릿으로 전달하여 렌더링합니다.
    """
    return render_template('index.html', users=users)

if __name__ == '__main__':
    
    app.run(debug=True, port=5000)
