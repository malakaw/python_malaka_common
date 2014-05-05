import web

urls = (
    '/', 'index',
    '/query',"Query"
)

render = web.template.render('templates/')

class index:
    def GET(self):
        i = web.input()
        if hasattr(i, 't'):
            return render.index(i.t)
        else:
            return render.index("null")


class Query:
    def GET(self):
        return ""

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
