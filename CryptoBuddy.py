#Define the new class CryptoBuddy
class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            },
            "Solana": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "low",
                "sustainability_score": 7/10
            },
            "Polkadot": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10
            },
            "Avalanche": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            },
            "Polygon": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10
            },
            "Chainlink": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 6/10
            },
            "Cosmos": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            },
            "Tezos": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 9/10
            },
            "Algorand": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 9/10
            },
            "Stellar": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            },
            "Hedera": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            }
        }
    
    def greet(self):
        print(f"Hi there! I'm {self.name}, your friendly cryptocurrency advisor. How can I help you today?")
        print("You can ask me about trending cryptos, sustainable coins, or general investment advice.")
        print("Type 'quit' to exit.\n")
    
    def handle_trend_query(self):
        trending_coins = [coin for coin in self.crypto_db 
                         if self.crypto_db[coin]["price_trend"] == "rising"]
        if trending_coins:
            print(f"{self.name}: These cryptos are currently trending up: {', '.join(trending_coins)} 📈")
            best_rising = max(trending_coins, 
                            key=lambda x: self.crypto_db[x]["sustainability_score"])
            print(f"For the best combination of growth and sustainability, consider {best_rising}!") 
        else:
            print(f"{self.name}: No major cryptos are currently in a strong upward trend.")
    
    def handle_sustainability_query(self):
        sustainable_coins = [coin for coin in self.crypto_db 
                           if self.crypto_db[coin]["sustainability_score"] >= 7/10]
        if sustainable_coins:
            best_sustainable = max(sustainable_coins, 
                                 key=lambda x: self.crypto_db[x]["sustainability_score"])
            print(f"{self.name}: For eco-friendly investing, I recommend {best_sustainable} "
                 f"with a sustainability score of {self.crypto_db[best_sustainable]['sustainability_score']*10}/10! 🌱")
        else:
            print(f"{self.name}: No cryptos meet high sustainability standards in our current database.")
    
    def handle_investment_query(self):
        profitable_coins = [coin for coin in self.crypto_db 
                          if (self.crypto_db[coin]["price_trend"] == "rising" 
                              and self.crypto_db[coin]["market_cap"] == "high")]
        if profitable_coins:
            print(f"{self.name}: For long-term growth, consider these established, rising cryptos: "
                 f"{', '.join(profitable_coins)}")
            print("Remember: Higher market cap means lower risk but potentially lower returns.")
        else:
            print(f"{self.name}: Market conditions are uncertain now. Consider stable coins or wait for clearer trends.")
    
    def process_query(self, user_query):
        user_query = user_query.lower()
        
        if "trend" in user_query or "rising" in user_query:
            self.handle_trend_query()
        elif "sustain" in user_query or "eco" in user_query or "green" in user_query:
            self.handle_sustainability_query()
        elif "invest" in user_query or "buy" in user_query or "long-term" in user_query:
            self.handle_investment_query()
        else:
            print(f"{self.name}: I'm not sure I understand. Try asking about trends, sustainability, or investment advice!")
    
    def run(self):
        self.greet()
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'quit':
                print(f"{self.name}: Happy investing! Remember to DYOR (Do Your Own Research)! 👋")
                break
                
            self.process_query(user_input)


# Run the chatbot
if __name__ == "__main__":
    bot = CryptoBuddy()
    bot.run()
