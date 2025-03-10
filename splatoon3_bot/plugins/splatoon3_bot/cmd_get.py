from nonebot import on_command, logger
from nonebot.adapters import Event, Bot
from nonebot.adapters.onebot.v11 import Bot as QQBot

from .sp3bot import (
    get_user_db_info, get_last_battle_or_coop, get_me, get_friends_msg, get_ns_friends_msg, get_x_top_msg,
    get_my_schedule_msg, get_screenshot_image, get_history_msg, get_friend_code, get_top
)
from .utils import bot_send, check_session_handler

__all__ = ['show_db_info', 'last', 'me']


@on_command("show_db_info", aliases={'sdi'}, block=True).handle()
@check_session_handler
async def show_db_info(bot: Bot, event: Event):

    if 'group' in event.get_event_name():
        await bot_send(bot, event, '请私聊机器人', parse_mode='Markdown')
        return

    user_id = event.get_user_id()
    msg = get_user_db_info(user_id=user_id)

    await bot_send(bot, event, msg, parse_mode='Markdown')


@on_command("last", block=True).handle()
@check_session_handler
async def last(bot: Bot, event: Event):
    user_id = event.get_user_id()

    get_text = False
    get_battle = False
    get_coop = False
    get_pic = False
    get_image = False
    get_ss = False
    mask = False
    idx = 0
    cmd_message = event.get_plaintext()[5:].strip()
    logger.debug(f'last: {cmd_message}')
    if cmd_message:
        cmd_lst = cmd_message.split()
        if 'b' in cmd_lst or 'battle' in cmd_lst:
            get_battle = True
        if 'c' in cmd_lst or 'coop' in cmd_lst:
            get_coop = True
        if 't' in cmd_lst or 'text' in cmd_lst:
            get_text = True
        if 'p' in cmd_lst or 'pic' in cmd_lst:
            get_pic = True
        if 'i' in cmd_lst or 'image' in cmd_lst:
            get_image = True
        if 'ss' in cmd_lst or 'screenshot' in cmd_lst:
            get_ss = True
        if 'm' in cmd_lst or 'mask' in cmd_lst:
            mask = True
        for cmd in cmd_lst:
            if cmd.isdigit():
                idx = int(cmd) - 1
                idx = max(0, idx)
                idx = min(49, idx)
                break

    image_width = 1000
    if isinstance(bot, QQBot) and get_text is False and get_pic is False and get_ss is False:
        # qq 默认图片
        get_image = True

    if get_text:
        get_image = False

    if get_image:
        image_width = 630

    msg = await get_last_battle_or_coop(user_id, get_battle=get_battle, get_coop=get_coop, get_pic=get_pic, idx=idx,
                                        get_screenshot=get_ss, get_image=get_image, mask=mask)
    photo = None
    if get_ss:
        photo = msg
        msg = ''
    await bot_send(bot, event, msg, parse_mode='Markdown', photo=photo, image_width=image_width)


@on_command("me", block=True).handle()
@check_session_handler
async def me(bot: Bot, event: Event):
    user_id = event.get_user_id()

    msg = await get_me(user_id)
    await bot_send(bot, event, msg, parse_mode='Markdown')


@on_command("friends", aliases={'fr'}, block=True).handle()
@check_session_handler
async def friends(bot: Bot, event: Event):
    get_text = False
    cmd_lst = event.get_plaintext().strip().split()
    if 't' in cmd_lst or 'text' in cmd_lst:
        get_text = True

    msg = await get_friends_msg(event.get_user_id(), get_text)
    await bot_send(bot, event, msg, parse_mode='Markdown', image_width=600)


@on_command("ns_friends", aliases={'ns'}, block=True).handle()
@check_session_handler
async def ns_friends(bot: Bot, event: Event):
    msg = await get_ns_friends_msg(event.get_user_id())
    await bot_send(bot, event, msg, parse_mode='Markdown', image_width=680)


@on_command("x_top", block=True).handle()
async def x_top(bot: Bot, event: Event):
    msg = await get_x_top_msg()
    await bot_send(bot, event, msg, parse_mode='Markdown')


@on_command("my_schedule", block=True).handle()
@check_session_handler
async def schedule(bot: Bot, event: Event):
    msg = await get_my_schedule_msg(event.get_user_id())
    await bot_send(bot, event, msg, parse_mode='Markdown')


@on_command("screen_shot", aliases={'ss'}, block=True).handle()
@check_session_handler
async def screen_shot(bot: Bot, event: Event):
    key = ''
    if ' ' in event.get_plaintext():
        key = event.get_plaintext().split(' ', 1)[1].strip()
    img = await get_screenshot_image(event.get_user_id(), key=key)
    message = ''
    if not img:
        message = '网络错误，或指令不对。'
    await bot_send(bot, event, message=message, photo=img)


@on_command("history", block=True).handle()
@check_session_handler
async def history(bot: Bot, event: Event):
    _type = 'open'
    await bot_send(bot, event, '`开始努力作图，请稍等~`', parse_mode='Markdown', skip_log_cmd=True)

    cmd_message = event.get_plaintext()[8:].strip()
    logger.debug(f'history: {cmd_message}')
    if cmd_message:
        cmd_lst = cmd_message.split()
        if 'e' in cmd_lst or 'event' in cmd_lst:
            _type = 'event'
        if 'f' in cmd_lst or 'fest' in cmd_lst:
            _type = 'fest'

    msg = await get_history_msg(event.get_user_id(), _type=_type)
    await bot_send(bot, event, msg, parse_mode='Markdown', image_width=1000)


@on_command("friend_code", aliases={'fc'}, block=True).handle()
@check_session_handler
async def friend_code(bot: Bot, event: Event):
    msg = get_friend_code(event.get_user_id())
    await bot_send(bot, event, msg, parse_mode='Markdown')


@on_command("top", block=True).handle()
@check_session_handler
async def _top(bot: Bot, event: Event):

    cmd_message = event.get_plaintext()[4:].strip()
    logger.debug(f'top: {cmd_message}')
    battle = None
    player = None
    if cmd_message:
        cmd_lst = cmd_message.split()
        for cmd in cmd_lst:
            cmd = cmd.strip()
            if not cmd:
                continue
            if cmd.isdigit():
                battle = int(cmd)
            else:
                player = cmd.lower()

    if battle:
        battle = max(1, battle)
        battle = min(50, battle)
    if player:
        if len(player) != 1 or player not in 'abcdefgh':
            player = 1
        else:
            player = ord(player) - ord('a') + 1

    if battle and not player:
        player = 1
    if player and not battle:
        battle = 1

    _msg = '查无数据'
    photo = await get_top(event.get_user_id(), battle, player)
    if photo:
        if not photo.startswith('###'):
            _msg += f', {photo}'
        else:
            _msg = photo
    await bot_send(bot, event, _msg)
