from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionServiceInfo(Action):
    def name(self) -> str:
        return "action_service_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        dispatcher.utter_message(text="We automate workflows, customer support, and marketing pipelines.")
        return []