from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_lotto_numbers():
    results = []
    for _ in range(5):
        numbers = sorted(random.sample(range(1, 46), 5))
        results.append(numbers)
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # POST 요청 처리 로직: 새로운 로또 번호 생성
        lotto_numbers = generate_lotto_numbers()
        return render_template('index.html', lotto_numbers=lotto_numbers)
    else:
        # GET 요청 처리 로직: 초기 로드
        lotto_numbers = generate_lotto_numbers()
        return render_template('index.html', lotto_numbers=lotto_numbers)

if __name__ == '__main__':
    app.run(debug=True)
