{
    'name': 'Bistro Theme',
    'description': 'Bistro Theme - Restaurant, Food/Drink, Catering, Food trucks',
    'category': 'Theme/Food',
    'summary': 'Bistro, Restaurant, Bar, Pub, Cafe, Food, Catering',
    'sequence': 220,
    'version': '2.0.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/layout.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_columns.xml',
        'views/snippets/s_cards_grid.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_card_offset.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_image_punchy.xml',
        'views/snippets/s_image_title.xml',
        'views/snippets/s_sidegrid.xml',
        'views/snippets/s_images_mosaic.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_features_wall.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_quotes_carousel_minimal.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_accordion_image.xml',
        'views/snippets/s_key_benefits.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_carousel_intro.xml',
        'views/snippets/s_image_hexagonal.xml',
        'views/snippets/s_striped_center_top.xml',
        'views/snippets/s_motto.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_striped_top.xml',
        'views/snippets/s_quadrant.xml',
        'views/snippets/s_intro_pill.xml',
        'views/snippets/s_big_number.xml',
        'views/snippets/s_image_frame.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_shape_image.xml',
        'views/snippets/s_images_constellation.xml',
        'views/snippets/s_text_cover.xml',
        'views/snippets/s_empowerment.xml',
        'views/new_page_template.xml',

    ],
    'images': [
        'static/description/bistro_cover.jpg',
        'static/description/bistro_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_bistro/static/src/img/backgrounds/17.jpg',
        'website.s_media_list_default_image_1': '/theme_bistro/static/src/img/content/media_list_01.jpg',
        'website.s_image_text_default_image': '/theme_bistro/static/src/img/content/image_text.jpg',
        'website.s_media_list_default_image_2': '/theme_bistro/static/src/img/content/media_list_02.jpg',
        'website.s_text_image_default_image': '/theme_bistro/static/src/img/content/text_image.jpg',
        'website.s_quotes_carousel_demo_image_1': '/theme_bistro/static/src/img/backgrounds/s_quotes_carousel_background.jpg',
        'website.library_image_10': '/theme_bistro/static/src/img/backgrounds/07.jpg',
        'website.library_image_05': '/theme_bistro/static/src/img/backgrounds/11.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_image_title', 's_key_images', 's_pricelist_cafe', 's_quotes_carousel', 's_quadrant'],
        'pricing': ["s_text_image", "s_product_catalog"],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bistro.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_bistro/static/src/js/tour.js',
        ],
    }
}
