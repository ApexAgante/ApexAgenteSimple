from prompt_toolkit.completion import Completer, Completion
from cli.data import Data

data = Data({
    'headers': '',
    'query': '?hostname',
    'body': '',
    'http_method': 'GET'
})


class MyCustomCompleter(Completer):
    def __init__(self):
        self.commands = ["help", "clear", "all", "get"]
        self.hostnames = data.get_all_host()

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor.lower()
        words_before_cursor = text_before_cursor.split()

        # If the input starts with "get",
        # return completions for the second word
        if len(words_before_cursor) == 2 and words_before_cursor[0] == "get":
            completions = [Completion(hostname, -len(words_before_cursor[-1]))
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
