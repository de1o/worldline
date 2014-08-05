#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import os
import functools


emoticons = [
    """(⌒▽⌒)""",
    """（￣▽￣）""",
    """(=・ω・=)""",
    """(｀・ω・´)""",
    """(〜￣△￣)〜""",
    """(･∀･)""",
    """(°∀°)ﾉ""",
    """(￣3￣)""",
    """╮(￣▽￣)╭""",
    """( ´_ゝ｀)""",
    """←_←""",
    """→_→""",
    """(<_<)""",
    """(>_>)""",
    """(;¬_¬)""",
    """("▔□▔)/""",
    """(ﾟДﾟ≡ﾟдﾟ)!?""",
    """Σ(ﾟдﾟ;)""",
    """Σ( ￣□￣||)""",
    """(´；ω；`)""",
    """（/TДT)/""",
    """(^・ω・^ )""",
    """(｡･ω･｡)""",
    """(●￣(ｴ)￣●)""",
    """ε=ε=(ノ≧∇≦)ノ""",
    """(´･_･`)""",
    """(-_-#)""",
    """（￣へ￣）""",
    """(￣ε(#￣)Σ""",
    """ヽ(`Д´)ﾉ""",
    """(╯°口°)╯(┴—┴""",
    """（#-_-)┯━┯""",
    """_(:3」∠)_""",
]


def moemoeda(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        func(*args, **kwargs)
        emoticon = get_random_emoticon()
        print emoticon
    return decorator


def taihen(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("世界线跳跃发生异常，时光机卡在时空裂隙中，Good Luck..."),
    return decorator


def calc_divergence_value(commit_a, commit_b):
    diff_cmd = "git diff --shortstat %s %s --exit-code" % (commit_a, commit_b)
    dp = os.popen(diff_cmd)

    dp_buf = dp.read().split()

    delete_delta = 0
    insert_delta = 0
    for index, part in enumerate(dp_buf):
        if 'deletion' in part:
            delete_delta = int(dp_buf[index-1])
        elif 'insertion' in part:
            insert_delta = int(dp_buf[index-1])

    delta = insert_delta + delete_delta
    return delta


def calc_world_base_value():
    total_cnt_cmd = "git ls-files|grep '.py\|.css\|.html\|.js' |xargs cat 2>&-|wc -l|tail -1"
    tp = os.popen(total_cnt_cmd)
    total = int(tp.read())
    return total


def get_last_two_commit_hash():
    cmd = "git log --pretty=oneline -2"
    p = os.popen(cmd)
    buf = p.readlines()
    return buf[0].split()[0], buf[1].split()[0]


def get_random_emoticon():
    import random
    emoticon_index = random.randint(0, len(emoticons)-1)
    emoticon = emoticons[emoticon_index]

    return emoticon


@moemoeda
@taihen
def when_checkout(argv):
    if argv[3] != '1':
        return
    if argv[1] == argv[2]:
        print("世界线收束至同一位置"),
        return
    delta = calc_divergence_value(sys.argv[1], sys.argv[2])
    total = calc_world_base_value()
    print("世界线变动率%6f..." % (delta/total)),


@moemoeda
# @taihen
def when_commit():
    commit_a, commit_b = get_last_two_commit_hash()
    delta = calc_divergence_value(commit_a, commit_b)
    print("本次time leap导致世界线偏离了%6f" % (delta/calc_world_base_value())),


@moemoeda
@taihen
def when_merge():
    commit_a, commit_b = get_last_two_commit_hash()
    delta = calc_divergence_value(commit_a, commit_b)
    total = calc_world_base_value()
    print("受到另一世界线的影响，本世界线偏移了%6f" % (delta/total)),
