from django.db import models
from common.models import CommonModel
from django.db.models import Count
from django.core.exceptions import ValidationError
from comments.models import Recomment


class Feed(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="feeds",
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    visited = models.PositiveIntegerField(
        editable=False,
        default=0,
    )

    def __str__(self) -> str:
        return f"{self.user}의 게시글"

    @property
    def like_count(self):
        return self.feedlike.count()

    # @property
    # def comments_count(self):
    #     count = self.comment.count()
    #     for i in self.comment.all():
    #         count += i.recomment.count()
    #     return count

    # @property
    # def comments_count(self):
    #     count = self.comment.count()
    #     for i in self.comment.prefetch_related("recomment"):
    #         count += i.recomment.count()
    #     return count

    @property
    def comments_count(self):
        return self.comment.count() + self.comment.aggregate(
            recomment_count=Count("recomment")
        ).get("recomment_count")

    @property
    def highest_like_comments(self):
        return self.comment.annotate(like_count=Count("commentlike")).order_by(
            "-like_count"
        )[:1]

    # @property
    # def thumbnail(self):
    #     if self.images.exists():
    #         return self.images.value_list("url", flat=True).first()
    #     else:
    #         return None
    # @property
    # def thumbnail(self):
    #     if self.images.exists():
    #         return self.images.all()[0].url
    #     else:
    #         return None
    @property
    def thumbnail(self):
        image = self.images.first()
        if image:
            return image.url
        else:
            return None

    def clean(self):
        super().clean()
        if self.category.group != self.group:
            raise ValidationError("그룹의 카테고리 내에서 선택해주세요.")
