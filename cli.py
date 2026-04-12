"""Command-line interface for ProjectHatch."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import BudgetTracker, QueryRouter, LocalInference, APIHandler


class CLI:
    def __init__(self, config: dict):
        self.config = config
        self.budget = BudgetTracker()
        self.router = QueryRouter()
        self.local = LocalInference()
        self.api = APIHandler(config)
        self.conversation = []
    
    def run(self):
        """Main chat loop."""
        print("🐣 ProjectHatch v0.1")
        print("Made for the people. By Paul Sudo.\n")
        
        # Show disclaimer on first run
        if not self.config.get("disclaimer_accepted"):
            self.show_disclaimer()
        
        print("Type 'help' for commands, 'quit' to exit.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if user_input.lower() == 'help':
                    self.show_help()
                    continue
                
                if user_input.lower() == 'budget':
                    print(self.budget.get_status())
                    continue
                
                # Process query
                self.process_query(user_input)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def show_disclaimer(self):
        """Show disclaimer and get acceptance."""
        print("=" * 60)
        print("⚖️  DISCLAIMER")
        print("=" * 60)
        print("""
ProjectHatch is experimental software provided "as-is"
under the MIT License. By using this software, you accept
full responsibility for any outcomes.

• No warranty or guarantees
• May incur API costs (you control budget)
• May modify files (with your permission)
• Community-supported, best effort

Continue? (yes/no): """)
        
        response = input().strip().lower()
        if response != 'yes':
            print("Exiting...")
            sys.exit(0)
        
        self.config["disclaimer_accepted"] = True
        print("\n✅ Disclaimer accepted. Let's go!\n")
    
    def show_help(self):
        """Show available commands."""
        print("""
Commands:
  help     - Show this help
  budget   - Show budget status
  quit     - Exit

Prefixes:
  @local   - Force local model
  @cloud   - Force cloud model
""")
    
    def process_query(self, query: str):
        """Process user query."""
        # Check for force prefixes
        force_local = query.startswith("@local")
        force_cloud = query.startswith("@cloud")
        
        if force_local or force_cloud:
            query = query.split(maxsplit=1)[1] if len(query.split()) > 1 else ""
        
        # Analyze complexity
        complexity, reasoning = self.router.analyze_query(query)
        
        # Get available models
        local_models = self.local.list_models()
        
        # Route
        if force_local:
            if not local_models:
                print("❌ No local models available")
                return
            response = self.local.run(local_models[0], query)
        elif force_cloud:
            response, cost = self.api.run_google(query)
            self.budget.record_spending(cost, "google")
        else:
            # Smart routing
            route = self.router.select_model(complexity, local_models, self.budget.get_remaining())
            
            if route["type"] == "local":
                print(f"🧠 Using local: {route['model']}")
                response = self.local.run(route["model"], query)
            elif route["type"] == "ask_user":
                print(f"\n💭 {route['reasoning']}")
                print(f"💸 Estimated cost: ${route['estimated_cost']:.2f}")
                print(f"   Remaining budget: ${self.budget.get_remaining():.2f}")
                choice = input("   Use cloud? (y/n): ").lower()
                
                if choice == 'y':
                    response, cost = self.api.run_google(query)
                    self.budget.record_spending(cost, "google")
                else:
                    if local_models:
                        response = self.local.run(local_models[-1], query)
                    else:
                        print("❌ No local models available")
                        return
        
        if response:
            print(f"\nHatch: {response}\n")
        else:
            print("❌ Failed to get response")


def main(config):
    """Entry point for CLI."""
    cli = CLI(config)
    cli.run()
