# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class AnswerQuestion(Action):
    def name(self) -> Text:
        return "Answer"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ent = tracker.latest_message['entities']
        intent = tracker.latest_message['intent']
        if intent['confidence'] < 0.8:
            dispatcher.utter_message(text=f"Pertanyaan tidak terdata dalam dataset")
        else:
            entry = "ENTITIES\n"
            count = int(0)
            for f in ent:
                entry += str(count+1) + ". " + "ENTITY = " + str(f['entity']) + ". CONFIDENCE ENTITY = " + str(f['confidence_entity']) + ". VALUE ENTITY = " + str(f['value']) + "\n"
                count = count+1
            entry += "INTENT\n" + "1. INTENT NAME = " + str(intent['name']) + ". INTENT CONFIDENCE = " + str(intent['confidence'])
            dispatcher.utter_message(text=f"{entry}")
            # dispatcher.utter_message(text=f"{ent}")
            # dispatcher.utter_message(text=f"{intent}")

        return []
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
