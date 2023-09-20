async def get_text_start_admin(name_user: str) -> str:
    return f"ВКЛЮЧЕН РЕЖИМ АДМИНА 👨‍💼\n\n" \
           f"Здравствуйте, админ <b>{name_user}</b>!👋\n\n" \
           f"‼️ Чтобы настроить бота, вам нужно выполнить 3 шага ‼️\n\n" \
           f"1️⃣️ Завести сотрудников\n" \
           f"2️⃣ Создать ЮР Лица\n" \
           f"3️⃣ Создать категории\n\n" \
           f"<u>Рабочие кнопки бота Управляйки</u> ⚙️ :\n\n" \
           f"1️⃣️ <b>Сотрудники</b> - добавление и изменение списка сотрудников, подключенных к боту. (шаг 1)\n\n" \
           f"2️⃣ <b>Юр лица</b> - добавление и изменение списка юр лиц, подключенных к боту," \
           f" управление их отображением. (шаг 2)\n\n" \
           f"3️⃣ <b>Категории</b> - управление отображением категорий, и подкатегорий на разных уровнях " \
           f"вложенности. (шаг 3)\n\n" \
           f"4️⃣ <b>Отчеты</b> - изменение списка наблюдателей для разных периодов ваших отчетов\n\n" \
           f"5️⃣ <b>Режим: Админ</b> 👨‍💼 / <b>Режим: Юзер</b> 🙎‍♂️  - ваш текущий режим работы с ботом, " \
           f"нажмите чтобы сменить"
