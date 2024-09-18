import markups
from states.template.UserState import UserState
from states.template.Response import Response
import config_controller
import utils.ScannerCode as Scan
from db.controllers.GoodsController import GoodsController
import asyncio

class ScannerState(UserState):
    async def start_msg(self):
        if self.message_obj.content_type == "photo":
            file = await self.bot.get_file(self.message_obj.photo[-1].file_id)
            file_bytes = await self.bot.download_file(file.file_path)
            code = Scan.get_code_from_bytes_image(file_bytes)
            if code is not None:
                goods = GoodsController()
                tovar = await goods.get_by(code=code)
                if len(tovar) == 0:
                    return Response(text="Нажаль, цього товара немає у списку кешбеку😢", is_end=True)
                else:
                    tovar = tovar[0]
                    return Response(
                        text= f"Штрих-код: {tovar.code}\n"
                              f"Назва: {tovar.name}\n"
                              f"Бренд: {tovar.brend}\n",
                        is_end = True
                    )
            else:
                return Response(text="Халепа! Невдалося відсканувати штрих-код!\n"
                                     "Спробуйте зробити більш якісніше фото чи введіть штрих-код вручну", is_end=True)

        elif self.message_obj.content_type == "text":
            text = self.message_obj.text
            goods = GoodsController()
            if text.isdigit():
                code = text
                tovar = await goods.get_by(code=code)
                if len(tovar) == 0:
                    return Response(text="Нажаль, цього товара немає у списку кешбеку😢", is_end=True)
                else:
                    tovar = tovar[0]
                    return Response(
                        text= f"Штрих-код: {tovar.code}\n"
                              f"Назва: {tovar.name}\n"
                              f"Бренд: {tovar.brend}\n",
                        is_end = True
                    )
            else:
                tovar = await goods.get_by(name=text)
                if len(tovar) == 0:
                    return Response(text="Нажаль, цього товара немає у списку кешбеку😢", is_end=True)
                else:
                    text_tovar = f"Було знайдено {len(tovar)} товарів\n\n"
                    while True:
                        for _ in range(5):
                            if len(tovar) == 0:
                                await self.bot.send_message(chat_id=self.user_chat_id, text=text_tovar)
                                break
                            text_tovar += (f"Штрих-код: {tovar[0].code}\n"
                                           f"Назва: {tovar[0].name}\n"
                                           f"Бренд: {tovar[0].brend}\n\n")
                            del tovar[0]
                        await self.bot.send_message(chat_id=self.user_chat_id, text=text_tovar)
                        text_tovar = ""
                        await asyncio.sleep(2)

        elif self.message_obj.content_type == "video":
            return Response(text="Відео не підтримується😢\n"
                                 "Краще фото або текстом🙂", is_end=True)
        else:
            return Response(text="От халепа! Щось пішло не так😢\n"
                                 "Спробуйте знову надіслати фото штрих-коду, або ж введіть назву товару чи штрих-код", is_end=True)
