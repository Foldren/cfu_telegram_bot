from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from components.filters import IsUserFilter, IsNotMainMenuMessage
from components.tools import get_inline_keyb_markup, get_msg_queue, get_callb_content, \
    get_inline_keyb_profit_cost, get_inline_keyb_str_back_to_parent_items_u, \
    get_str_format_queue
from components.users.texts import text_get_user_list_mi
from services.models_extends.menu_item import MenuItemApi
from states.user.steps_create_notes_to_bd import StepsWriteMenuItemsToBd

rt = Router()

# Фильтр на проверку категории доступа пользователя
rt.message.filter(IsUserFilter(), IsNotMainMenuMessage())
rt.callback_query.filter(IsUserFilter())


# Вывод дочерних пунктов меню
@rt.callback_query(StepsWriteMenuItemsToBd.set_queue_menu_items, F.data.startswith("user_menu_item"))
async def next_to_nested_items_u(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsWriteMenuItemsToBd.set_queue_menu_items)

    message = callback.message
    selected_item_id = await get_callb_content(callback.data)
    selected_item = await MenuItemApi.get_by_id(selected_item_id)
    menu_items = await MenuItemApi.get_user_items_by_parent_id(callback.from_user.id, parent_id=selected_item.id)
    queue = await get_str_format_queue(selected_item_id)
    msg_queue = await get_msg_queue(selected_item.level, selected_item.name, queue)

    dict_mi_names_ids = {'names': [], "ids": []}

    # Заполняем дикт списки названиями кнопок и данными колбеков, пропускаем скрытые (id mi)
    for e in menu_items:
        if e['status'] == 1:
            dict_mi_names_ids['names'].append(e['name'])
            dict_mi_names_ids['ids'].append(e['id'])

    if dict_mi_names_ids['names']:
        keyboard = await get_inline_keyb_markup(
            list_names=dict_mi_names_ids['names'],
            list_data=dict_mi_names_ids['ids'],
            callback_str="user_menu_item",
            number_cols=2,
            add_keyb_to_start=await get_inline_keyb_str_back_to_parent_items_u(selected_item_id)
        )

        await message.edit_text(text=msg_queue, reply_markup=keyboard, parse_mode="html")

    else:
        # Если последняя категория и это колбек, добавляем кнопки расход и доход
        keyboard = await get_inline_keyb_profit_cost(selected_item_id)
        await message.edit_text(text=msg_queue, reply_markup=keyboard, parse_mode="html")


# Возврат назад к родительским пунктам меню
@rt.callback_query(StepsWriteMenuItemsToBd.set_queue_menu_items, F.data.startswith("back_to_upper_level_u"))
async def back_to_parent_items_u(callback: CallbackQuery):
    selected_item_id = await get_callb_content(callback.data)
    selected_item = await MenuItemApi.get_by_id(selected_item_id)
    parent_item = await selected_item.parent
    parent_item_name = parent_item.name if parent_item is not None else None
    menu_items = await MenuItemApi.get_parent_items_by_chat_id(selected_item_id, callback.message.chat.id)
    old_queue = await get_str_format_queue(selected_item_id)
    new_queue = old_queue[:old_queue.rfind('→') - 1]
    msg_queue = await get_msg_queue(selected_item.level-1, parent_item_name, new_queue)
    upper_level = menu_items[0]['parent_id'] is None
    final_msg = text_get_user_list_mi + msg_queue if upper_level else msg_queue
    selected_upper_item_id = selected_item.parent_id
    dict_mi_names_ids = {'names': [], "ids": []}

    # Заполняем дикт списки названиями кнопок и данными колбеков, пропускаем скрытые (id mi)
    for e in menu_items:
        if e['status'] == 1:
            dict_mi_names_ids['names'].append(e['name'])
            dict_mi_names_ids['ids'].append(e['id'])

    keyb_str = None if upper_level else await get_inline_keyb_str_back_to_parent_items_u(selected_upper_item_id)

    keyboard = await get_inline_keyb_markup(
        list_names=dict_mi_names_ids['names'],
        list_data=dict_mi_names_ids['ids'],
        callback_str="user_menu_item",
        number_cols=2,
        add_keyb_to_start=keyb_str
    )

    await callback.message.edit_text(text=final_msg, reply_markup=keyboard, parse_mode='html')

