from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import asyncio

# Define data models
class ASI1miniRequest(Model):
    query: str

class ASI1miniResponse(Model):
    response: str

# Initialize the agent
agent = Agent(name="Test", seed="test asi mini req", port=8001, mailbox=True)
fund_agent_if_low(agent.wallet.address())

ASI1_MINI_ADDRESS = "agent1qvn0t4u5jeyewp9l544mykv639szuhq8dhmatrgfuwqphx20n8jn78m9paa"

# List of questions to ask
questions = [
    "What are the fundamental principles of AI?",
    "How does backpropagation work in neural networks?",
    "What is the role of bias and variance in machine learning?",
    "How do convolutional neural networks process images?",
    "What are the differences between classification and regression?",
    "How does AI affect digital privacy?",
    "What is ensemble learning in machine learning?",
    "How do recurrent neural networks handle sequential data?",
    "What are the applications of AI in gaming?",
    "How is AI used in fraud detection?",
    "What is the relationship between big data and AI?",
    "How do genetic algorithms solve optimization problems?",
    "What are the implications of AI for intellectual property?",
    "How does natural language generation work?",
    "What is the role of AI in autonomous weapons systems?",
    "How do sentiment analysis systems work?",
    "What are the challenges in AI ethics?",
    "How does AI impact democratic processes?",
    "What is the mathematics behind machine learning?",
    "How do AI systems handle uncertainty?",
    "What are the applications of AI in environmental monitoring?",
    "How is AI used in predictive policing?",
    "What is the role of AI in content moderation?",
    "How do knowledge graphs enhance AI systems?",
    "What are the philosophical questions raised by AI?",
    "How do AI systems learn causal relationships?",
    "What is the impact of AI on global inequality?",
    "How do neural networks approximate functions?",
    "What are the applications of AI in legal systems?",
    "How is AI changing journalism?",
    "What is the role of dataset bias in AI development?",
    "How do reinforcement learning agents explore environments?",
    "What are the applications of AI in sports analytics?",
    "How is AI used in mental health care?",
    "What is the difference between model-free and model-based learning?",
    "How do AI systems understand context?",
    "What are the applications of AI in energy management?",
    "How is AI used in wildlife conservation?",
    "What is the role of generative models in content creation?",
    "How do AI systems deal with adversarial attacks?",
    "What are the applications of AI in transportation logistics?",
    "How is AI changing educational assessment?",
    "What is the impact of AI on labor rights?",
    "How do AI systems learn from human demonstrations?",
    "What are the applications of AI in urban planning?",
    "How is AI used in archaeological research?",
    "What is the role of feature engineering in machine learning?",
    "How do AI systems handle multilingual problems?",
    "What are the applications of AI in public health surveillance?",
    "How is AI changing scientific publishing?",
    "What is the impact of AI on childhood development?",
    "How do AI systems perform reasoning tasks?",
    "What are the applications of AI in water management?",
    "How is AI used in protein folding prediction?",
    "What is the role of AI in augmented reality?",
    "How do AI systems handle noisy data?",
    "What are the applications of AI in fashion and design?",
    "How is AI changing political campaigning?",
    "What is the impact of AI on international relations?",
    "How do AI systems perform visual recognition?",
    "What are the applications of AI in marine science?",
    "How is AI used in language preservation?",
    "What is the role of human-centered design in AI development?",
    "How do AI systems generate synthetic speech?",
    "What are the applications of AI in tax compliance?",
    "How is AI changing personal finance?",
    "What is the impact of AI on privacy laws?",
    "How do AI systems perform optical character recognition?",
    "What are the applications of AI in music composition?",
    "How is AI used in epidemic forecasting?",
    "What is the role of AI in virtual reality?",
    "How do AI systems learn from human preferences?",
    "What are the applications of AI in construction?",
    "How is AI changing advertising?",
    "What is the impact of AI on economic mobility?",
    "How do AI systems perform semantic segmentation?",
    "What are the applications of AI in disaster prediction?",
    "How is AI used in cultural heritage preservation?",
    "What is the role of edge computing in AI deployment?",
    "How do AI systems learn hierarchical representations?",
    "What are the applications of AI in insurance?",
    "How is AI changing waste management?",
    "What is the impact of AI on global cooperation?",
    "How do AI systems perform time series forecasting?",
    "What are the applications of AI in mining?",
    "How is AI used in elections monitoring?",
    "What is the role of AI in personalized nutrition?",
    "How do AI systems handle concept drift?",
    "What are the applications of AI in forestry?",
    "How is AI changing elderly care?",
    "What is the impact of AI on digital literacy?",
    "How do AI systems perform object tracking?",
    "What are the applications of AI in humanitarian aid?",
    "How is AI used in geological exploration?",
    "What is the role of AI in social simulations?",
    "How do AI systems perform document understanding?",
    "What are the applications of AI in tourism?",
    "How is AI changing philanthropy and nonprofits?"
]

# Track which question to send next
current_question_index = 0

@agent.on_interval(period=10)
async def send_next_question(ctx: Context):
    global current_question_index
    
    # Check if we have questions left to send
    if current_question_index < len(questions):
        question = questions[current_question_index]
        ctx.logger.info(f"Sending question {current_question_index + 1}: {question}")
        
        # Send the current question
        await ctx.send(ASI1_MINI_ADDRESS, ASI1miniRequest(query=question))
        
        # Increment the index for the next interval
        current_question_index += 1
    else:
        ctx.logger.info("All questions have been sent")

@agent.on_message(model=ASI1miniResponse)
async def handle_response(ctx: Context, sender: str, msg: ASI1miniResponse):
    # Log the response with the question number
    response_index = current_question_index - 1  # The response is for the most recently sent question
    ctx.logger.info(f"Response for question {response_index + 1}:")
    ctx.logger.info(msg.response)

if __name__ == "__main__":
      agent.run()
