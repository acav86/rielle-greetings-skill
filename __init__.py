from mycroft import MycroftSkill, intent_file_handler


class RielleGreetings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('greetings.rielle.intent')
    def handle_greetings_rielle(self, message):
        self.speak_dialog('greetings.rielle')


def create_skill():
    return RielleGreetings()

