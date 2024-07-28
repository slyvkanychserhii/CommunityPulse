from app import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, port=8000)  # на macOS 5000-й порт занимает AirPlay Receiver
