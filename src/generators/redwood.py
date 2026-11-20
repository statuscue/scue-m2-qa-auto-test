import string
from datetime import datetime

from data.bluewood_data import balances, productItems
from utils.utils import Utils


class RedWood:
    def __init__(self):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.page = Utils.random_data(size=1, chars=string.digits)
        self.first = Utils.random_data(size=2, chars=string.digits)

    def generate_bluewood_data(self, base_data: str, date: str = None, page: str = None, first: str = None):
        return base_data % (date, page, first) if not date and page and first \
            else base_data % (self.date, self.page, self.first)


if __name__ == '__main__':
    r = RedWood()
    x = r.generate_bluewood_data(balances)
    y = r.generate_bluewood_data(productItems)
