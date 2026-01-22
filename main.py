import time
import asyncio
import platform 

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

Schedular_ID = "Scheduler@jabbim.com"    
Schedular_PWD = "Truva4512"

CLIENT_ID = "RequestSender@jabbim.com"     
CLIENT_PWD = "Truva4512"




#  AGENT 1: SCHEDULER 
class SchedularAgent(Agent):
    class ListenBehaviour(CyclicBehaviour):
        async def run(self):
            print("Schedular: Waiting for messages... (Connected to server)")
            
            msg = await self.receive(timeout=60) 

            if msg:
                print(f"Schedular: Message received! -> '{msg.body}'")
                
                busy_slots = ["09:00", "13:00", "15:00"]
                
                if msg.body in busy_slots:
                    reply_content = "BUSY: That time slot is already taken."
                else:
                    reply_content = "FREE: Slot available. Appointment booked."

                reply = Message(to=str(msg.sender))
                reply.body = reply_content
                await self.send(reply)
                
                print(f"Schedular: Reply sent -> {reply_content}")
            else:
                pass 

    async def setup(self):
        print("System: Starting Schedular Agent...")
        self.add_behaviour(self.ListenBehaviour())

# AGENT 2: CLIENT 
class ClientAgent(Agent):
    class AskBehaviour(OneShotBehaviour):
        async def run(self):
            print("Client: Waiting 5 seconds before asking...")
            await asyncio.sleep(5) 

            print("Client: Sending request for 13:00...")
            msg = Message(to=Schedular_ID)
            msg.body = "13:00"

            await self.send(msg)
            print("Client: Message sent! Waiting for reply...")

            response = await self.receive(timeout=60)
            if response:
                print(f"Client: GOT REPLY! -> {response.body}")
            else:
                print("Client: No reply received (Timeout).")
            
            await self.agent.stop()

    async def setup(self):
        print("System: Starting Client Agent...")
        self.add_behaviour(self.AskBehaviour())

async def main():
    Schedular = SchedularAgent(Schedular_ID, Schedular_PWD)
    await Schedular.start()
    print("System: Schedular is active.")

    client = ClientAgent(CLIENT_ID, CLIENT_PWD)
    await client.start()
    print("System: Client is active.")

    while client.is_alive():
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break
    
    await Schedular.stop()
    print("System: Process finished.")

if __name__ == "__main__":
    asyncio.run(main())