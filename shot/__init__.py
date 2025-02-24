from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'shot'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

class Screenshot(ExtraModel):
    player = models.Link(Player)
    timestamp = models.StringField()
    image_data = models.LongStringField()

def custom_export(players):
    yield ['session', 'participant', 'timestamp', 'image_data']

    screenshots = Screenshot.filter()
    for s in screenshots:
        player = s.player
        participant = player.participant
        session = player.session
        yield [session.code, participant.code, s.timestamp, s.image_data]

# PAGES
class MyPage(Page):
    timeout_seconds = 30
    timer_text = '剩余时间：'
    
    @staticmethod
    def live_method(player, data):
        if data['action'] == 'save_screenshot':
            # 保存截图数据到 Screenshot 模型
            Screenshot.create(
                player=player,
                timestamp=data['timestamp'],
                image_data=data['image']
            )
            # 返回成功消息（可选）
            return {player.id_in_group: {'status': 'success'}}


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        screenshots = Screenshot.filter(player=player)
        return {'screenshots':screenshots}


page_sequence = [MyPage, Results]
