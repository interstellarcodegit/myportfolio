
from django.db import models
# from django.utils import timezone
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    types=[
        ('tech','termux'),
        ('code','coding'),
        ('termux','Technology'),
    ]
    MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
]
    typeof= models.CharField(max_length=30,choices=types, default="code")
    date_published= models.DateTimeField('date published')
    image= models.FileField(null=True, upload_to='files')#max_length
    def __str__(self):
        return self.title
        
class Entry(models.Model):
    blog = models.ForeignKey(BlogPost)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self):
        return self.headline
