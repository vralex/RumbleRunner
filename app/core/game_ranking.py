from app.models.all import GameRanking
from base.api.database import SessionScope
from base.api.handler import Context


class GameRankingHelpers:
    @staticmethod
    def get_or_create(context: Context) -> GameRanking:
        game_ranking = SessionScope.session().query(GameRanking).filter(
            GameRanking.tg_group_id == context.group.tg_id).one_or_none()
        if game_ranking is None:
            game_ranking = GameRanking(tg_group_id=context.group.tg_id)
            SessionScope.session().add(game_ranking)
            SessionScope.commit()
        return game_ranking
