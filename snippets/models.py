from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Get available lexers and styles from Pygments
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        # Get the appropriate lexer for the code's language
        lexer = get_lexer_by_name(self.language)
        
        # Set line numbers if required
        linenos = 'table' if self.linenos else False
        
        # Include the title if it's provided
        options = {'title': self.title} if self.title else {}
        
        # Create the formatter using the selected style and options
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        
        # Generate the highlighted HTML version of the code
        self.highlighted = highlight(self.code, lexer, formatter)
        
        # Call the parent class's save method to actually save the object
        super().save(*args, **kwargs)

