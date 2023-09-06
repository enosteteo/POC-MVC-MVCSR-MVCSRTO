from mvc.main import bp


@bp.route('/')
def index():
    return 'This is the main blueprint'
