# vim: fileencoding=utf-8

def upload_template(filename, destination, context, mode=None):
    """
    Create file from string.Template and upload it.
    """
    with open(filename) as f:
        tpl = Template(f.read())
    put(local_path=StringIO(tpl.substitute(context)),
            remote_path=destination,
            mode=mode)
