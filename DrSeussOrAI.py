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
            {"role": "user", "content": "Write a fake quote in the style of Dr. Seuss. Do NOT include any hashtags or quotation marks. Make sure it is under 256 characters."}
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
        tweet_text = "This Dr. Seuss quote was AI-generated!"
    else:
        tweet_text = "This is a real Dr. Seuss quote!"
    client.create_tweet(in_reply_to_tweet_id=tweet_id, text = tweet_text)

dr_seuss_quotes_index = -1
dr_suess_quotes = [
"When beetles fight these battles in a bottle with their paddles and the bottle's on a poodle and the poodle's eating noodles...they call this a muddle puddle tweetle poodle beetle noodle bottle paddle battle.",
"Through three cheese trees three free fleas flew. While these fleas flew, freezy breeze blew. Freezy breeze made these three trees freeze, Freezy trees made these trees' cheese freeze, That's what made these three free fleas sneeze.",
"In bed is where I'm going to stay. And I don't care what the neighbors say! I never liked them anyway. Let them try to wake me. Let them scream and yowl and yelp. They can yelp from now until Christmas but it isn't going to help.",
"And when you're alone, there's a very good chance you'll meet things that scare you right out of your pants. There are some, down the road between hither and yon, that can scare you so much you won't want to go on.",
"You will come to a place where the streets are not marked. Some windows are lighted, but mostly they're darked.", "A place you could sprain both your elbow and chin! Do you dare to stay out? Do you dare to go in? How much can you lose? How much can you win?"
"That's why I say, 'Duckie! Don't grumble! Don't stew! Some critters are much-much, oh, ever so much-much, so muchly much-much more unlucky than you!'",
"Thank goodness for all the things you are not! Thank goodness you're not something someone forgot, and left all alone in some punkerish place like a rusty tin coat hanger hanging in space.",
"'This is called teamwork. I furnish the brains. You furnish the muscles, the aches and the pains. I'll pick the best roads, tell you just where to go, And we'll find a good doctor more quickly, you know.'",
"If you never did, you should. These things are fun, and Fun is good.",
"'You're going to be roped! And you're going to be caged! And, as for your dust speck - hah! That we shall boil in a hot steaming kettle of Beezle-Nut Oil!'",
"Always remember you are braver than you believe, stronger than you seem, smarter than you think and twice as beautiful as you've ever imagined.",
"There are points to be scored. There are games to be won. And the magical things you can do with that ball will make you the winning-est winner of all.",
"The storm starts, when the drops start dropping. When the drops stop dropping then the storm starts stopping.",
"Some people are much more… oh, ever so much more… oh, muchly much-much more unlucky than you!",
"How did it get so late so soon? It's night before it's afternoon. December is here before it's June. My goodness how the time has flewn. How did it get so late so soon?",
"Fantasy is a necessary ingredient in living. It's a way of looking at life through the wrong end of a telescope.",
"'I've heard there are troubles of more than one kind; some come from ahead, and some come from behind. But I've brought a big bat. I'm all ready, you see; now my troubles are going to have troubles with me!'",
"'You'll get mixed up, of course, as you already know. You'll get mixed up with many strange birds as you go.",
"So be sure when you step. Step with care and great tact and remember that life's a great balancing act. Just never forget to be dexterous and deft. And never mix up your right foot with your left.'",
"'Some days are yellow. Some are blue. On different days I'm different too.'",
"Then he grunts, 'I will call you by Whisper-Ma-Phone, for the secrets I tell are for your ears alone.'",
"If you read with your eyes shut you're likely to find that the place where you're going is far, far behind.",
"Then they yelled at the ones that had stars at the start. 'We're exactly like you! You can't tell us apart. We're all just the same, now, you snooty old smarties! And now we can go to your frankfurter parties.'",
"And it klonked. And it bonked. And it jerked. And it berked. And it bopped them about. But the thing really worked!",
"Not one of them is like another. Don't ask us why. Go ask your mother.",
"From sun in the summer. From rain when it's fallish, I'm going to protect them. No matter how small-ish!",
"They've proved they ARE persons, no matter how small. And their whole world was saved by the Smallest of All!",
"He will live at our house. He will grow and grow. Will our mother like this? We don't know.",
"From east of the East-est to west of the West-est we've searched the whole world just to bring you the best-est.",
"Because, after your party, as well you may guess, it will take twenty days just to sweep up the mess.",
"Unless someone like you cares a whole awful lot, nothing is going to get better. It's not.",
"Feet in the morning. Feet at night. Left foot, left foot, left foot, right. Wet foot, dry foot. High foot, low foot.",
"I can read in red. I can read in blue. I can read in pickle color too.",
"Simple it's not, I am afraid you will find, for a mind-maker-upper to make up his mind.",
"They say I'm old-fashioned, and live in the past, but sometimes I think progress progresses too fast!",
"If you'd never been born, then you might be an Isn't! An Isn't has no fun at all. No, he didn't!",
"Think left and think right and think low and think high. Oh, the thinks you can think up if only you try!",
"And will you succeed? Yes indeed, yes indeed! Ninety-eight and three-quarters percent guaranteed!",
"Unless someone like you cares a whole awful lot. Nothing is going to get better. It's not."
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
tweet_output = tweet_quote(dr_seuss_quotes_index, dr_suess_quotes)
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
            tweet_output = tweet_quote(dr_seuss_quotes_index, dr_suess_quotes)

            AI_tweet = tweet_output[0]
            tweet_id = tweet_output[1]
            time.sleep(3600)
            tweet_AI_or_real_reply(AI_tweet, tweet_id)

            initial_datetime = curr_datetime


        time.sleep(1)
    except:
        print("Twitterbot DrSeussOrAI error occured!")
       
       