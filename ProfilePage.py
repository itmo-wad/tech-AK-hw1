import datetime

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

data = {
    "name": "Arthur K.",
    "email": "email.fake.email@do-not-mail.spdns.org",
    "pic_file_name": "profile_pic.jpg",
    "education_exchange_university": "Guest University: ITMO University",
    "education_university": "Home University: University of Cologne",
    "github_display_url": "GitHub Profile",
    "work_experience": "Developing Apps",
    "github_url": "https://github.com/tech-AK",
    "update_date": datetime.date.today()
}

@app.route('/')
def main():
    return redirect(url_for('profile'))

@app.route('/profile', defaults={'liteOrFullProfile': 'lite'})
@app.route('/profile/<string:liteOrFullProfile>')
def profile(liteOrFullProfile):
    if liteOrFullProfile == "full":
        return render_template('index.html', fullProfile=True, data=data)
    else:
        return render_template('index.html', fullProfile=False, data=data)


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)