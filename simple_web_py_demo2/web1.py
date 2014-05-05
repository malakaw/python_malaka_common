import action.json as json
import web
from action.Pager import Pager
from web import form
import action.solr_client as sclient
urls = (
    '/', 'index',
    '/query',"Query",
    '/bquery',"BQuery",
    '/bquery/page/(\d+)','BQuery',
    '/pquery','PQuery',
    '/pquery/page/(\d+)','PQuery',
    '/ft','Ft'
)

app = web.application(urls, globals())




render = web.template.render('templates/')




class index:
    def GET(self):
        i = web.input()
        if hasattr(i, 't'):
            return render.index(i.t)
        else:
            return render.index("null")



checkList_wh    = []
checkList_catid = []
checkList_level = []
price_range     = ['0','9999999']
agio_range      = ['0','10']


class PQuery:
    def GET(self,page=1,price_range=['0','9999999']):
        print web.input()
        page = int(page)
        print "p %s" %page

        checkList_wh    =  web.input(cwh=[])
        checkList_catid =  web.input(ccat=[])
        checkList_level =  web.input(plev=[])

        print checkList_wh['cwh']
        print checkList_level['plev']

        params = web.input()
        if hasattr(params,'p_min') and hasattr(params,'p_max'):
            price_range = [ sclient.getPrice(web.input('p_min')['p_min'] ,False) , sclient.getPrice(web.input('p_max')['p_max'] ,True)]

        if hasattr(params ,'page'):
            page = web.input('page')['page']
        print "p_r %s" % price_range



        page = int(page)
        if page == 1 :
            pagestart = 0
        else:
            pagestart = 20 * (page-1)

        result = sclient.qProduct(pagestart,20,web.input(cwh=[]),web.input(ccat=[]) ,price_range,checkList_level)
        mypdiv =  Pager("%s",total_count=result.numFound,page_size=20,cur_page=page).getPage()
        print mypdiv

        countp = result.numFound
        return render.pquery(result,set(checkList_wh['cwh']),set(checkList_catid['ccat']),set(checkList_level['plev']),price_range,mypdiv,countp)

class BQuery:
    def GET(self,page=1,price_range=['0','9999999'],agio_range=['0','10']):
        print web.input()

        page = int(page)
        print "page %s" % page
        checkList_wh    =  web.input(cwh=[])
        checkList_catid =  web.input(ccat=[])
        checkList_level =  web.input(plev=[])

        print checkList_wh['cwh']

        params = web.input()
        if hasattr(params,'p_min') and hasattr(params,'p_max'):
            price_range = [ sclient.getPrice(web.input('p_min')['p_min'] ,False) , sclient.getPrice(web.input('p_max')['p_max'] ,True)]
        if hasattr(params ,'agio_min') and hasattr(params,'agio_max'):
            agio_range = [sclient.getAgio(web.input('agio_min')['agio_min'],False),sclient.getAgio(web.input('agio_max')['agio_max'],True)]



        if hasattr(params ,'page'):
            page = web.input('page')['page']

        page = int(page)
        if page == 1 :
            pagestart = 0
        else:
            pagestart = 20 * (page-1)

        print "start:%s" % pagestart
        result = sclient.qBrand(pagestart,20,web.input(cwh=[]),web.input(ccat=[]) ,price_range,agio_range,checkList_level)

        print "sum:%s" % result.numFound
        mypdiv =  Pager("%s",total_count=result.numFound,page_size=20,cur_page=page).getPage()
        print mypdiv



        return render.bquery(result,set(checkList_wh['cwh']),set(checkList_catid['ccat']),set(checkList_level['plev']),price_range,agio_range,mypdiv)







if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
