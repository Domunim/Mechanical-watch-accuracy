import csv
from os.path import exists


class Watch:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def add_watch(self, watch):

        Watch.watch = watch

        watch = [self.make, self.model]
        table_exists = exists('watches_table.csv')

        if table_exists:
            with open('watches_table.csv', 'a') as watches_table:

                writer = csv.writer(watches_table)
                writer.writerow(watch)

        else:
            with open('watches_table.csv', 'w') as watches_table:
                column_names = ['Make', 'Model', 'Measurements']

                writer = csv.writer(watches_table)
                writer.writerow(column_names)
                writer.writerow(watch)

    # def delete_watch(self, watch):
    #     if
    #         import csv
    #
    #         with open("watches_table.csv", "r") as original:
    #             reader_obj = csv.reader(original)
    #
    #             with open("new_table.csv", "w") as new:
    #                 writer_obj = csv.writer(new)
    #                 for column in reader_obj:
    #                     writer_obj.writerow(())
