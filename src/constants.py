import os
from typing import Dict

## Github
SEC_FILE_NAME: str = os.path.dirname(__file__) + "/gh_token.txt"
GITHUB_API_URL: str = "https://api.github.com/"
GITHUB_API_REPO: str = "repos/"
HTTP_STATUS: Dict = {
    "OK_200": 200,
    "FOUND_302": 302,
    "NOT_FOUND_404": 404,
    "FORBIDDEN_403": 403,
}
