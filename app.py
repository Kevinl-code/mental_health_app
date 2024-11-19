from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('mental_health.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mood_checkins
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, mood TEXT, stress_level INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

# API to handle mood data submission
@app.route('/submitMood', methods=['POST'])
def submit_mood():
    data = request.get_json()
    mood = data.get('mood')
    stress_level = data.get('stressLevel')

    if not mood or not stress_level:
        return jsonify({"error": "Missing data"}), 400

    conn = sqlite3.connect('mental_health.db')
    c = conn.cursor()
    c.execute('INSERT INTO mood_checkins (mood, stress_level) VALUES (?, ?)', (mood, stress_level))
    conn.commit()
    conn.close()

    return jsonify({"message": "Mood data saved successfully"}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
