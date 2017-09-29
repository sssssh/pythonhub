"""
pickle模块是Python内部的一种格式，用来完成对象的持久化
pickle模块可以将一个复杂的对象转换为一个字节数组并且使
用相同的内部结构将字节流转换为一个对象。
将字节流写入文件或许最常见的场景，但也
可能输出到网络进行传输或是数据库。
pickle关注的只有python。
"""
import pickle
import logging
import sys

audit_log = logging.getLogger("audit")
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

with open('travel_blog.p', 'wb') as target:  # 文件的写入使用了纯字节
    pickle.dump(travel, target)

with open('travel_blog.p', 'rb') as source:
    copy = pickle.load(source)


class Hand_x:
    def __init__(self, dealer_card, *card):
        self.dealer_card = dealer_card
        self.cards = list(cards)
        for c in self.cards:
            audit_log.info("Initial %s", c)

    def append(self, card):
        self.cards.append(card)
        audit_log.info("Hit %s", card)

    def __str__(self):
        cards = ", ".join(map(str, self.cards))
        return "{self.dealer_card} | {cards}".format(self=self,
                                                     cards=cards)


class Hand2:
    def __init__(self, dealer_card, *card):
        self.dealer_card = dealer_card
        self.cards = list(cards)
        for c in self.cards:
            audit_log.info("Initial %s", c)

    def append(self, card):
        self.cards.append(card)
        audit_log.info("Hit %s", card)

    def __str__(self):
        cards = ", ".join(map(str, self.cards))
        return "{self.dealer_card} | {cards}".format(self=self,
                                                     cards=cards)
        def __getattribute__(self):
            return self.__dict__
        def __setattr__(self, state):
            self.__dict__.update(state)
            for c in self.cards:
                audit_log.info("Initial (unpickle) %s", c)


import builtins
class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "builtins":
            if name not in ("exec", "eval"):
                return getattr(builtins, name)
        elif module == "__main__":
            return globals()[name]
        # elif module in any of our application modules...
        raise pickle.UnpicklingError(
            "global '{module}.{name}' is forbidden".format(module=module,
                                                           name=name)
