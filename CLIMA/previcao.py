import requests

class PrevisaoOpenMeteo:
    def __init__(self):
        # URLs base da Open-Meteo
        self.geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        self.weather_url = "https://api.open-meteo.com/v1/forecast"

    def buscar_cidade(self, nome_cidade):
        # --- PASSO 1: Descobrir as coordenadas da cidade (Geocoding) ---
        geo_params = {"name": nome_cidade, "count": 1, "language": "pt", "format": "json"}
        
        try:
            geo_response = requests.get(self.geo_url, params=geo_params)
            geo_data = geo_response.json()

            # Verificamos se a API encontrou alguma cidade
            if "results" not in geo_data:
                return {"erro": f"Cidade '{nome_cidade}' não encontrada."}

            # Pegamos a primeira cidade da lista e suas coordenadas
            cidade_info = geo_data["results"][0]
            lat = cidade_info["latitude"]
            lon = cidade_info["longitude"]
            nome_real = cidade_info["name"]
            pais = cidade_info.get("country", "")

            # --- PASSO 2: Buscar o clima usando as coordenadas ---
            weather_params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": "true", # Queremos o tempo AGORA, não histórico
                "timezone": "auto"
            }

            weather_response = requests.get(self.weather_url, params=weather_params)
            weather_data = weather_response.json()

            if "current_weather" in weather_data:
                tempo = weather_data["current_weather"]
                
                return {
                    "cidade": nome_real,
                    "pais": pais,
                    "temperatura": tempo["temperature"],
                    "velocidade_vento": tempo["windspeed"],
                    "codigo_tempo": tempo["weathercode"] # Usaremos isso para ícones depois
                }
            else:
                return {"erro": "Erro ao obter dados meteorológicos."}

        except requests.exceptions.RequestException as e:
            return {"erro": f"Erro de conexão: {e}"}

# --- TESTE NO CONSOLE ---
sistema = PrevisaoOpenMeteo()
resultado = sistema.buscar_cidade("Manaus") # Teste com sua cidade
print(resultado)
	