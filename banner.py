# Color Definitions
RED = '\033[1;91m'
WHITE = '\033[46m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
DEFAULT = '\033[3;0m'
YELLOW = '\033[1;33m'
YELLOW2 = '\033[1;93m'
GREEN2 = '\033[1;92m'

def banner():
    """Display the banner for the application."""
    kill = f'''
{YELLOW}██████{DEFAULT}╗ {YELLOW}███████{DEFAULT}╗{YELLOW}██{DEFAULT}╗   {YELLOW}██{DEFAULT}╗{YELLOW}██{DEFAULT}╗{YELLOW}██{DEFAULT}╗   {YELLOW}█{DEFAULT}╗ {YELLOW}███████{DEFAULT}╗     {YELLOW}██████{DEFAULT}╗ {YELLOW}█████{DEFAULT}╗ {YELLOW}██{DEFAULT}╗     {YELLOW}██{DEFAULT}╗     
{YELLOW}██{DEFAULT}╔══{YELLOW}██{DEFAULT}╗{YELLOW}██{DEFAULT}╔════╝{YELLOW}██{DEFAULT}║   {YELLOW}██{DEFAULT}║{YELLOW}██{DEFAULT}║{YELLOW}██{DEFAULT}║   {DEFAULT}╚╝ {YELLOW}██{DEFAULT}╔════╝    {YELLOW}██{DEFAULT}╔════╝{YELLOW}██{DEFAULT}╔══{YELLOW}██{DEFAULT}╗{YELLOW}██{DEFAULT}║     {YELLOW}██{DEFAULT}║     
{YELLOW}██{DEFAULT}║  {YELLOW}██{DEFAULT}║{YELLOW}█████{DEFAULT}╗  {YELLOW}██{DEFAULT}║   {YELLOW}██{DEFAULT}║{YELLOW}██{DEFAULT}║{YELLOW}██{DEFAULT}║      {YELLOW}███████{DEFAULT}╗    {YELLOW}██{DEFAULT}║     {YELLOW}███████{DEFAULT}║{YELLOW}██{DEFAULT}║     {YELLOW}██{DEFAULT}║     
{YELLOW}██{DEFAULT}║  {YELLOW}██{DEFAULT}║{YELLOW}██{DEFAULT}╔══╝  ╚{YELLOW}██{DEFAULT}╗ {YELLOW}██╔{DEFAULT}╝{YELLOW}██{DEFAULT}║{YELLOW}██{DEFAULT}║      ╚════{YELLOW}██{DEFAULT}║    {YELLOW}██{DEFAULT}║     {YELLOW}██{DEFAULT}╔══{YELLOW}██{DEFAULT}║{YELLOW}██{DEFAULT}║     {YELLOW}██{DEFAULT}║     
{YELLOW}██████{DEFAULT}╔╝{YELLOW}███████{DEFAULT}╗ ╚{YELLOW}████{DEFAULT}╔╝ {YELLOW}██{DEFAULT}║{YELLOW}███████{DEFAULT}╗ {YELLOW}███████{DEFAULT}║    ╚{YELLOW}██████{DEFAULT}╗{YELLOW}██{DEFAULT}║  {YELLOW}██{DEFAULT}║{YELLOW}███████{DEFAULT}╗{YELLOW}███████{DEFAULT}╗
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝
    '''

    # Displaying the banner
    print(f"\t\t\t{CYAN}YOU ARE GOING TO MAKE A{GREEN}")
    print(kill)
    print(f"{GREEN} \n\t\t\t\tby hasanfirnas{DEFAULT}")  # Signature

# Call the banner function to display it
if __name__ == "__main__":
    banner()
