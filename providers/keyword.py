from transaction.models import Keyword

def get_keywords_description(description_words):
    return Keyword.objects.filter(keyword__in=description_words).select_related('merchant__category')