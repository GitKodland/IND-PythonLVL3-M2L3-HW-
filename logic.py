from discord import ui, ButtonStyle


class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        buttons = []
        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'correct_{i}'))
            else:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'wrong_{i}'))
        return buttons


quiz_questions = [
   Question("Apa yang kucing lakukan ketika tidak ada yang melihat mereka?", 1, "Tidur", "Menulis meme"),
   Question("Bagaimana kucing menunjukkan cinta?", 0, "Purring keras", "Foto cinta", "Menggonggong"),
   Question("Buku apa yang kucing suka membaca?", 3, "Buku bantuan diri sendiri", "Manajemen waktu: bagaimana tidur 18 jam sehari", "101 cara untuk tidur 5 menit lebih awal dari pemilik Anda", "Panduan manajemen manusia")
]