from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/date', methods=['GET'])
def get_date():
    today = datetime.date.today()
    dates = {
        0: '今日は月曜だよ！',
        1: '今日は火曜だよ！',
        2: '今日は水曜だよ！',
        3: '今日は木曜だよ！',
        4: '今日は金曜だよ！',
        5: '今日は土曜だよ！',
        6: '今日は日曜だよ！'
    }

    return render_template('translate.html', message=dates[today.weekday()])


if __name__ == "__main__":
    app.run(port=8080)
