# manage menu items ----------------------------------------------------------------------------------------------------

text_get_user_list_mi = f"<b>ШАГ</b> 2️⃣:\n" \
                        f"Задайте нужную очередь категорий для внесения новой записи в бд.\n\n" \
                        f"<u>Кнопки управления</u>:\n\n" \
                        f"Назад ⬅️ - вернуться на уровень выше\n" \
                        f"Расход ➖ - новая запись о расходе\n" \
                        f"Доход ➕ - новая запись о доходе\n\n" \
                        f"Для перехода на уровень меню ниже, нажмите на нужную категорию 👉\n\n"

text_no_menu_items_u = f"Вы добавлены в бот, но похоже админ еще не назначил доступные для вас категории 🙅‍♀️"

text_start_add_mi_to_bd = f"<b>ШАГ</b> 3️⃣:\nВведите сумму операции в рублях, в формате числа 💵\n<b>Пример</b>:" \
                          f"\n<code>987654</code>"

text_choose_bank = f"<b>ШАГ</b> 4️⃣:\nВыберите банк, по которому произведена " \
                   f"операция 🏦 (либо способ оплаты наличными): \n"

text_invalid_volume_operation = "Некорректная сумма. Введите число 💯"

text_send_check_photo = "<b>ШАГ</b> 5️⃣:\nПеретащите в чат фото чека 🖼️\n(в сжатом виде или в виде файла)" \
                        "\n\n Либо нажмите - 📎 чтобы прикрепить файл."

text_invalid_check_photo = "Похоже вы отправили не фото 🤷‍♂️"

text_end_add_mi_to_bd = f"Запись успешно добавлена в лист БД ✅\n" \
                        f"Чеки и таблицу можно посмотреть в вашем хранилище google drive.\n"

# join bot to group ----------------------------------------------------------------------------------------------------

text_success_join_bot_to_group = f"Похоже меня добавили в группу. Здравствуйте, коллеги," \
                                 f" я - <b>Бот Управляйка</b> 🙎‍♂️👋\n\n" \
                                 f"Вижу приглашение отправлено от одного из пользователей, зарегистрированный " \
                                 f"в моей системе. \nОкей, уведомления о новых операциях вашей организации буду " \
                                 f"присылать в этот чат 💬"

text_repeat_add = f"Я уже прикреплен к другой группе, чтобы "

# make issuance of report ----------------------------------------------------------------------------------------------

text_start_issuance = "<b>ШАГ</b> 1️⃣:\nВыберите ЮР Лицо из списка 👇"

text_select_worker_issuance = "<b>ШАГ</b> 2️⃣:\nВыберите сотрудника для выдачи под отчет 👇"

text_set_volume_issuance = "<b>ШАГ</b> 3️⃣:\nУкажите сумму в рублях в формате числа 💵 \n\n" \
                           "<b>Пример:</b>\n<code>12455</code>"

text_select_payment_method_issuance = "<b>ШАГ</b> 4️⃣:\nВыберите кошелек 👇"

text_no_notify_groups = "Для начала пригласите бота хотя бы в одну группу 🤗\n" \
                        "Я отправлю туда сообщение с подтверждением операции 📩"

text_select_notify_group_issuance = "<b>ШАГ</b> 5️⃣:\nВыберите группу, в которую нужно отправить уведомление 👇"

text_end_issuance = "Отправил уведомление с подтверждением в группы 📨"

text_confirm_issuance_report = "Пользователь подтвердил получение под отчет ✅"

# make return issuance of report ---------------------------------------------------------------------------------------

text_set_volume_return_issuance = "<b>ШАГ</b> 2️⃣:\nУкажите сумму в рублях в формате числа 💵 \n\n" \
                                  "<b>Пример:</b>\n<code>12455</code>"

text_select_payment_method_return_issuance = "<b>ШАГ</b> 3️⃣:\nВыберите кошелек 👇"

text_end_return_issuance = "Запись о возврате подотчетных средств внесена успешно ✅"

# write mi to bd -------------------------------------------------------------------------------------------------------

text_choose_sender_write_item = "<b>ШАГ</b> 1️⃣:\nВыберите имя исполнителя операции 👇"

# make transfer --------------------------------------------------------------------------------------------------------

text_set_volume_transfer = "<b>ШАГ</b> 2️⃣:\nУкажите сумму в рублях в формате числа 💵 \n\n" \
                           "<b>Пример:</b>\n<code>12455</code>"

text_select_wallet_sender = "<b>ШАГ</b> 3️⃣:\nВыберите кошелек с которого нужно вывести деньги 👇"

text_select_wallet_recipient = "<b>ШАГ</b> 4️⃣:\nВыберите кошелек для пополнения 👇"

text_end_transfer = "Запись о переводе внесена успешно ✅"

# change menu ----------------------------------------------------------------------------------------------------------

text_open_under_stats_menu = "▶️ Вы вошли в меню - 'Операция с подотчетами'"

text_open_wallets_menu = "▶️ Вы вошли в меню - 'Кошельки'"

text_back_to_main_menu = "◀️ Вы вернулись в главное меню"

# change wallet list ---------------------------------------------------------------------------------------------------

text_change_wallets_list = f"💰<b>КОШЕЛЬКИ</b>\n" \
                           f"Выберите кошельки которые будете использовать при выполнении операций\n" \
                           f"(подключенные кошельки отмечены флажком, должен быть выбран хотя бы один кошелек) 👇"

text_end_change_wallets_list = "Список кошельков изменен успешно ✅"

# open stats list ------------------------------------------------------------------------------------------------------

text_success_show_stats = "Выберите период отчета, по которому нужно отобразить информацию 👇"

text_no_shares_show_stats = "Похоже админ не предоставил для вас доступ к таблице 🙅‍♂️"
