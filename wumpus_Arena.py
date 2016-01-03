__author__ = 'Jasper'


class Arena():
    def __init__(self, row_limit, col_limit):
        self.row_limit = row_limit
        self.col_limit = col_limit
        self.array = self.arena_array()

    def arena_array(self):
        return [['-' for col in xrange(self.col_limit)] for
                row in xrange(self.row_limit)]

