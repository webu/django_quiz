# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-06-22 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import parler


class Migration(migrations.Migration):
    initial = True

    dependencies = [("quiz", "__first__")]

    operations = [
        migrations.CreateModel(
            name="Answer",
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
                    "content",
                    models.CharField(
                        help_text="Enter the answer text that you want displayed",
                        max_length=1000,
                        verbose_name="Content",
                    ),
                ),
                (
                    "correct",
                    models.BooleanField(
                        default=False,
                        help_text="Is this a correct answer?",
                        verbose_name="Correct",
                    ),
                ),
            ],
            options={"verbose_name": "Answer", "verbose_name_plural": "Answers"},
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="MCQuestion",
            fields=[
                (
                    "question_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="quiz.Question",
                    ),
                ),
                (
                    "answer_order",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("content", "Content"),
                            ("random", "Random"),
                            ("none", "None"),
                        ],
                        help_text="The order in which multichoice answer options are displayed to the user",
                        max_length=30,
                        null=True,
                        verbose_name="Answer Order",
                    ),
                ),
            ],
            options={
                "verbose_name": "Multiple Choice Question",
                "verbose_name_plural": "Multiple Choice Questions",
            },
            bases=("quiz.question",),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="multichoice.MCQuestion",
                verbose_name="Question",
            ),
        ),
    ]
