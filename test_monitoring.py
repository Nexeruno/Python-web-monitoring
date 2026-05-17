from unittest.mock import patch, MagicMock
from monitoring_system import zkontroluj_web, posli_slack


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
        
def test_web_nedostupny():
    web = {"name": "test", "url": "https://google.com"}
    
    with patch("monitoring_system.requests.get") as mock_get, \
         patch("monitoring_system.requests.post") as mock_post:
        mock_get.side_effect = Exception("Connection error")
        mock_post.return_value = MagicMock(status_code=200)
        
        result = zkontroluj_web(web)
        assert result == False
        
def test_slack_nefunguje():
    with patch("monitoring_system.requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "error"
        mock_post.return_value = mock_response
        
        posli_slack("test zprava")
        mock_post.assert_called_once()