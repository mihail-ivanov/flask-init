
from flask_assets import Bundle


ASSET_DIRS = [
    'static',
    'static/css',

    'vendor',
    'vendor/foundation-sites',
    'vendor/foundation-sites/dist/js',
]


ASSETS = {
    # jQuery
    'jquery': Bundle(
        'jquery-3.2.0.min.js',
        filters='jsmin',
        output='js/jquery.min.js'
    ),

    # Foundation
    'foundation_css': Bundle(
        'foundation_settings.scss', 'assets/foundation.scss',
        filters='libsass',
        output='css/foundation.css',
        depends='**/*.scss'
    ),
    'foundation_js': Bundle(
        'foundation.min.js',
        filters='jsmin',
        output='js/foundation.min.js'
    ),
}
