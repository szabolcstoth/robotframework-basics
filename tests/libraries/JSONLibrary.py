import json

from robot.api.deco import keyword, library


@library(scope="GLOBAL", version="1.0")
class JSONLibrary:
    """Library which contains keywords to work with JSON files."""

    @keyword("Parse JSON File", tags=["json"])
    def parse_json_file(self, json_file: str):
        """Returns the parsed ``json_file`` as a dictionary.

        Example:
        | &{parsed_json}= | Parse JSON File | exam_results.json |
        =>
        | ${parsed_json}= {'Jane Doe': {'math': '90%', 'physics': '85%'}}
        """
        with open(json_file, encoding="utf-8") as json_content:
            return json.load(json_content)
