from prompt_toolkit.completion import Completer, Completion
from .data import Data

data = Data({
    'headers': '',
    'query': '?hostname',
    'body': '',
    'http_method': 'GET'
})


class TerminalCompleter(Completer):
    """
    Terminal completer for custom CLI
    """

    def __init__(self):
        self.commands = ['help', 'clear', 'all', 'get']
        self.hostnames = data.get_all_host()

    def get_completions(self, document, complete_event):
        """
        Rendering auto complete for commands
        """
        text_before_cursor = document.text_before_cursor.lower()
        words_before_cursor = text_before_cursor.split()

        # Check if input starts with get and
        # return completions for the second word using host name
        if len(words_before_cursor) == 2 and words_before_cursor[0] == 'get':
            completions = [Completion(hostname, -len(words_before_cursor[1]))
                           for hostname in self.hostnames if hostname.lower().
                           startswith(words_before_cursor[-1])]
        elif len(words_before_cursor) == 0:
            completions = [Completion(command, start_position=0)
                           for command in self.commands]
        else:
            completions = [Completion(command, -len(words_before_cursor[-1]))
                           for command in self.commands if command.lower().
                           startswith(words_before_cursor[-1])]

        return completions
