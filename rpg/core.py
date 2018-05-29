class Rpg:
    def __init__(self, **kwargs):
        """
        :param kwargs:
            name
            greeting
            frames
        """
        self.name = kwargs['name']
        self.greeting = kwargs['greeting']
        self.frames = kwargs['frames']

        self.current_frame = 'house'

    def start(self):
        self.show_greeting()
        self.read_frame(self.current_frame)

    def read_frame(self, frame_name):
        self.prompt(self.frames[frame_name]['intro'])

    def get_movement_options(self):
        return [*self.frames[self.current_frame]['moves']] + [*self.frames[self.current_frame]['actions']]

    def show_hint(self):
        return 'These are your movement options: ' + str(self.get_movement_options())

    def parse_response(self, response):
        if response == 'hint':
            return self.prompt(self.show_hint())
        if response == 'help':
            return self.prompt(self.show_hint())
        if self.get_movement_options().count(response):
            self.current_frame = self.frames[self.current_frame]['moves'][response]
            return self.read_frame(self.current_frame)

    def show_greeting(self):
        print('You are now playing ' + self.name)
        print(self.greeting)

    def prompt(self, question):
        print(question)
        print(str(self.get_movement_options()))
        print(self.parse_response(str(input(''))))
