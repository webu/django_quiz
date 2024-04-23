# Generated by Django 2.2.24 on 2022-01-06 10:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import re


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category", old_name="category", new_name="_category"
        ),
        migrations.RenameField(
            model_name="question", old_name="content", new_name="_content"
        ),
        migrations.RenameField(
            model_name="question", old_name="explanation", new_name="_explanation"
        ),
        migrations.RenameField(
            model_name="quiz", old_name="description", new_name="_description"
        ),
        migrations.RenameField(
            model_name="quiz", old_name="fail_text", new_name="_fail_text"
        ),
        migrations.RenameField(
            model_name="quiz", old_name="success_text", new_name="_success_text"
        ),
        migrations.RenameField(model_name="quiz", old_name="title", new_name="_title"),
        migrations.RenameField(model_name="quiz", old_name="url", new_name="_url"),
        migrations.RenameField(
            model_name="subcategory", old_name="sub_category", new_name="_sub_category"
        ),
        migrations.AddField(
            model_name="question",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_quiz.question_set+",
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="progress",
            name="score",
            field=models.CharField(
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z"),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
                verbose_name="Score",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="draft",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.",
                verbose_name="Draft",
            ),
        ),
        migrations.AlterField(
            model_name="sitting",
            name="incorrect_questions",
            field=models.CharField(
                blank=True,
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z"),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
                verbose_name="Incorrect questions",
            ),
        ),
        migrations.AlterField(
            model_name="sitting",
            name="question_list",
            field=models.CharField(
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z"),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
                verbose_name="Question List",
            ),
        ),
        migrations.AlterField(
            model_name="sitting",
            name="question_order",
            field=models.CharField(
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z"),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
                verbose_name="Question Order",
            ),
        ),
        migrations.CreateModel(
            name="SubCategoryTranslation",
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
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
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
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="quiz.SubCategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sub-Category Translation",
                "db_table": "quiz_subcategory_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="QuizTranslation",
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
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                ("title", models.CharField(max_length=60, verbose_name="Title")),
                (
                    "url",
                    models.SlugField(
                        help_text="a user friendly url",
                        max_length=60,
                        verbose_name="user friendly url",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="a description of the quiz",
                        verbose_name="Description",
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
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="quiz.Quiz",
                    ),
                ),
            ],
            options={
                "verbose_name": "Quiz Translation",
                "db_table": "quiz_quiz_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="QuestionTranslation",
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
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
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
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="base_translations",
                        to="quiz.Question",
                    ),
                ),
            ],
            options={
                "verbose_name": "Question Translation",
                "db_table": "quiz_question_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="CategoryTranslation",
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
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
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
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="quiz.Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category Translation",
                "db_table": "quiz_category_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
