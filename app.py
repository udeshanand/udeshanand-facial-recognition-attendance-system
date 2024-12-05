from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

import attendance_taker
import features_extraction_to_csv
import get_faces_from_camera_tkinter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', selected_date='', no_data=False)


@app.route('/attendance', methods=['POST'])
def attendance():
    selected_date = request.form.get('selected_date')
    selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
    formatted_date = selected_date_obj.strftime('%Y-%m-%d')

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
    attendance_data = cursor.fetchall()

    conn.close()

    if not attendance_data:
        return render_template('index.html', selected_date=selected_date, no_data=True)

    return render_template('index.html', selected_date=selected_date, attendance_data=attendance_data)


def register():
    get_faces_from_camera_tkinter.main()
    features_extraction_to_csv.main()
    return render_template('index.html' ,message="Registration complete. You can now mark attendance.")


def mark_attendance():
    attendance_taker.main()
    return render_template('index.html')


@app.route('/handle_action', methods=['POST'])
def handle_action():
    action = request.form.get('action')
    if action == "register":
        return register()
    elif action == "mark_attendance":
         return mark_attendance()
    else:
        return "Invalid action", 400





if __name__ == '__main__':
    app.run(debug=True)
