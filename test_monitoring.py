from unittest.mock import patch, MagicMock
from monitoring_system import zkontroluj_web

def test_web_funguje():
    web = {"name": "test", "url": "https://google.com"}
    
    with patch("monitoring_system.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.elapsed.total_seconds.return_value = 0.5
        mock_get.return_value = mock_response
        
        result = zkontroluj_web(web)
        assert result == True
        
def test_web_nefunguje():
    web = {"name": "test", "url": "https://google.com"}
    
    with patch("monitoring_system.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.elapsed.total_seconds.return_value = 0.5
        mock_get.return_value = mock_response
        
        result = zkontroluj_web(web)
        assert result == False