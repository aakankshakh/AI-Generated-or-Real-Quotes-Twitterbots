#!/usr/bin/env python3
import tweepy
import random
import openai
import datetime
import time


def useAI():
    num = random.randint(0,1)
    print('BOOLEAN', num)
    if num == 0:
        return True #representing AI generated text
    return False

def generate_AI_text():
    openai.api_key = "enter your key here"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a fake Florida news headline. Do NOT include any hashtags or quotation marks. Make sure it is under 256 characters."}
        ],
    temperature = 0.8
    )

    output_text = response['choices'][0]['message']['content']
    return output_text


def get_real_text(quotes_index: int, quotes: list):
    quotes_index += 1
    if quotes_index < len(quotes):
        return quotes[quotes_index]
    return ""

def tweet_quote(quotes_index: int, quotes: list):
    tweet_text = ""
    currChoice = useAI()

    if (currChoice):
        tweet_text = generate_AI_text()
    else:
        tweet_text = get_real_text(quotes_index, quotes)
    
    print("tweet:",tweet_text)
    tweet = client.create_tweet(text = tweet_text)
    tweet_id = tweet.data["edit_history_tweet_ids"][0]
    return [currChoice, tweet_id]

def tweet_AI_or_real_reply(AI_quote: bool , tweet_id: str):
    tweet_text = ""
    if (AI_quote):
        tweet_text = "This Florida headline quote was AI-generated!"
    else:
        tweet_text = "This is a real Florida headline quote!"
    client.create_tweet(in_reply_to_tweet_id=tweet_id, text = tweet_text)

florida_headlines_index = -1
florida_headlines = [
"`Dr. Love`, Florida man who faked being teen doctor, is arrested again",
"Man steals entire stacks of lottery tickets, returns in new clothes to steal safe",
"Man steals gator from Florida golf course, tosses it around to `teach it a lesson`",
"Man sprays bear repellent inside Florida Bath & Body Works; dozens injured, police say",
"`I think it is sending a message`: Florida man fills pothole with banana tree",
"Man uses trash can to capture alligator",
"Man wielding sword sets fire in roadway, floods booking office after arrest, police say",
"Man tried robbing Waffle House with finger guns, sheriff says",
"Man flashes buttocks at IHOP after impersonating a police officer to get free food",
"Drunk man attempts to ride bike through Taco Bell drive-thru, fights with police",
"Man steals 850 pairs of underwear from Victoria's Secret",
"Man arrested for smoking pot in hospital maternity ward",
"Florida man arrested after urinating on in-law's carpet during Thanksgiving gathering",
"Florida Man Arrested Outside of Olive Garden After Eating Pasta Belligerently",
"Vacationers Find Alligator Lounging on Alligator Pool Float at Their Miami Airbnb",
"Fake Cop Pulls Over Real Cop on I-4, Gets Arrested",
"Mom Arrested After Letting Children Ride in an Inflatable Pool on Top of a Vehicle",
"Florida Man resists arrest while dressed in Boy Scout costume",
"Tar-smeared Florida Man arrested on convenience store roof at 3 a.m",
"Naked Florida Man captured after threatening passers-by with sword",
"Florida Man sentenced to prison for attempting to start 'race war' near Disney World",
"Florida Man proposes to girlfriend, ties ring to alligator",
"Car runs over turtle, propels it through another driver's windshield on I-4",
"Police: Bus passenger punched for yawning, suspect felt 'disrespected'",
"Police tase, arrest Pokemon Go player after he refuses to leave park",
"Florida suspect uses his own wanted poster as Facebook profile picture",
"Drunk, High Florida Men Post Video to Facebook of Themselves Driving Around at 3 AM with Wounded, Possibly Endangered Owl",
"Florida Man on Bath Salts Head-Butts Car, Slaps Fire Chief",
"Identical Twin Florida Men Arrested After Getting in Brick Fight",
"82-Year-Old Florida Man Slashes 88-Year-Old Florida Woman's Tires with an Ice Pick for Taking His Seat at Bingo",
"Florida Man Dances on Top of Police Cruiser to Ward Off Vampires",
"Crack-Smoking Florida Man Drinks Capri Sun to Rehydrate During Police Chase",
"Florida Man Flees Library on Scooter After Smelling Woman's Feet",
"Florida man once arrested for fighting drag queen with tiki torch runs for mayor",
"Florida man tries to evade arrest by cartwheeling away from cops",
"Florida Man Launches Chair at Mailman Because He Had No Mail For Him",
"Florida Man Bites Off Neighbor's Ear Because He Wouldn't Give Him a Cigarette",
"Florida Man Tries To Avoid Court Appearance By Claiming He Has Ebola",
"Hardware Store Discards 15-Feet of Carpet After Florida Man Rolls Himself Up In It and Pees",
"Florida Man Arrested For Calling 911 After His Cat Was Denied Entry To Strip Club"
]


# keys removed for privacy purposes
# create your own by making a twitter developer profile
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#tweet = client.create_tweet(text = "test!")
#print(tweet)

initial_datetime = datetime.datetime.now()
print("starting tweet creation...")
#Tweeting an initial quote and reply
tweet_output = tweet_quote(florida_headlines_index, florida_headlines)
print("tweet twoted!")
AI_tweet = tweet_output[0]
tweet_id = tweet_output[1]

time.sleep(3600)
tweet_AI_or_real_reply(AI_tweet, tweet_id)

while True:
    try:
        curr_datetime = datetime.datetime.now()
        hours_passed = curr_datetime.hour - initial_datetime.hour

        if (hours_passed == 2):
            print('New tweet alert!')
            tweet_output = tweet_quote(florida_headlines_index, florida_headlines)

            AI_tweet = tweet_output[0]
            tweet_id = tweet_output[1]
            time.sleep(3600)
            tweet_AI_or_real_reply(AI_tweet, tweet_id)

            initial_datetime = curr_datetime


        time.sleep(1)
    except:
        print("Twitterbot FloridaOrAI error occured!")