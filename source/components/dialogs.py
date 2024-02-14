from aiogram_dialog import Dialog, LaunchMode
from windows.categories.create import select_name
from windows.categories.delete import select_categories
from windows.categories.get import main_categories, child_categories
from windows.categories.update import select_param, select_category, update_name
from windows.counterparties.create import write_params, select_attach_category
from windows.counterparties.delete import select_counterparties
from windows.counterparties.get import counterparties
from windows.admin_menu.menu import main
from windows.authorization.authorization import start, authorization


# authorization
authorization = Dialog(start, authorization, launch_mode=LaunchMode.ROOT)


# menu
change_menu = Dialog(main, launch_mode=LaunchMode.ROOT)


# category
get_categories = Dialog(main_categories, child_categories, launch_mode=LaunchMode.SINGLE_TOP)

create_category = Dialog(select_name, launch_mode=LaunchMode.SINGLE_TOP)

update_category = Dialog(select_category, select_param, update_name, launch_mode=LaunchMode.SINGLE_TOP)

delete_categories = Dialog(select_categories, launch_mode=LaunchMode.SINGLE_TOP)


# counterparty
get_counterparties = Dialog(counterparties, launch_mode=LaunchMode.SINGLE_TOP)

create_counterparty = Dialog(write_params, select_attach_category, launch_mode=LaunchMode.SINGLE_TOP)

# delete_counterparties = Dialog(select_counterparties, launch_mode=LaunchMode.SINGLE_TOP)
