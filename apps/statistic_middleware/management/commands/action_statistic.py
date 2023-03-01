import logging

from django.core.management import BaseCommand, CommandParser

from apps.middleware_custom import models


class Command(BaseCommand):
    help = "Delete all actions statistic info"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "-del",
            help="Delete ALL action statistic records",
            action="store_true",
        )

    def handle(self, *args, **kwargs):
        current_records = models.ActionStatistic.objects.all().count()

        if kwargs["del"]:
            all_info = models.ActionStatistic.objects.all()
            all_info.delete()

        records_after_deleting = models.ActionStatistic.objects.all().count()
        deleted_records = current_records - records_after_deleting

        self.stdout.write(
            self.style.SQL_TABLE("  Actual visit statistic records BEFORE deleting: %s" % (current_records))
        )
        self.stdout.write(self.style.WARNING("  Visit statistic records deleted with success: %s" % (deleted_records)))
        self.stdout.write(
            self.style.SUCCESS("  Actual visit statistic records AFTER deleting: %s" % (records_after_deleting))
        )