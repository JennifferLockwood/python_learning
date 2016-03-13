from django.db import models


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."

def run_test():
    e = Entry()
    e.text = "Short text"
    print(e.__str__())
    e.text = "Long text is long.  It goes over 50 chars.  Long text is long.  It goes over 50 chars.  Long text is long.  It goes over 50 chars.  Long text is long.  It goes over 50 chars.  Long text is Long text is long.  It goes over 50 chars.  long.  It goes over 50 chars.  Long text is long.  It goes over 50 chars.  "
    print(e.__str__())

if __name__ == "__main__":
    run_test()