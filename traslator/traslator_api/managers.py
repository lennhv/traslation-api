from django.db import models
from django.utils import timezone


class TraslationManager(models.Manager):

    def create_task(self, **kwargs):
        """ 
        """
        from .tasks import traslate_task
        task = self.model(
            lang_source=kwargs["lang_source"],
            lang_target=kwargs["lang_target"],
            text=self.model.SPLIT_CHAR.join(kwargs["text"])
        )
        task.save(using=self._db)
        # to task
        kwargs["id"] = task.id
        print("kwargs", kwargs)
        # traslate_task.delay(kwargs['id'], kwargs['text'], kwargs['lang_source'], kwargs['lang_target'])
        traslate_task.delay(**kwargs)
        return task

    def save_traslation(self, id, traslation, sucess=True):
        self.model.objects.filter(id=id).\
            update(traslation=self.model.SPLIT_CHAR.join(traslation),
                   status=self.model.TRASLATED if sucess else self.model.FAILED,
                   finish_time=timezone.now())
