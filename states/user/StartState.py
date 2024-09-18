import markups
from states.template.UserState import UserState
from states.template.Response import Response
import config_controller

class StartState(UserState):
    async def start_msg(self):
        return Response(text="Вітаю у боті!\n"
                             "Бот був створений для зручності пошуку товарів з кешбеком 'Зроблено в Україні'.\n"
                             "Бо не всі товари з кешбеком, які зроблені в Україні.\n\n"
                             "Для початку роботи з ботом надішліть фото штрихкоду, або ж вручну введіть його чи знайдіть по назві товару.", is_end=True)