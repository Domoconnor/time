import re
from datetime import datetime, timedelta

class Chrono():

    indicators = {
        'night': 22,
        'evening': 18,
        'afternoon': 13,
        'morning': 9
    }

    def parse(self, string, reference):
        pattern = 'now|tonight|(this|tomorrow|yesterday)\s(night|evening|morning|afternoon)|tomorrow|yesterday'
        string = string.lower()

        match = re.search(pattern, string)




        if match:
            if match.group(0) == 'now':
                return reference

            if match.group(0) == 'tomorrow':
                return reference + timedelta(hours=24)

            if match.group(0) == 'yesterday':
                return reference + timedelta(hours=-24)

            if match.group(0) == 'tonight':
                return reference.replace(hour=self.indicators['night'])

            if match.group(1) and match.group(2):
                newDate = reference

                newDate = newDate.replace(hour=self.indicators[match.group(2)])

                if match.group(1) == 'tomorrow':
                    return newDate + timedelta(hours=24)

                if match.group(1) == 'yesterday':
                    return newDate + timedelta(hours=-24)



