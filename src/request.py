import requests
from typing import Dict, Union, List
import os
import re
from constants import SEC_FILE_NAME, GITHUB_API_URL


class Request:
    def __init__(self) -> None:
        self._headers: Dict
        self.set_headers()
        self.is_token_valid()

    def get(self, query: str):
        """Make a api call to github with specific query

        Args:
            query (str): github api query

        Returns:
            _type_: _description_
        """
        return requests.get(f"{GITHUB_API_URL}{query}", headers=self._headers)

    def set_headers(self) -> None:
        """Set headers with authorization header"""
        self._headers = {"Authorization": f"Bearer {self.get_token()}"}

    def is_token_valid(self) -> bool:
        """Make request to github API if github declined it token is not valid

        Returns:
            bool: Token is valid or not
        """
        response = requests.get(f"{GITHUB_API_URL}octacot", headers=self._headers)
        if 400 <= response.status_code <= 500:
            return False
        return True

    def get_token(self) -> str:
        """Get token from file to the class

        Raises:
            NotImplemented: If token not exists raise an error
        """
        if os.path.exists(SEC_FILE_NAME):
            with open(SEC_FILE_NAME, "r") as file:
                return file.read()
        else:
            raise NotImplemented("Token is not implemented.")


    def convert_query_json_to_dirs_list(self, output_json) -> List:
        directory_list: List = []
        for object in output_json:
            if re.search(".*\.md$", object.get("name")):
                directory_list.append(object.get("name"))
        return directory_list


