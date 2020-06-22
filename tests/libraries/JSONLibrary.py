from robot.api.deco import keyword
from robot.api.deco import library
import json


@library(scope='GLOBAL', version='1.0')
class JSONLibrary():
    """Library which contains keywords to work with JSON files."""

    @keyword(tags=['json'], types={'json_file': str})
    def parse_json_file(self, json_file):
        """Returns the parsed ``json_file`` as a dictionary.

        Example:
        | &{parsed_json}= | Parse JSON File | exam_results.json |
        =>
        | ${parsed_json}= {'Jane Doe': {'math': '90%', 'physics': '85%'}}
        """
        with open(json_file, 'r') as json_content:
            return json.load(json_content)
