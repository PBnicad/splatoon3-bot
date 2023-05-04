
from nonebot import logger, on_startswith, on_command, get_driver
from nonebot.adapters import Event, Bot
from nonebot.adapters.telegram import Bot as TGBot
from nonebot.adapters.onebot.v11 import Bot as QQBot

from .db_sqlite import set_db_info, get_user, get_or_set_user
from .sp3bot import get_user_db_info, get_last_battle_or_coop, get_me, push_latest_battle
from .sp3msg import MSG_HELP, MSG_HELP_QQ, get_statics
from .utils import INTERVAL, bot_send, check_user_login

from .cmd_get import *
from .cmd_push import *
from .cmd_set import *


@on_startswith(("/", "、"), priority=1, block=False).handle()
async def all_command(bot: Bot, event: Event):
    data = {'user_id': event.get_user_id()}
    _event = event.dict() or {}
    if isinstance(bot, TGBot):
        data.update({
            'id_type': 'tg',
            'username': _event.get('from_', {}).get('username', ''),
            'first_name': _event.get('from_', {}).get('first_name', ''),
            'last_name': _event.get('from_', {}).get('last_name', ''),
        })
        if _event.get('chat', {}).get('type') == 'group':
            data.update({
                'group_id': _event['chat']['id'],
                'group_name': _event.get('chat', {}).get('title', ''),
            })
    elif isinstance(bot, QQBot):
        data.update({
            'id_type': 'qq',
            'username': _event.get('sender', {}).get('nickname', ''),
        })
        if _event.get('group_id'):
            try:
                group_info = await bot.call_api('get_group_info', group_id=_event['group_id'])
            except Exception as e:
                logger.error(e)
                group_info = {}
            data.update({
                'group_id': _event['group_id'],
                'group_name': group_info.get('group_name', ''),
            })
    set_db_info(**data)


@on_startswith(("/", "、"), priority=10).handle()
async def unknown_command(bot: Bot, event: Event):
    logger.info(f'unknown_command {event.get_event_name()}')
    if 'private' in event.get_event_name():
        _msg = "Sorry, I didn't understand that command. /help\nOr permission denied /login first."
        if isinstance(bot, QQBot):
            _msg = '无效命令，输入 /help 查看帮助\n或无权限查看，请先 /login 登录'
        logger.info(_msg)
        await bot.send(event, message=_msg)


@on_command("help", aliases={'h', '帮助', '说明', '文档'}, block=True).handle()
async def _help(bot: Bot, event: Event):
    if isinstance(bot, TGBot):
        await bot.send(event, message=MSG_HELP, disable_web_page_preview=True)

    elif isinstance(bot, QQBot):
        await bot_send(bot, event, message=MSG_HELP_QQ)


@get_driver().on_startup
async def bot_on_start():
    version = utils.BOT_VERSION
    logger.info(f' bot start, version: {version} '.center(120, '-'))
