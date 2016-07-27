# -*- coding: utf-8 -*-
##############################################################################
#
#    hr_holidays_workingdays module for OpenERP, Compute number of day requested without days not worked in company
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.syleam.fr>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of hr_holidays_workingdays
#
#    hr_holidays_workingdays is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    hr_holidays_workingdays is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv
import datetime
from dateutil.rrule import rrule, rruleset, HOURLY, MO, TU, WE, TH, FR, SA, SU
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from dateutil import tz
import time


class HrHolidays(osv.osv):
    _inherit = 'hr.holidays'

    def _get_nb_of_days(self, cr, uid, from_dt, to_dt, employee_id):
        """Returns a float equals to the timedelta between two dates given as string."""
        user = self.pool['res.users'].browse(cr, uid, uid)
        company = user.company_id
        local_zone = tz.gettz(user.tz or 'Europe/Paris')
        local_time = local_zone.utcoffset(from_dt).total_seconds() / 60 / 60
        opening_time = int(company.opening_time - local_time)
        closing_time = int(company.closing_time - local_time)
        midday = ((closing_time - opening_time) / 2) + opening_time
        if int(from_dt.hour) < midday:
            from_dt = from_dt.replace(hour=opening_time, minute=0, second=0)
        else:
            from_dt = from_dt.replace(hour=midday, minute=0, second=0)
        if int(to_dt.hour) < midday:
            to_dt = to_dt.replace(hour=midday, minute=0, second=0)
        else:
            to_dt = to_dt.replace(hour=closing_time, minute=0, second=0)
        diff_day = rruleset()
        # Search all date between from and to date
        diff_day.rrule(rrule(HOURLY, byhour=[opening_time + 1, closing_time - 1], dtstart=from_dt, until=to_dt))
        # Exclude all days not worked
        available_weekdays = []
        if employee_id:
            employee = self.pool.get('hr.employee').browse(cr, uid, employee_id)
            if employee.contract_id and employee.contract_id.working_hours:
                # List available weekdays
                days = list(set([attendance.dayofweek for attendance in employee.contract_id.working_hours.attendance_ids]))
                if '0' in days:
                    available_weekdays.append(MO)
                if '1' in days:
                    available_weekdays.append(TU)
                if '2' in days:
                    available_weekdays.append(WE)
                if '3' in days:
                    available_weekdays.append(TH)
                if '4' in days:
                    available_weekdays.append(FR)
                if '5' in days:
                    available_weekdays.append(SA)
                if '6' in days:
                    available_weekdays.append(SU)
        if not available_weekdays:
            if not company.workingday_monday:
                available_weekdays.append(MO)
            if not company.workingday_tuesday:
                available_weekdays.append(TU)
            if not company.workingday_wednesday:
                available_weekdays.append(WE)
            if not company.workingday_thursday:
                available_weekdays.append(TH)
            if not company.workingday_friday:
                available_weekdays.append(FR)
            if not company.workingday_saturday:
                available_weekdays.append(SA)
            if not company.workingday_sunday:
                available_weekdays.append(SU)
        diff_day.exrule(rrule(HOURLY, byweekday=available_weekdays, dtstart=from_dt))
        diff_day = self.pool['res.country.workdates'].not_worked(cr, uid, company.country_id.id, diff_day, from_dt, to_dt)
        diff_day = diff_day.count() / 2.
        date_from = from_dt.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        date_to = to_dt.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        return diff_day, date_from, date_to

    def onchange_date_from(self, cr, uid, ids, date_to, date_from):
        """
        If there are no date set for date_to, automatically set one 8 hours later than
        the date_from.
        Also update the number_of_days.
        """
        result = super(HrHolidays, self).onchange_date_from(cr, uid, ids, date_to, date_from)
        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            from_dt = datetime.datetime.fromtimestamp(time.mktime(time.strptime(date_from, DEFAULT_SERVER_DATETIME_FORMAT)))
            to_dt = datetime.datetime.fromtimestamp(time.mktime(time.strptime(date_to, DEFAULT_SERVER_DATETIME_FORMAT)))
            if (to_dt - from_dt).days >= 1:
                diff_day, date_from, date_to = self._get_nb_of_days(cr, uid, from_dt, to_dt)
                result = {'value': {
                    'number_of_days_temp': diff_day,
                    'date_from': date_from,
                    'date_to': date_to,
                }}
        return result

    def onchange_date_to(self, cr, uid, ids, date_to, date_from):
        """
        Update the number_of_days.
        """
        result = super(HrHolidays, self).onchange_date_to(cr, uid, ids, date_to, date_from)
        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            from_dt = datetime.datetime.fromtimestamp(time.mktime(time.strptime(date_from, DEFAULT_SERVER_DATETIME_FORMAT)))
            to_dt = datetime.datetime.fromtimestamp(time.mktime(time.strptime(date_to, DEFAULT_SERVER_DATETIME_FORMAT)))
            if (to_dt - from_dt).days >= 1:
                diff_day, date_from, date_to = self._get_nb_of_days(cr, uid, from_dt, to_dt)
                result = {'value': {
                    'number_of_days_temp': diff_day,
                    'date_from': date_from,
                    'date_to': date_to,
                }}
        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
