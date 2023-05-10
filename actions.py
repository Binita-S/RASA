from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRecommendUniversity(Action):
    def name(self) -> Text:
        return "action_recommend_university"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        course = tracker.latest_message.get('entities')[0].get('value')
        
        if course == "engineering":
            dispatcher.utter_message(text="The best universities for engineering are MIT, Stanford and Caltech.")
        elif course == "medicine":
            dispatcher.utter_message(text="The best universities for medicine are Harvard, Johns Hopkins and Stanford.")
        elif course == "law":
            dispatcher.utter_message(text="The best universities for law are Harvard, Yale and Stanford.")
        else:
            dispatcher.utter_message(text="Sorry, I'm not sure which universities are best for that course.")
        
        return []

