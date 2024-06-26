# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-06-22 11:20
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import parler


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        unique=True,
                        verbose_name="Category",
                    ),
                ),
            ],
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Progress",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score",
                    models.CharField(
                        max_length=1024,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^\\d+(?:\\,\\d+)*\\Z", 32),
                                code="invalid",
                                message="Enter only digits separated by commas.",
                            )
                        ],
                        verbose_name="Score",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Progress",
                "verbose_name_plural": "User progress records",
            },
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "figure",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="uploads/%Y/%m/%d",
                        verbose_name="Figure",
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        help_text="Enter the question text that you want displayed",
                        max_length=1000,
                        verbose_name="Question",
                    ),
                ),
                (
                    "explanation",
                    models.TextField(
                        blank=True,
                        help_text="Explanation to be shown after the question has been answered.",
                        max_length=2000,
                        verbose_name="Explanation",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.Category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "Questions",
                "ordering": ["category"],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=60, verbose_name="Title")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="a description of the quiz",
                        verbose_name="Description",
                    ),
                ),
                (
                    "url",
                    models.SlugField(
                        help_text="a user friendly url",
                        max_length=60,
                        verbose_name="user friendly url",
                    ),
                ),
                (
                    "random_order",
                    models.BooleanField(
                        default=False,
                        help_text="Display the questions in a random order or as they are set?",
                        verbose_name="Random Order",
                    ),
                ),
                (
                    "max_questions",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Number of questions to be answered on each attempt.",
                        null=True,
                        verbose_name="Max Questions",
                    ),
                ),
                (
                    "answers_at_end",
                    models.BooleanField(
                        default=False,
                        help_text="Correct answer is NOT shown after question. Answers displayed at the end.",
                        verbose_name="Answers at end",
                    ),
                ),
                (
                    "exam_paper",
                    models.BooleanField(
                        default=False,
                        help_text="If yes, the result of each attempt by a user will be stored. Necessary for marking.",
                        verbose_name="Exam Paper",
                    ),
                ),
                (
                    "single_attempt",
                    models.BooleanField(
                        default=False,
                        help_text="If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.",
                        verbose_name="Single Attempt",
                    ),
                ),
                (
                    "pass_mark",
                    models.SmallIntegerField(
                        blank=True,
                        default=0,
                        help_text="Percentage required to pass exam.",
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="Pass Mark",
                    ),
                ),
                (
                    "success_text",
                    models.TextField(
                        blank=True,
                        help_text="Displayed if user passes.",
                        verbose_name="Success Text",
                    ),
                ),
                (
                    "fail_text",
                    models.TextField(
                        blank=True,
                        help_text="Displayed if user fails.",
                        verbose_name="Fail Text",
                    ),
                ),
                (
                    "draft",
                    models.BooleanField(
                        default=False,
                        help_text="If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.",
                        verbose_name="Draft",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.Category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={"verbose_name": "Quiz", "verbose_name_plural": "Quizzes"},
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Sitting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question_order",
                    models.CharField(
                        max_length=1024,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^\\d+(?:\\,\\d+)*\\Z", 32),
                                code="invalid",
                                message="Enter only digits separated by commas.",
                            )
                        ],
                        verbose_name="Question Order",
                    ),
                ),
                (
                    "question_list",
                    models.CharField(
                        max_length=1024,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^\\d+(?:\\,\\d+)*\\Z", 32),
                                code="invalid",
                                message="Enter only digits separated by commas.",
                            )
                        ],
                        verbose_name="Question List",
                    ),
                ),
                (
                    "incorrect_questions",
                    models.CharField(
                        blank=True,
                        max_length=1024,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^\\d+(?:\\,\\d+)*\\Z", 32),
                                code="invalid",
                                message="Enter only digits separated by commas.",
                            )
                        ],
                        verbose_name="Incorrect questions",
                    ),
                ),
                ("current_score", models.IntegerField(verbose_name="Current Score")),
                (
                    "complete",
                    models.BooleanField(default=False, verbose_name="Complete"),
                ),
                (
                    "user_answers",
                    models.TextField(
                        blank=True, default="{}", verbose_name="User Answers"
                    ),
                ),
                (
                    "start",
                    models.DateTimeField(auto_now_add=True, verbose_name="Start"),
                ),
                (
                    "end",
                    models.DateTimeField(blank=True, null=True, verbose_name="End"),
                ),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.Quiz",
                        verbose_name="Quiz",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={"permissions": (("view_sittings", "Can see completed exams."),)},
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sub_category",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Sub-Category",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.Category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sub-Category",
                "verbose_name_plural": "Sub-Categories",
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name="question",
            name="quiz",
            field=models.ManyToManyField(
                blank=True, to="quiz.Quiz", verbose_name="Quiz"
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="sub_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.SubCategory",
                verbose_name="Sub-Category",
            ),
        ),
    ]
