from app import app  # Make sure this imports your Flask app

if __name__ == '__main__':
    print("Starting ATS Score Checker...")
    app.run(debug=True, port=5000)
    