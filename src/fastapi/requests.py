from request import Request
from typing import Literal
from constants import GITHUB_API_REPO, HTTP_STATUS



class FastAPIRequest(Request):
    def __init__(
        self,
        *,
        docs_section: Literal["advanced", "tutorial", "deployment"] = "tutorial"
    ) -> None:
        super().__init__()
        self.docs_dir: str = "tiangolo/fastapi/contents/docs/en/docs/"
        self.docs_section = docs_section


    def fetch_file_list(self):
        response = self.get(GITHUB_API_REPO + self.docs_dir + self.docs_section)
        if response.status_code != HTTP_STATUS["OK_200"]:
            return False
        return self.convert_query_json_to_dirs_list(response.json())





        
