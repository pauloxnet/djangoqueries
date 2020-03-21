from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
)
from django.db import models

search_vectors = (
    SearchVector("nickname", weight="A", config="english")
    + SearchVector(
        StringAgg("genres__name", delimiter=" "), weight="B", config="english"
    )
    + SearchVector("description", weight="D", config="english")
)


class BandManager(models.Manager):
    def search(self, text):
        search_query = SearchQuery(text, config="english")
        search_rank = SearchRank(search_vectors, search_query)
        trigram_similarity = TrigramSimilarity("nickname", text)
        return (
            self.get_queryset()
            .annotate(search=search_vectors)
            .filter(search=search_query)
            .annotate(rank=search_rank + trigram_similarity)
            .order_by("-rank")
        )
