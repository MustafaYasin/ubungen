name_to_xpath_mapper = {
    'muscle_group': '//h1[@itemprop = "name"]/text()',
    'subset_muscles': '//span[@id = "titleYear"]/a/text()',
    'exercise_title': '//span[@itemprop="ratingValue"]/text()',
    'muscle_description_title': '//span[@itemprop="ratingCount"]/text()',
    'muscle_description': '//span[@itemprop="director"]/a/span/text()',
    'exercise_execution_title': '//span[@itemprop="actors"]/a/span/text()',

}

export_order = ["muscle_group", "subset_muscles", "exercise_title", "muscle_description_title", "muscle_description", "exercise_execution_title"]
