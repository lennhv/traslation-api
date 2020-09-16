import time
import pygsheets
from celery import task
from celery.utils.log import get_task_logger
from django.conf import settings

from .models import Traslation

log = get_task_logger(__name__)


@task
def traslate_task(**kwargs):
    """
    Task to traslate some text using google spreadsheet
    """
    log.debug("task kwargs %s", str(kwargs))
    client = pygsheets.authorize(service_file=settings.GSHEET_SERVICE_CONFIG)
    gsheet = client.create("sheet-%s" % kwargs["id"])
    wks = gsheet.sheet1

    words = kwargs["text"]

    for i, word in enumerate(words):
        row_idx = "A%s" % str(i+1)
        traslator = '=GOOGLETRANSLATE(%s,"%s","%s")' % (
                    row_idx, kwargs['lang_source'], kwargs['lang_target'])
        wks.update_row(i+1, [word, traslator])

    time.sleep(5) # wait for traslations

    traslation = []
    for i, word in enumerate(words):
        row_idx = "B%s" % str(i+1)
        _word = word
        for i in range(10):
            _word = wks.get_value(row_idx)
            if _word != 'Loading...':
                break
            time.sleep(2)
        traslation.append(_word)
    log.debug("traslation %s", str(traslation))

    Traslation.objects.save_traslation(kwargs["id"], traslation)

    return True
