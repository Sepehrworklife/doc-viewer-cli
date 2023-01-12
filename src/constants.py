import os
## Github
SEC_FILE_NAME: str = os.path.dirname(__file__) + "/gh_token.txt"








## Messages
# TODO: Fix error message
MESSAGE_ERROR_IF_INITIAL_NOT_HAPPEND: str = "[bold red]ERROR![/bold red] [red] You haven't set your github personal token [/red]! run: xxxxx"
MESSAGE_SUCCESS_INITIAL: str = "[bold green]Success![/bold green] Github personal token has been set successfully! :boom:"