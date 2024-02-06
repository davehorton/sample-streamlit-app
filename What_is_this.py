import streamlit as st

st.set_page_config(
    page_title="LLM Conversational Response Classifier",
    layout='wide'
)

st.header("Making voicebots not suck")
st.write("""
Yes, we can talk to AI. Connecting a speech driven interface to AI is easy. 

But crafting a conversational experience that approaches the ease and pleasure of a human conversation is hard.

One reason for this is that today's speech recognition systems are not good at detecting the turn of a conversation.

As humans, we're super good at this.  We continually process all sorts of cues during a conversation
to determine when our partner has indicated they are done speaking.  For instance:

- our speaking partner asked us a question so we know it's time for us to respond (and think about how easy it is for us to 
         distinguish a rhetorical question, which is not something we should respond to),
- our speaking partner starts by saying "it's a long story.." and we settle in to wait longer for our turn to speak, or
- our partner may pause during speech, but we know it is a "thinking" or a "bridge" pause with more to come ("Yeeeah.....well, it's not that simple, my friend")

In a conversation with AI the ASR will frequently return a fragment of what the user said, and when we feed that partial
response to the AI the conversation is quickly derailed.  If on the other hand we simply wait an extra long time to be sure the user 
has finished speaking, this creates a stilted conversation that is an even worse experience

Lets' use AI to help us predict the turn of conversation.

In this example, we use an LLM to predict the type of response a caller may make to a given statement or question from a voicebot.
Based on that prediction we can then tune the ASR for this part of the conversation to give ourselves the best chance of collecting a full and
meaningful response from the user efficiently.
""")

st.session_state.prefix = """You are monitoring conversations in a call center between an agent and a customer.
Your job is to listen to what the agent says and then predict the nature of the subsequent response from the customer.

You will then classify your prediction of the expected response from the customer as one of the following: 
single utterance, single sentence, multiple sentences, or identification data.

## Classification metric

single utterance

Return this when the response is extremely likely to be only one or two words. Generally, return this only when the agent has just asked a yes/no type of question of the customer.

single sentence

Return this when the response is likely to be short, but more than a single word or two.  Examples include when the expected response to the statement is a command or a short clarifying response to the agent's statement.  This response should also be returned if the agent just offered the customer a range of 2-5 options and the customer is expected to select one of them.

multiple sentences

Return this when the response is likely to be more than a single sentence, but less than a paragraph or two.  Examples include when the statement from the agent may encourage the customer to provide additional supporting or background information in addition to a direct response.

identification data 

Return this any time the response is likely to spoken data for identification purposes, such as a postal address, an email address, a phone number, a credit card number, a personal identifier, a license plate etc. This response should always be returned in preference to the others if the response is deemed likely to return identification data.

## Steps to use:

1. Evaluate the statement made by the agent in terms of whether it can be answered simply or not.  Pay attention to questions that are likely to require more detail, or that are worded in a way that may encourage the customer to broaden the conversation to other topics.

2. If the question can be answered simply, then consider whether the response is likely to include a person's name or other identification data, because if so you should classify the response as 'identification data' even though the question is a simple one.

3. Keep in mind that agent and customer are speaking by phone and as such some shorthand may be used: i.e. "call" may mean "phone call" and "number" could mean "phone number".

After performing these steps return the classification choice as an unformatted JSON format as an object with 'classification' and 'reason' properties.
"""


st.session_state.examples = """statement: Would you like me to go ahead and book the flight for you?
classification: single utterance
reason: The agent is asking a yes/no question.  Since the flight is apparently ready to be booked, it implies that a lot of information such as departure city, time, and airline company have already been confirmed.  This sounds like a final prompt to simply confirm the customer wishes to proceed.

statement: This call may be recorded for quality purposes.  Am I speaking to Thomas C. Jones of 59 Locust Lane?
classification: single utterance
reason: The agent is asking a simple yes/no question.

statement: Thank you for reaching out to our support team. How can we assist you today?
classification: multiple sentences
reason: The agent has asked a very open-ended question.

statement: Our technician has availability at 10AM, 2PM, or 4PM.  Would one of these times work for you?
classification: single sentence
reason: The agent has offered a small set of choices and is asking the customer to choose one.

statement: Please tell me the name of the patient requesting service
classification: identification data
reason: The agent is asking the customer to speak a person's name, which is identification data.

statement: Would you like me to initiate the return process for you?
classification: single utterance
reason: The agent has asked a yes/no question.

statement: Can you tell me the day and month of your birth?
classification: identification data
reason: The agent has asked the customer to speak parts of a date, which is identification data.

statement: I'd be happy to book a flight for you, provide the status of a flight, or answer other questions you may have.  What can I do for you today?
classification: single sentence
reason: The agent has asked an open-ended question but has also tried to guide the customer to select from a small set of choices.
"""

