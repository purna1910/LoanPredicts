class LoanChatbot:
    def __init__(self):
        self.responses = {
            "documents": "Required documents: Identity proof, Address proof, Income proof, Property documents.",
            "eligibility": "Check eligibility based on income, credit history, and employment.",
            "status": "Login to track your application status.",
            "help": "I can help with documents, eligibility, and application status."
        }
    
    def get_response(self, message):
        message = message.lower()
        for key in self.responses:
            if key in message:
                return self.responses[key]
        return "Sorry, I didn't understand. Ask about documents, eligibility, or status."
