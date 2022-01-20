from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
from rasa_sdk.events import SlotSet


import time
from google.cloud import translate_v2 as translate
import os


class LanguageDetector(Component):
    """A pre-trained language detect component"""


    name = "language"
    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en"]


    def __init__(self, component_config=None):
        super(LanguageDetector, self).__init__(component_config)


    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass






    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""
        
        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "language",
                  "extractor": "language_extractor"}


        return entity




    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/vatsal/Gupshup Intern/rasademo5/keen-virtue-336017-50278af04ad3.json"

        
        if message.get('text')!=None:

            begin = time.time()
            translate_client = translate.Client()

            result = translate_client.translate(message.get('text'), target_language="en")
            end = time.time()

            entity = self.convert_to_rasa(result["detectedSourceLanguage"], 1)
            message.set("entities", [entity], add_to_output=True)

        else:
            pass

            