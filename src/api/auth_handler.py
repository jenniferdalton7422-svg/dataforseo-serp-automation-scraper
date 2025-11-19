thonpython
import base64

class AuthHandler:
 @staticmethod
 def generate_auth_header(username: str, password: str) -> str:
 token = base64.b64encode(f"{username}:{password}".encode()).decode()
 return f"Basic {token}"