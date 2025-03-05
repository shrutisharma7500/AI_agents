from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low


class WebsiteSummarizerRequest(Model):
    url: str


class WebsiteSummarizerResponse(Model):
    text: str

# Initialize the local agent
agent = Agent(
    name="local_agent",
    seed="testing",
    port=8000, 
    mailbox=True,
)
fund_agent_if_low(agent.wallet.address())

AGENTVERSE_AGENT_ADDRESS = "agent1qthlkqd9y2dz3twzgx4vyyvesxf8n875cwh2pg95nd69wd6rckzaq5yvlhc"

@agent.on_event("startup")
async def send_message(ctx: Context):
    
    website_url=input("enter the website you want to summarize :")
    await ctx.send(AGENTVERSE_AGENT_ADDRESS, WebsiteSummarizerRequest(url=website_url))
    ctx.logger.info(f"Sent request for scraping the Website: {website_url}")




agent.on_message(WebsiteSummarizerResponse)
async def handle_summary(ctx: Context, sender: str, msg: WebsiteSummarizerResponse):
    try:
        ctx.logger.info(f"Received WebsiteSummarizerResponse from {sender[-10:]}")
        ctx.logger.info(f"Summarized text: {msg.text}")
    except Exception as e:
        ctx.logger.error(f"Error in handle_summary: {e}")

if __name__ == "__main__":
    agent.run()