import falcon


class InstaHack:

    def __init__(self):
        pass

    def on_get(self, req, resp):
        url = req.get_param('url')

        agent = req.get_header('User-Agent')

        if "instagram" in agent.lower():
            resp.status = falcon.HTTP_OK
            resp.data = bytes("i know you dont want me to be happy".encode('utf-8'))
            resp.content_type = 'application/pdf'
            resp.downloadable_as = 'scary_file'
            resp.accept_ranges = 'bytes'
            resp.set_header('Content-Transfer-Encoding', 'binary')
            return

        raise falcon.HTTPMovedPermanently(url)
