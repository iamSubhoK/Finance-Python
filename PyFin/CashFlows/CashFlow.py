# -*- coding: utf-8 -*-
u"""
Created on 2017-6-7

@author: cheng.li
"""

from PyFin.Env.Settings import Settings


class CashFlow(object):

    def __init__(self):
        pass

    def date(self):
        pass

    def amount(self):
        pass

    def ex_coupon_date(self):
        return None

    def trading_ex_coupon(self, ref_date=None):
        ecd = self.ex_coupon_date()

        if not ecd:
            return False
        else:
            ref_date = ref_date if ref_date else Settings.evaluationDate
            return ecd <= ref_date

    def has_occurred(self, ref_date=None, include_ref_date=False):
        if ref_date:
            cf = self.date()
            if ref_date < cf:
                return False
            elif cf < ref_date:
                return True

        if (not ref_date) or ref_date == Settings.evaluationDate:
            ref_date = Settings.evaluationDate
            include_today = Settings.includeTodaysCashFlows

            if include_today:
                include_ref_date = include_today

        if include_ref_date:
            return self.date() < ref_date
        else:
            return self.date() <= ref_date