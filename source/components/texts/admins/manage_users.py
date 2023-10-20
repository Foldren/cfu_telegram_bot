text_start_admin_user = f"<b>Режим Юзера</b> 🙎‍♂️\n\n" \
                        f"<u>Рабочие кнопки бота Управляйки в режиме юзера</u> ⚙️\n" \
                        f"🔹 <b>Операция с категориями</b> - создайте и добавьте новую запись в отчет (лист БД), " \
                        f"выбирая нужные категории для позиции в отчете. <i>(категория, это статья движения - " \
                        f"доход или расход денежных средств)</i>\n" \
                        f"🔹 <b>Операция с подотчетами</b> - выдача в подотчет, возврат подотчета, " \
                        f"остаток в подотчете, запрос денег в подотчет.\n" \
                        f"🔹 <b>Кошельки</b> - перевод с одного кошелька на другой по выбранному " \
                        f"ЮР Лицу и изменение " \
                        f"списка ваших кошельков\n" \
                        f"🔹 <b>Отчеты</b> - вывод отчетов в зависимости от настройки админа.\n" \
                        f"🔹 <b>Поддержка</b> - обращайтесь к нам за помощью, в случае неисправностей, недопонимания" \
                        f" или с пожеланиями по доработкам.\n" \
                        f"🔹 📩 - уведомления с запросами от сотрудников к вам на подтверждение, " \
                        f"ориентируйтесь с помощью групп уведомлений."
text_get_list_users = f"<b>Сотрудники</b>\n\n" \
                      f"👨‍💼 Здесь вы можете настроить доступы ваших сотрудников к боту Управляйке.\n" \
                      f"<i>(нажмите на сотрудника, чтобы перейти с ним в чат)</i>\n\n" \
                      f"<u>Кнопки управления</u>:\n" \
                      f"➕ - добавить пользователя\n" \
                      f"✏️ - редактировать\n" \
                      f"❌️ - забрать доступ"
text_start_add_user = f"<b>Добавление сотрудника:</b> (шаг 1)\n\n" \
                      f"<u>Введите данные пользователя</u>:\n" \
                      f"<b>Имя пользователя</b> - в телеграм указан со значком @\n" \
                      f"<b>ФИО</b> - введите через пробел (Фамилия Имя Отчество)\n" \
                      f"<b>Должность сотрудника</b> - в формате строки\n\n" \
                      f"📋 Каждый параметр, начиная со второго вводите с новой строки в формате, " \
                      f"указанном ниже.\n\n" \
                      f"<b>Пример</b> <i>(просто нажмите 👇)</i>:\n" \
                      f"<code>@user987\nПочетов Сергей Александрович\nменеджер</code>"
text_get_id_user = "🔵 Перешлите сюда сообщение этого пользователя,\nчтобы я мог взять его chat_id 📨🆔\n" \
                   "(у пользователя в настройках конфиденциальности должна быть разрешена 'пересылка сообщений')\n\n" \
                   "🔵 Либо просто укажите chat_id в формате числа👇"
text_invalid_user_id = "Указан невалидный chat_id ⚠️"
text_end_add_user = f"📩 Отправьте пользователю ссылку на меня - @upravlyaika_bot, я добавлю его в систему " \
                    f"как только он запустит бот."
text_user_exists = f"Упс, похоже пользователь с этим chat_id уже зарегистрирован в боте 🤷‍♂️"
text_start_change_user = "<b>Редактирование сотрудника:</b> (шаг 1)\n\n" \
                         "👉 Выберите сотрудника, данные которого нужно изменить."
text_change_user = f"<u>Введите новые данные пользователя</u>:\n" \
                   f"<b>Имя пользователя</b> - в телеграм указан со значком @.\n" \
                   f"<b>ФИО</b> - введите через пробел (фамилия имя отчество)\n" \
                   f"<b>Должность сотрудника</b> - в формате строки.\n\n" \
                   f"📋 Каждый параметр, начиная со второго вводите с новой строки в формате, " \
                   f"указанном ниже.\n" \
                   f"<i>(также вы просто можете скопировать пример, в нем указаны данные " \
                   f"выбранного пользователя)</i>\n\n" \
                   f"<b>Пример</b> <i>(просто нажмите 👇)</i>:\n"
text_end_change_user = f"Данные пользователя изменены ✅"
text_end_change_id_user = f"id пользователя изменен ✅🆔"
text_get_id_change_user = "🔵 Перешлите сюда сообщение пользователя,\nчтобы я мог взять его chat_id 📨🆔\n" \
                          "(у пользователя в настройках конфиденциальности должна быть " \
                          "разрешена 'пересылка сообщений')\n\n" \
                          "🔵 Либо просто укажите новый chat_id в формате числа👇"
text_start_delete_users = f"<b>Изменение доступа сотрудников:</b> (шаг 1)\n\n" \
                          "👉 Выберите пользователей, у которых нужно забрать доступ."
