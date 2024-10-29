from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .content {
                    text-align: center;
                }
            </style>
            <script>
                function updateTime() {
                    const now = new Date();
                    const formattedTime = now.toLocaleString('ru-RU', {
                        year: 'numeric',
                        month: '2-digit',
                        day: '2-digit',
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit'
                    });
                    document.getElementById('time').textContent = formattedTime;
                }
                setInterval(updateTime, 1000);
                window.onload = updateTime; // Обновить время при загрузке
            </script>
        </head>
        <body>
            <div class="content">
                <h1>Текущие дата и время:</h1>
                <p id="time"></p>
            </div>
        </body>
    </html>"""

if __name__ == '__main__':
    app.run()