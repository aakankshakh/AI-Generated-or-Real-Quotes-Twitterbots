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
            {"role": "user", "content": "Write a fake quote in the style of Elon Musk Do NOT include any hashtags or quotation marks. Make sure it is under 256 characters."}
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
        tweet_text = "This Elon Musk quote was AI-generated!"
    else:
        tweet_text = "This is a real Elon Musk quote!"
    client.create_tweet(in_reply_to_tweet_id=tweet_id, text = tweet_text)

musk_quotes_index = -1
musk_quotes = [
"Life is too short for long-term grudges.",
"I didn`t really expect to make any money. If I could make enough to cover the rent and buy some food that would be fine. As it turns out, it turned out to be quite valuable in the end.",
"I don`t have an issue with serving in the military per se, but serving in the South African army suppressing black people just didn`t seem like a really good way to spend time.",
"I think South Africa is a great country.",
"If you wanted to be close to the cutting edge, particularly in technology, you came to North America.",
"Tuition costs are outrageous. Fortunately, they gave me a scholarship…so I only had to cover living expenses, books, etc., by working.",
"One was the Internet, one was clean energy and one was space.",
"I could either watch it happen, or be part of it.",
"We could figure out ways with small aerospace companies to do a low-cost spacecraft and lander. But we could not find a way to do a low-cost launcher, unless we went to the Russians.",
"The answer was we thought it could be done.",
"There is nothing inherently expensive about rockets. It's just that those who have built and operated them in the past have done so with horrendously poor efficiency.",
"Falcon One is going to be the lowest cost per flight to orbit of any production rocket.",
"Which means we`re cheaper than the Chinese, cheaper than [the] Russians or anywhere else--and we`re doing it in the United States with American labour costs.",
"I think the reason it`s cheaper is, first of all, we are a private entity and we have a very lean system in here. What we have been able to do here at SpaceX is to cherry-pick, you know, the top one or two percent and give them, you know, capital to execute well and a clear mission, which is low cost, reliable access to space, and no other constraints.",
"Well, I have tried to learn as much as possible from prior attempts.",
"If nothing else, we are committed to failing in a new way.",
"There`s a graveyard of prior attempts, a big graveyard. There`s probably some freshly dug graves just waiting to be filled. Our aspiration is to avoid that destination.",
"I think we`ve got the risks pretty well characterized. I think we are at least avoiding the mistakes that have been made in the past.",
"I think the rocket business is quite cyclic. There are a great many peaks and troughs.",
"Imagine creating a huge software program that can only be tested in little pieces on a computer that is slightly different from what it is supposed to run on. However, when you do run it as a whole on the actual computer for the first time, it must run almost flawlessly without a single significant bug. When is the last time you saw a software program do that?",
"When thinking about starting a business, I think it`s actually better to start in a trough and come to market in a peak, than the other way around. Frankly, if anything does, and it`s almost cliché, space has a long-term future.",
"I want to be able to make sure that we have enough capital to survive at least three consecutive failures. If you want to make a small fortune in the launch vehicle business, start with a large one.",
"The long term ultimate objective--the holy grail--is we would like to help make life multi-planetary.",
"We got to the moon, but have never done anything better since. I'm disappointed that we have not made more progress since Apollo. I don't even see a plan that says we're going to do better than Apollo to exceed that goal.",
"I like to be involved in things that change the world. The Internet did, and space will probably be more responsible for changing the world than anything else. If humanity can expand beyond the Earth, obviously that's where the future is.",
"If we can be one of the companies that makes it possible for humans to become a multi-planetary species, that would be the Holy Grail. It sounds a bit crazy but it's going to happen, and only if people build the means to do so. We're making progress toward a greater philosophical goal while building a sound business.",
"When Henry Ford made cheap, reliable cars people said, 'Nah, what's wrong with a horse?' That was a huge bet he made, and it worked.",
"It doesn`t do a great deal to advance the goal of humanity. I would pay $20 million not to spend six months in Russia. And besides this, my interest is how do we enable many other people to go to space, not necessarily me, personally.",
"If we can build something that is capable of taking people and equipment to Mars, such that it can service a transportation infrastructure for humanity becoming a multi- planet species - which I think is a very, very important objective - then I would consider the mission of SpaceX successful, at that point.",
"We are used to things improving every year; we are used to having a better cell phone next year than this year; a better lap top. We are even used to some basic things, like we expect more from your car in next year`s model than last year`s model.",
"...in space reliability and cost--those are the fundamental parameters of transportation--have not improved.",
"Starting and growing a business is as much about the innovation, drive and determination of the people who do it as it is about the product they sell.",
"So even if a fire develops, it can't really attack the particularly vulnerable locations like the pneumatic system or the avionics or the engine bay. We want to be in the situation that even if a fire develops, the rocket just keeps going.",
"A great deal of bargaining power with suppliers. We are never locked in to anyone.",
"I think it is a mistake to hire huge numbers of people to get a complicated job done. Numbers will never compensate for talent in getting the right answer (two people who don't know something are no better than one), will tend to slow down progress, and will make the task incredibly expensive.",
"My approach is simply to seek out very talented people, ensure that the environment at SpaceX is as motivating & enjoyable as possible and establish clear & measurable objectives.",
"Rocket engineering is not like ditch digging. With ditch digging you can get 100 people and dig a ditch, and you will dig it a hundred times as faster if you get 100 people versus one. With rockets, you have to solve the problem of a particular level of difficulty; one person who can solve the problem is worth an infinite number of people who can`t.",
"I think that is a mistake and results in cloudy judgment on important technical issues. They can't tell if something is really good or not, so they just do what everyone else does, assuming it to be the safe bet.",
"Although I am new in the business, my team is not. I would say that, person for person, there has never been a better rocket company in existence, in history. I don`t think there has ever been a group this talented in one place, in one company, developing a rocket--ever.",
"This is the chance to fulfill a dream.",
"I`m nauseatingly pro-American. It is where great things are possible.",
"As life`s agents, it`s on our shoulders.",
"Sooner or later, we must expand life beyond our little blue mud ball--or go extinct.",
"When something is important enough, you do it even if the odds are not in your favor.",
"I'd rather be optimistic and wrong; than pessimistic and right.",
"I would like to die on Mars; just not on impact.",
"Even if there's a zombie apocalypse, you'll still be able to travel using the Tesla Supercharging system.",
"Getting to Mars is too big an accomplishment for us to feel proud by just by swinging by. We are a nation of enterprise as well as exploration, and we're not about to go there without making something of it.",
"AI is much more advanced than people realize. ... Humanity's position on this planet depends on its intelligence so if our intelligence is exceeded, it's unlikely that we will remain in charge of the planet.",
"Every person in your company is a vector. Your progress is determined by the sum of all vectors.",
"I don`t get the little ship thing. You can`t show up at Mars in something the size of a rowboat. What if there are Martians? It would be so embarrassing."
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
tweet_output = tweet_quote(musk_quotes_index, musk_quotes)
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
            tweet_output = tweet_quote()

            AI_tweet = tweet_output[0]
            tweet_id = tweet_output[1]
            time.sleep(3600)
            tweet_AI_or_real_reply(AI_tweet, tweet_id)

            initial_datetime = curr_datetime


        time.sleep(1)
    except:
        print("Twitterbot MuskOrAI error occured!")
       
       