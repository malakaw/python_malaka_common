#coding=utf-8
import solr
#http://10.19.21.64:9030/s171.25/8983/solr/product_brand/select?q=*:*
#http://10.19.21.64:9030/s171.25/8983/solr/product_brand/select?q=sl_type:b&fl=sl_content&wt=json&fq=sl_hasstock:true AND sl_pbrand_level:B AND sl_sell_to:[NOW TO *]
#
#http://192.168.44.68:8983/8983/solr//product_brand/select?q=sl_type:b&fl=sl_content&wt=json&fq=sl_hasstock:true AND  sl_sell_to:[NOW TO *]
#http://192.168.44.68:8983/solr/product_brand/select?q=sl_type%3Ab&wt=json&indent=true
#
#

solrserver68 = solr.SolrConnection('http://10.19.21.64:9030/s171.25/8983/solr/product_brand')
#solrserver68 = solr.SolrConnection('http://192.168.44.68:8983/solr/product_brand')
def querysolr():
    s = solr.SolrConnection('http://192.168.44.68:8983/solr')
    result = s.query("*:*", rows=5)
    for r in result:
        print r['id']
    return result



def qBrand(bpstart,bprows,wh,cat,price_r,agio_range,plevel):
    q_str = ''
    if len(wh['cwh']):
        for wh in wh['cwh']:
            if len(q_str) > 0:
                q_str += " AND  sl_to_warehouse:%s " % wh
            else:
                q_str += "sl_to_warehouse:%s " % wh

#    if len(wh['cwh']):
#        q_str  =  "sl_to_warehouse:%s" % (",".join(wh['cwh']))
    if len(cat['ccat']):
        for catid in cat['ccat']:
            if len(q_str)>0:
                q_str += " AND sl_catid:%s" % catid
            else:
                q_str += "sl_catid:%s" % catid


    if len(plevel['plev']):
        if len(q_str)>0:
            q_str  += " AND (sl_pbrand_level:"
        else:
            q_str  += "(sl_pbrand_level:"
        q_str  += " OR sl_pbrand_level:".join(plevel['plev'])
        q_str += ")"



    if len(q_str):
        q_str += " AND sl_range_pct:[%s TO %s]" % (getPrice(price_r[0],False),getPrice(price_r[1],True))
    else:
        q_str += "sl_range_pct:[%s TO %s]" % (getPrice(price_r[0],False),getPrice(price_r[1],True))


    if len(q_str):
        q_str  += " AND  (sl_range_agio_min:[%s TO %s] AND sl_range_agio_max:[%s TO %s]) " % (agio_range[0],agio_range[1],agio_range[0],agio_range[1] )
    else:
        q_str  +=  "  (sl_range_agio_min:[%s TO %s] AND sl_range_agio_max:[%s TO %s]) " % (agio_range[0],agio_range[1],agio_range[0],agio_range[1] )
    print q_str

    print "start %s rows %s" % (bpstart,bprows)
    result =  solrserver68.query("sl_type:b",fq=q_str,start=bpstart,rows=bprows,sort="sl_sequcence desc")

    return result


#http://10.19.21.64:9030/s171.25/8983/solr/product_brand/select?q=sl_type:p&fq=sl_sell_to:[NOW%20TO%20*]%20AND%20sl_hasstock:true&sort=sl_sequcence%20desc
#http://10.19.21.64:9030/s171.25/8983/solr/product_brand/select?q=sl_type:p&fq=sl_to_warehouse:VIP_SH
#
#
#sl_hasstock:true   AND sl_sell_to:[NOW TO *]&wt=json&sort=sl_itsr
def qProduct(bpstart,bprows,wh,cat,price_r,plevel):
    q_str = ''
    if len(wh['cwh']):
        for wh in wh['cwh']:
            if len(q_str) > 0:
                q_str += " AND  sl_to_warehouse:%s " % wh
            else:
                q_str += "sl_to_warehouse:%s " % wh

#    if len(wh['cwh']):
#        q_str  =  "sl_to_warehouse:%s" % (",".join(wh['cwh']))
    if len(cat['ccat']):
        for catid in cat['ccat']:
            if len(q_str)>0:
                q_str += " AND sl_catid:%s" % catid
            else:
                q_str += "sl_catid:%s" % catid


    if len(plevel['plev']):
        if len(q_str)>0:
            q_str  += " AND (sl_pbrand_level:"
        else:
            q_str  += "(sl_pbrand_level:"
        q_str  += " OR sl_pbrand_level:".join(plevel['plev'])
        q_str += ")"



#    if len(cat['ccat']):
#        q_str  +=  " AND sl_catid:%s" % (" ".join(cat['ccat']))


    if len(q_str):
        q_str += " AND sl_range_price:[%s TO %s]" % (getPrice(price_r[0],False),getPrice(price_r[1],True))
    else:
        q_str += "sl_range_price:[%s TO %s]" % (getPrice(price_r[0],False),getPrice(price_r[1],True))

    q_str += " AND  sl_hasstock:true   AND sl_sell_to:[NOW TO *]"

    print q_str
    result =  solrserver68.query("sl_type:p",fq=q_str,rows=bprows,start=bpstart ,sort="sl_sequcence desc")
    print result.numFound
    return result



import sys
def getPrice(p ,ismax):
    if ismax:
        if len(p):
            return p
        else:
            return sys.maxint
    else:
        if len(p):
            return p
        else:
            return "0"

def getAgio(a ,ismax):
    if ismax:
        if len(a):
            return a
        else:
            return 10
    else:
        if len(a):
            return a
        else:
            return "0"
