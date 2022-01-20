# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from google.cloud import translate_v2 as translate
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
from scipy import spatial


states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry","India"]

model = SentenceTransformer('sentence-transformers/LaBSE')
embeddings = model.encode(states)
print("Encodings for states calculated")

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

class ActionCustom(Action):

    def name(self) -> Text:
        return "action_custom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.covid19india.org/data.json").json()
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/vatsal/Gupshup Intern/rasademo5/keen-virtue-336017-50278af04ad3.json"


        intent = tracker.latest_message['intent'].get('name')
        if intent == "greet":
            message = "Hey! Welcome To COVID-19 Stats Bot.\nYou Can Ask Me about Following Info:\n1.To Check Corona Statistics Of Your State Where You Live , Type 'Corona Tracker' or 'corona stats'\n2.What Is COVID-19?\n3.How does Corona Spread?\n4.How does food spread corona virus?\n5.Can warm weather actually stop corona?\n6.Who is more prone to get corona virus infection?\n7.About Community Spread from COVID-19\n8.Preventive Steps to be taken for COVID-19\n9.COVID-19 Symptoms Check\n10.About Vaccine Availability For COVID-19\n11.How To Handle Someone who gets in contact with infected person from COVID-19."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "mood_great":
            message = "Great, carry on!"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "mood_unhappy":
            message = "Here is something to cheer you up:"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(text=result["translatedText"])
            dispatcher.utter_message(image= "https://i.imgur.com/nGF1K8f.jpg")

            message = "Did that help you?"
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(text=result["translatedText"])


            return []

        if intent == "affirm":
            message = "Great, carry on!"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "deny":
            message = "GoodBye! Hope To See You Soon !\nJust Type 'hey' or 'hi' anytime to redirect to the Intro Section of The Bot :))"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_intro":
            message = "The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).[1] The disease was first identified in December 2019 in Wuhan, China.[4] The World Health Organization declared the outbreak a Public Health Emergency of International Concern on 30 January 2020 and a pandemic on 11 March 2020. As of 24 September 2020, more than 31.9 million cases have been reported in 188 countries and territories, resulting in more than 978,000 deaths; more than 22 million people have recovered."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_spread":
            message = "This virus was first detected in Wuhan City, Hubei Province, China. The\
                 \ first infections were linked to a live animal market, but the virus is now\
                 \ spreading from person-to-person. It’s important to note that person-to-person\
                 \ spread can happen on a continuum. Some viruses are highly contagious (like\
                 \ measles), while other viruses are less so. The virus that causes COVID-19\
                 \ is spreading from person-to-person. Someone who is actively sick with COVID-19\
                 \ can spread the illness to others. That is why we recommend that these patients\
                 \ be isolated either in the hospital or at home (depending on how sick they\
                 \ are) until they are better and no longer pose a risk of infecting others.\n\
                 How long someone is actively sick can vary so the decision on when to release\
                 \ someone from isolation is made on a case-by-case basis in consultation with\
                 \ doctors, infection prevention and control experts, and public health officials\
                 \ and involves considering specifics of each situation including disease severity,\
                 \ illness signs and symptoms, and results of laboratory testing for that patient.\n\
                 The virus that causes COVID-19 seems to be spreading easily and sustainably\
                 \ in the community (“community spread”) in some affected geographic areas. Community\
                 \ spread means people have been infected with the virus in an area, including\
                 \ some who are not sure how or where they became infected."

            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_food_spread":
            message = "It is highly unlikely that people can contract COVID-19 from food or food packaging. COVID-19 is a respiratory illness and the primary transmission route is through person-to- person contact and through direct contact with respiratory droplets generated when an infected person coughs or sneezes."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_spread_warm":
            message = "With the start of summer coming soon, many are hopeful that the warmer weather will slow the spread of SARS-CoV-2, the novel coronavirus that causes COVID-19. There have been hints from lab experiments that increased temperature and humidity may reduce the viability of SARS-CoV-2. Meanwhile, other coronaviruses that cause less severe diseases, such as the common cold, do spread more slowly among people during the summer."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_spread_risk":
            message = "COVID-19 is often more severe in people who are older than 60 years or who have health conditions like lung or heart disease, diabetes or conditions that affect their immune system.​ If you’re at high risk, know what to do, and take the right actions now to protect yourself.If you’re not at high risk, do your part to prevent the spread of coronavirus to those who are.There is increasing evidence that people with existing chronic conditions or compromised immune systems due to disability are at higher risk of death due to COVID-19."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_stats_check":
            message = "Covid-19 Tracker [India] :\nPlease Enter the State name you wish to see the Covid-19 Statistics : "
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_states_stat":
            responses = requests.get("https://api.covid19india.org/data.json").json()
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/vatsal/Gupshup Intern/rasademo5/keen-virtue-336017-50278af04ad3.json"

            entities = tracker.latest_message['entities']
            print("Now Showing Data For:", entities)
            state = None

            for i in entities:
                if i["entity"] == "state":
                    state = i["value"]
                    curremb = model.encode(state)
                    currsim = 0
                    currmax = 0
                    for j in range(len(embeddings)):
                        if (1 - spatial.distance.cosine(curremb,embeddings[j])) > currsim:
                            currsim = 1 - spatial.distance.cosine(curremb,embeddings[j])
                            currmax = j
                    
                    state = states[currmax]
                        

            message = "Please Enter Correct State Name !"

            if state == "India":
                state = "Total"
            for data in responses["statewise"]:
                if data["state"] == state.title():
                    print(data)
                    message = "Now Showing Cases For --> " + state.title() + " Since Last 24 Hours : "+ "\n" + "Active: " + data[
                        "active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data[
                                "recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n" + "As Per Data On: " + data[
                                "lastupdatedtime"]

            print(message)
            translate_client = translate.Client()
            messlanguage = tracker.get_slot("language")
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_community":
            message = "Community spread means people have been infected with the virus in an area, including some who are not sure how or where they became infected. Each health department determines community spread differently based on local conditions. For information on community spread in your area, please visit your health department’s website.​"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_mosq_spread":
            message = "At this time, CDC has no data to suggest that this new coronavirus or other similar coronaviruses are spread by mosquitoes or ticks. The main way that COVID-19 spreads is from person to person. See How Coronavirus Spreads for more information."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []
        
        if intent == "corona_prevent":
            message = "The best way to prevent illness is to avoid being exposed to the virus. CDC recommends everyday preventive actions to help prevent the spread of respiratory diseases.CDC recommends washing your hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not available, CDC recommends using an alcohol-based hand sanitizer that contains at least 60 percent alcohol.\nWear masks in public settings when around people not living in your household and particularly where other social distancing measures are difficult to maintain, such as grocery stores, pharmacies, and gas stations. Masks may slow the spread of the virus and help people who may have the virus and do not know it from transmitting it to others.COVID-19 can be spread by people who do not have symptoms and do not know that they are infected. That’s why it’s important for everyone to practice social distancing (staying at least 6 feet away from other people) and wear masks in public settings. Masks provide an extra layer to help prevent the respiratory droplets from traveling in the air and onto other people.The masks recommended are not surgical masks or N-95 respirators. Those are critical supplies that must continue to be reserved for healthcare workers and other medical first responders, as recommended by current CDC guidance."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "corona_symptoms":
            message = "COVID-19 symptoms include:\nCough\nFever or chills\nShortness of breath or \ndifficulty breathing\nMuscle or body aches\nSore throat\nNew loss of taste or smell\nDiarrhea\nHeadache\nNew fatigue\nNausea or vomiting\nCongestion or runny noseIn confirmed cases of illness in humans, common symptoms have been acute, serious respiratory illness with fever, cough, shortness of breath, and breathing difficulties. Based on current clinical experience, the infection generally presents as pneumonia. It has caused kidney failure and death in some cases. It is important to note that the current understanding of the illness caused by this infection is based on a limited number of cases and may change as more information becomes available."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []
        
        if intent == "corona_vaccine":
            message = "Human clinical trials for Covid-19 vaccine initiated in India: ICMR. Human clinical trials for a vaccine for Covid-19 have been initiated with approximately 1,000 volunteers participating in the exercise for each of the two indigenously developed vaccine candidates\nWhile some western, traditional or home remedies may provide comfort and alleviate symptoms of mild COVID-19, there are no medicines that have been shown to prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19. However, there are several ongoing clinical trials of both western and traditional medicines. WHO is coordinating efforts to develop vaccines and medicines to prevent and treat COVID-19 and will continue to provide updated information\nAt this time there is no vaccine to prevent coronavirus disease 2019 (COVID-19). The FDA is working with vaccine developers and other researchers and manufacturers to help expedite the development and availability of medical products such as vaccines, antibodies, and drugs to prevent COVID-19"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []
        
        if intent == "corona_infected person":
            message = "Stay home for 14 days after your last contact with a person who has COVID-19.\nBe alert for symptoms. Watch for fever, cough, shortness of breath, or other symptoms of COVID-19.\nIf possible, stay away from others, especially people who are at higher risk for getting very sick from COVID-19."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []
        
        if intent == "Thanks":
            message = "Your Welcome . Glad I could be of some help!\nJust type 'hey' or 'hi' again to redirect to the main phase of bot ! :))"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "bot_challenge":
            message = "I am a COVID-19 Stats bot, Developed By Harsh Sharma."
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

        if intent == "goodbye":
            message = "GoodBye! Hope To See You Soon !\nJust Type 'hey' or 'hi' anytime to redirect to the Intro Section of The Bot :))"
            messlanguage = tracker.get_slot("language")
            translate_client = translate.Client()
            result = translate_client.translate(message, target_language=messlanguage)

            dispatcher.utter_message(result["translatedText"])

            return []

class ActionHelloLoc(Action):

    def name(self) -> Text:
        return "action_get_loc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_name = tracker.get_slot("state")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/vatsal/Gupshup Intern/rasademo5/keen-virtue-336017-50278af04ad3.json"
        print("slotname", slot_name)

        message="So You Live In " + slot_name.title() + " , Here Are Your Location's Corona Stats: \n"
        messlanguage = tracker.get_slot("language")
        translate_client = translate.Client()
        result = translate_client.translate(message, target_language=messlanguage)

        dispatcher.utter_message(result["translatedText"])

        return []

class Actioncoronastats(Action):

    def name(self) -> Text:
        return "actions_corona_state_stat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.covid19india.org/data.json").json()
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/vatsal/Gupshup Intern/rasademo5/keen-virtue-336017-50278af04ad3.json"

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        state = None

        for i in entities:
            if i["entity"] == "state":
                state = i["value"]
                curremb = model.encode(state)
                currsim = 0
                currmax = 0
                for j in range(len(embeddings)):
                    if (1 - spatial.distance.cosine(curremb,embeddings[j])) > currsim:
                        currsim = 1 - spatial.distance.cosine(curremb,embeddings[j])
                        currmax = j
                
                state = states[currmax]
                    

        message = "Please Enter Correct State Name !"

        if state == "India":
            state = "Total"
        for data in responses["statewise"]:
            if data["state"] == state.title():
                print(data)
                message = "Now Showing Cases For --> " + state.title() + " Since Last 24 Hours : "+ "\n" + "Active: " + data[
                    "active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data[
                              "recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n" + "As Per Data On: " + data[
                              "lastupdatedtime"]

        print(message)
        translate_client = translate.Client()
        messlanguage = tracker.get_slot("language")
        result = translate_client.translate(message, target_language=messlanguage)

        dispatcher.utter_message(result["translatedText"])

        return []





