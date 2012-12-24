# -*- coding: utf-8 -*-
##############################################################################
#
#    hr_holidays_workingdays module for OpenERP, Compute days of holiday depending working days
#    Copyright (C) 2012 SYLEAM Info Services (<http://www.syleam.fr/>)
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

from osv import osv
from dateutil.rrule import rrule, rruleset, DAILY, MO, TU, WE, TH, FR, SA, SU
from datetime import datetime


class hr_holidays(osv.osv):
    _inherit = "hr.holidays"

    def onchange_date_from(self, cr, uid, ids, date_to, date_from, employee_id=None):
        result = {}
        company = self.pool.get('res.users').browse(cr, uid, uid).company_id

        if date_to and date_from:
            employee = self.pool.get('hr.employee').browse(cr, uid, employee_id)
            available_weekdays = []
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
            if company.country_id:
                if not available_weekdays:
                    # List available weekdays
                    if company.workingday_monday:
                        available_weekdays.append(MO)
                    if company.workingday_tuesday:
                        available_weekdays.append(TU)
                    if company.workingday_wednesday:
                        available_weekdays.append(WE)
                    if company.workingday_thursday:
                        available_weekdays.append(TH)
                    if company.workingday_friday:
                        available_weekdays.append(FR)
                    if company.workingday_saturday:
                        available_weekdays.append(SA)
                    if company.workingday_sunday:
                        available_weekdays.append(SU)

            if available_weekdays:
                # List all possible days
                diff_day = rruleset()
                diff_day.rrule(rrule(
                    DAILY,
                    byweekday=available_weekdays,
                    dtstart=datetime.strptime(date_from, '%Y-%m-%d %H:%M:%S'),
                    until=datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S')
                ))

                # Exclude not worked days from list
                dates_list = list(diff_day)
                # Deletes the not working days for the selected country
                if company.country_id:
                    diff_day = self.pool.get('res.country.workdates').not_worked(cr, uid, company.country_id.id, diff_day, dates_list[0], dates_list[-1])
                    dates_list = list(diff_day)
                result['value'] = {
                    'number_of_days_temp': len(dates_list)
                }
            else:
                diff_day = self._get_number_of_days(date_from, date_to)
                result['value'] = {
                    'number_of_days_temp': round(diff_day) + 1
                }
            return result
        result['value'] = {
            'number_of_days_temp': 0,
        }
        return result

hr_holidays()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
