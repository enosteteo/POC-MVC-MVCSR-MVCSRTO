from mvc_service_repository_transferobject.main import bp


@bp.route('/')
def index():
    return 'This is the main blueprint'
