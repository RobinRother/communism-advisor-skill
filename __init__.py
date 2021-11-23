from mycroft import MycroftSkill, intent_file_handler


class CommunismAdvisor(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('advisor.communism.intent')
    def handle_advisor_communism(self, message):
        self.speak_dialog('advisor.communism')


def create_skill():
    return CommunismAdvisor()

