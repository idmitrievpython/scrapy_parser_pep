import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.constants import BASE_DIR, HEADERS_PEP_TABLE, TIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.status_count.values())
        filename = 'status_summary_{datetime}.csv'.format(
            datetime=datetime.now().strftime(TIME_FORMAT)
        )
        total_status = ('Total', total)
        result_path = BASE_DIR / 'results'
        result_path.mkdir(exist_ok=True)
        filepath = result_path / filename

        with open(filepath, mode='w', encoding='utf-8') as csvfile:
            status_wtiter = csv.writer(csvfile, dialect=csv.unix_dialect)
            status_wtiter.writerow(HEADERS_PEP_TABLE)
            for type_status in self.status_count.items():
                status_wtiter.writerow(type_status)
            status_wtiter.writerow(total_status)
