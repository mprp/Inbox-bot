from pyrogram import types


def inline_button(each_row_list, labels_list, urls_list,
                  cbq_list, siq_list, markup_map):

    """To create all kind of inline buttons you can use this function.

    each_row_list guide and sample:
        each_row_list[0] Indicates the number of buttons to be
        displayed in the first row.
        for example, [3, 2, 3] -> [button1] [button2] [button3]
                                  [  button4  ]   [  button5  ]
                                  [button6] [button7] [button8]
        logical errors expected:
        if sum(each_row_list) < total_number_of_buttons,
        Certainly some of the buttons will not displayed

    label_list should contain labels for all buttons Respectively

    urls_list, cbq_list, siq_list:
        siq phrase refers to (switch inline query)

        each index must carry the content of the corresponding button.
        for better understanding, if your first button is a
        call back query button, therefore: urls_list[0] == 'None',
        cbq_list[0] == 'call back data',  siq_list[0] == 'None'

    markup_map guide:
        URL buttons -> 0
        Call back query buttons -> 1
        Inline query switcher buttons -> 2
        for example take a look at this, markup_map = [1, 1, 2]
        indicates that the first two buttons are call_back buttons
        and the latest button is Inline query switcher button :)
    """

    button_list, index = [], 0
    _button = types.InlineKeyboardButton

    for label in labels_list:

        if markup_map[index] == 0:
            button_list.append(_button(label, url=urls_list[index]))

        elif markup_map[index] == 1:
            button_list.append(_button(label, callback_data=cbq_list[index]))

        elif markup_map[index] == 2:
            button_list.append(
                _button(label,
                        switch_inline_query_current_chat=siq_list[index]))

        index += 1

    menu, list_index = [], 0

    for column in range(len(each_row_list)):
        row = []

        for i in range(each_row_list[list_index]):
            row.append(button_list.pop(0))

        list_index += 1
        menu.append(row)

    generated_buttons = types.InlineKeyboardMarkup(menu)

    return generated_buttons


def simple_button(each_row_list, labels_list):
    """To use this function in order to create Keyboard buttons.

    each_row_list guide and sample:
        each_row_list[0] Indicates the number of buttons to be
        displayed in the first row.
        for example, [3, 2, 3] -> [button1] [button2] [button3]
                                  [  button4  ]   [  button5  ]
                                  [button6] [button7] [button8]
        logical errors expected:
        if sum(each_row_list) < total_number_of_buttons,
        Certainly some of the buttons will not displayed

    label_list should contain labels for all buttons Respectively
    """

    button_list = []

    for label in labels_list:
        button_list.append(types.KeyboardButton(label))

    menu, list_index = [], 0

    for column in range(len(each_row_list)):
        row = []

        for i in range(each_row_list[list_index]):
            row.append(button_list.pop(0))

        list_index += 1
        menu.append(row)

    generated_buttons = types.ReplyKeyboardMarkup(menu, resize_keyboard=True)

    return generated_buttons


def inline_menu_creator(titles, contents, descriptions,
                        thumbs_url, reply_markups):
    """TO show contents as inline menu you can use this function.
    Note: all parameters are list type.

    titles:
        this list contains independent titles for each result
        i.e. titles[0] == "a title for first result"

    contents:
        in order to carry content for each result.
        a text or content that will send by user to chat,
        each time the user clicks on the related result.

    descriptions:
        an other list to carry descriptions for each result.
        descriptions are strings that will shown under titles.

    thumb_url:
        contains urls for each inline result.
        These urls are for photos that will be displayed
        next to the description.

    reply_markups:
        in short, these reply markups are displayed under contents,
        each time user clicks on any result!
    """

    result = types.InlineQueryResultArticle
    content = types.InputTextMessageContent
    results = []

    index = 0
    for title in titles:

        single_res = result(title=title,
                            input_message_content=content(contents[index]),
                            description=descriptions[index],
                            thumb_url=thumbs_url[index],
                            reply_markup=reply_markups[index])
        index += 1
        results.append(single_res)

    return results
