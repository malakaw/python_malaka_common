class Pager:
  def __init__(self,url,total_count,page_size=20,cur_page=1):
      self.url=url
      self.total_count=total_count
      self.page_size=page_size
      self.cur_page=cur_page
      self.page_count,tail=divmod(self.total_count,self.page_size)
      if tail is not 0:self.page_count+=1
      self.pages=[]

  def getPage(self):
      if self.cur_page>1:
          self.pages.append('<li><a href="#" onclick="javascript:fsubmit(%s)">上一页</a></li>' %(self.url %(self.cur_page-1)))
          self.pages.append('<li><a  href="#" onclick="javascript:fsubmit(%s)">首页</a></li>' %(self.url %1))
      if self.cur_page<=5:limit_s=1
      else:limit_s=self.cur_page-4
      if self.page_count>=self.cur_page+5:limit_e=self.cur_page+5
      else:
          limit_e=self.page_count
          if self.cur_page>=10:limit_s=self.cur_page-9
      for i in xrange(limit_s,limit_e+1):
          if self.cur_page==i:
              self.pages.append('<li class="disabled"><a href="#">%s</a></li>'%self.cur_page)
          else:
              self.pages.append('<li ><a  href="#" onclick="javascript:fsubmit(%s)">%s</a></li>' %(self.url%i,i))
      if self.cur_page<self.page_count:
          self.pages.append('<li ><a  href="#" onclick="javascript:fsubmit(%s)">下一页</a></li>' %(self.url%(self.cur_page+1)))
          self.pages.append('<li><a  href="#" onclick="javascript:fsubmit(%s)">尾页</a></li>'%(self.url %self.page_count))
      return "".join(self.pages)
