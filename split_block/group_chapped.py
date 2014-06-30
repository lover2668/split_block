# -*- coding: utf-8 -*-

from .item import SplitBlock
from .group_ext import z

class SplitBlockGroupChapped(object):

    def maybe_chapped_groups(self):
        """ Find continuous chapped SplitBlockGroup. """
        chapped_groups = []

        current_chapped_group = []
        for idx1, sb1 in enumerate(self):
            if sb1.is_letter and (not sb1.is_regular):
                current_chapped_group.append(sb1)

            if len(current_chapped_group) and sb1.is_blank:
                current_chapped_group.append(sb1)

            if sb1.is_other or (sb1.is_letter and sb1.is_regular) or (idx1 == (len(self) - 1 )):
                if len(current_chapped_group) > 2: chapped_groups.append(current_chapped_group)
                current_chapped_group = []

        return chapped_groups
