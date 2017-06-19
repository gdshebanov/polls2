from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.question

    def count_choices(self):
        return self.choice_set.count()

    def count_total_votes(self):
        result = 0
        for choice in self.choice_set.all():
            result += choice.count_votes()
        return result

    def can_vote(self, ip_address):
        return not self.vote_set.filter(ip_address=ip_address, poll=self).exists()

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=255)

    def count_votes(self):
        return self.vote_set.count()

    def __str__(self):
        return self.choice

class Vote(models.Model):
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    voter_name = models.CharField('Имя', max_length=60, blank=True, null=True)
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)

    def __str__(self):
        return self.ip_address

    class Meta:
        unique_together = ('ip_address', 'poll')
