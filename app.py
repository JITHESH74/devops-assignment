from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the HTML response
    return f"""
    <html>
        <head>
            <title>DevOps Assignment</title>
            <style>
            
                body {{
                    font-family: Arial, sans-serif; 
                    display: grid; 
                    place-items: center; 
                    min-height: 90vh; 
                    background-color: #f4f4f9;
                }}
                .container {{
                    padding: 2rem;
                    border-radius: 8px;
                    background-color: #ffffff;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                    text-align: center;
                }}
                h1 {{ color: #333; }}
                p {{ color: #555; font-size: 1.1rem; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello from Dr. ViKi DevOps Pipeline!</h1>
                <p>Current Server Time: {timestamp}</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)