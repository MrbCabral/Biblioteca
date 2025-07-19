# books/models.py
from django.db import models

class Book(models.Model):
    """
    Modelo para representar um livro no catálogo da biblioteca.
    """
    title = models.CharField(max_length=255, verbose_name="Título")
    author = models.CharField(max_length=255, verbose_name="Autor")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    publisher = models.CharField(max_length=255, verbose_name="Editora")
    publication_year = models.IntegerField(verbose_name="Ano de Publicação")
    genre = models.CharField(max_length=100, blank=True, null=True, verbose_name="Gênero")
    synopsis = models.TextField(blank=True, null=True, verbose_name="Sinopse")

    def __str__(self):
        return f"{self.title} ({self.author})"

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

class Copy(models.Model):
    """
    Modelo para representar um exemplar físico de um livro.
    """
    STATUS_CHOICES = [
        ('Available', 'Disponível'),
        ('Loaned', 'Emprestado'),
        ('Reserved', 'Reservado'),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies', verbose_name="Livro")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available', verbose_name="Status")

    def __str__(self):
        return f"Cópia de {self.book.title} ({self.status})"

    class Meta:
        verbose_name = "Exemplar"
        verbose_name_plural = "Exemplares"