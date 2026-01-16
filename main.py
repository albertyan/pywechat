import datetime
import re
import json
from pyweixin import Messages,Tools,Navigator
from pyweixin.Uielements import (Login_window,Main_window,SideBar,Independent_window,ListItems,
Buttons,Texts,Menus,TabItems,Lists,Edits,Windows,Panes)
from pyweixin.WinSettings import SystemSettings 
import pywinauto.mouse as mouse
import time
##########################################################################################

#各种UI实例化
Login_window=Login_window()#登录界面的UI
Main_window=Main_window()#主界面UI
SideBar=SideBar()#侧边栏UI
Independent_window=Independent_window()#独立主界面UI
Buttons=Buttons()#所有Button类型UI
Texts=Texts()#所有Text类型UI
TabItems=TabItems()#所有TabIem类型UI
Lists=Lists()#所有列表类型UI
Menus=Menus()#所有Menu类型UI
Edits=Edits()#所有Edits类型UI
Windows=Windows()#所有Window类型UI
Panes=Panes()#所有Pane类型UI


# contact_list,main_window= Navigator.open_contacts()

# def print_item_info(item):
#     # 获取所有子元素的文本和类名，以便调试
#     items_info = []
#     # 尝试获取子元素，如果直接children()不行，可能需要先等待或使用其他方法
#     # 这里假设contact_list是pywinauto的wrapper
#     try:
#         children = contact_list.children()
#         for item in children:
#             items_info.append({
#                 "text": item.window_text(),
#                 "class_name": item.class_name(),
#                 "control_type": item.element_info.control_type
#             })
#             print(json.dumps(items_info,ensure_ascii=False,indent=2))
#     except Exception as e:
#         items_info = {"error": str(e)}

    
#Tools.move_window_to_center()
# print(Contacts.get_friends_detail(is_json=True))
# Navigator.open_contacts_manage()
# print(Tools.get_current_wxid())
# moments = Messages.dump_recent_sessions(recent='Today')
# for dict in moments:
#     print(dict)
from pywinauto import Desktop


desktop=Desktop(**Independent_window.Desktop)

#通讯录列表
contact_list,main_window = Navigator.open_contacts(is_maximize=False)
custom=main_window.descendants(control_type='Custom')
buttons = custom[-1].children()[1].descendants(class_name='mmui::ContactsCellMangerBtnView')
buttons[0].click_input()

# contact_window=Tools.move_window_to_center(Independent_window.ContactManagerWindow)

contact_window = desktop.window(**Independent_window.ContactManagerWindow)

print(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))


contact_custom=contact_window.descendants(control_type='Custom')
print(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

contact_list_view = contact_custom[-1].children()[0].descendants(class_name='mmui::ContactsManagerDetailView')

print(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# is_scrollable=Tools.is_scrollable(contact_list_view[0])
# print(is_scrollable)

rect = contact_list_view[0].rectangle()
# x = rect.left + rect.width() // 2
# y = rect.top + rect.height() // 2
c = rect.mid_point()
# mmui::ContactsManagerDetailCell
if True:

    # begin_point_y = c.y + int(rect.width() / 3)
    # end_point_y = c.y - int(rect.width() / 3)

    mouse.move(coords=(c.x, c.y))
    friends = []
    g_inx = 1
    last_cell = None
    is_end = False
    # 记录上一个循环的最后一个联系人，用于判断是否滚动到了底部
    pre_last_cell = None
    while not is_end:
        cells = contact_list_view[0].descendants(class_name='mmui::ContactsManagerDetailCell')
        last_cell = cells[-1].window_text()
        for index, cell in enumerate(cells):
            if pre_last_cell is not None and last_cell == pre_last_cell:
                is_end = True
                break
            print(f'第{g_inx}个联系人: {cell.window_text()}')
            g_inx += 1
        pre_last_cell = last_cell
        time.sleep(1)
        contact_list_view[0].type_keys('{PGDN}')
contact_window.close()
    

# contact_list_view[0].set_focus()
# mouse.press(button='left',coords=(c.x, begin_point_y))
# mouse.release(button='left',coords=(c.x, end_point_y))
# mouse.scroll(coords=(c.x, c.y),wheel_dist=-1800)
# print(custom[-1].child_window(Uielements.Buttons.ContactsManageButton).window_text())

# contactManagerButton = contact_list.child_window(Uielements.Buttons.ContactsManageButton)
# contactManagerButton.click()
