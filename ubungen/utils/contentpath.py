name_to_xpath_mapper = {
    'muscle_group': '//h1[@itemprop = "name"]/text()',
    'muscle_description': '//span[@id = "titleYear"]/a/text()',
    'muscle_title': '//span[@itemprop="ratingValue"]/text()',
    'subset_muscles': '//span[@itemprop="ratingCount"]/text()',
    'list_of_exercises': '//span[@itemprop="director"]/a/span/text()',
    'list_of_sub_exercises': '//span[@itemprop="actors"]/a/span/text()',
    'exercise_title': '//div[@itemprop="description"]/p/text()',
    'muscle_image': '//h4[text() = "Taglines:"]/following-sibling::text()',
    'equipment': '//div[@itemprop="genre"]/a/text()',
    'exercise_level': '//h4[text() = "Country:"]/following::a/text()',
    'target_muscles': '//h4[text() = "Language:"]/following-sibling::a/text()',
    'supporting_muscles': '//h4[text() = "Filming Locations:"]/following-sibling::a/text()',
    'synonym_titles': '//h4[text() = "Budget:"]/following-sibling::text()',
    'exercise_execution': '//h4[text() = "Gross:"]/following-sibling::text()',
    'video_links': '//h4[text() = "Color:"]/following-sibling::a/text()',

}

export_order = ["muscle_group", "muscle_description", "muscle_title", "subset_muscles", "list_of_exercises", "muscle_image", "equipment",
                "exercise_level", "target_muscles", "supporting_muscles", "synonym_titles", "exercise_execution", "video_links"]
