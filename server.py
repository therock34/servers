from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def home():
    return "Welcome to the API server!"

# POST isteği için endpoint
@app.route('/api', methods=['POST'])
def process_api():
    data = request.json  # POST isteğiyle gelen veriyi alın
    # İşleme kodunu buraya ekleyin
    # .yaml dosyasında belirtilen işlemleri gerçekleştirin
    # Sonuçları oluşturun veya işleyin
    # Örneğin, gelen veriyi bir işleme tabi tutup sonuçları döndürebilirsiniz
    result = {'message': 'API request processed successfully', 'data': data}
    return jsonify(result), 200

# Swagger UI için gerekli ayarlar
SWAGGER_URL = '/swagger'
API_URL = 'C:\Users\ogulc\OneDrive\Masaüstü\server\openapi.yaml' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Server"
    }
)

# Swagger UI için blueprint'i kaydedin
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()
