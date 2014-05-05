function myEval(str) {
//    alert("in");
//    var obj = eval(str);
    var obj = eval('(' + str + ')');
    return obj['cat_id'];
//    return obj.toJSONString();
}


function getURL(str) {
    var obj = eval('(' + str + ')');
    //alert( "<a href="+obj['url'] + " target='_blank'>"+"<img src="+obj['img']+" />" + "</a>");
    return "<a href="+obj['url'] + " target='_blank'>"+"<img src="+obj['img']+" />" + "</a>";
}


function getName(str)
{
    var obj = eval('(' + str + ')');
    return obj['name'];
}

function getBrand(str)
{
    var obj = eval('(' + str + ')');
//    return obj['brand'];
    var tempstr = "";
    for(var i=0;i<obj['brand'].length;i++)
    {
        tempstr += obj['brand'][i]['name'] + " "+ obj['brand'][i]['level'];
    }
    return tempstr;
}

function getSellDate(str)
{
    var obj = eval('(' + str + ')');
    return  obj['sell_time_from'] +"-" +obj['sell_time_to'];
}

function getStock(str)
{
    var obj = eval('(' + str + ')');
    return  obj['stock'];
}

function getp_agio(str)
{
    var obj = eval('(' + str + ')');
    return  obj['agio'];
}
function getforeword(str)
{
    var obj = eval('(' + str + ')');
    return  obj['foreword'];
}


var hashMap = {
    Set : function(key,value){this[key] = value},
    Get : function(key){return this[key]},
    Contains : function(key){return this.Get(key) == null?false:true},
    Remove : function(key){delete this[key]}
}

hashMap.Set("102","男装");
hashMap.Set("109","家具百货");
hashMap.Set("106","箱包");
hashMap.Set("110","文体用品");
hashMap.Set("101","女装");
hashMap.Set("105","化妆品");
hashMap.Set("104","鞋类");
hashMap.Set("111","汽车配件");
hashMap.Set("103","童装");
hashMap.Set("107","配饰");
hashMap.Set("108","3c产品");
hashMap.Set("999","其他");

function getcatname(str)
{
   var words = new Array();
   words = str.split(" ");
   var strcc = "";
   for(var i=0;i<words.length;i++)
   {
       if(words[i].length >0)
           strcc += hashMap.Get(words[i]) + " ";
   }
   return  strcc;
}

var levelMap = {
    Set : function(key,value){this[key] = value},
    Get : function(key){return this[key]},
    Contains : function(key){return this.Get(key) == null?false:true},
    Remove : function(key){delete this[key]}
}


levelMap.Set("100","AD");
levelMap.Set("200","AA");
levelMap.Set("300","A+");
levelMap.Set("400","A");
levelMap.Set("500","A-");
levelMap.Set("600","B+");
levelMap.Set("700","B");
levelMap.Set("800","B-");
levelMap.Set("900","C+");
levelMap.Set("910","C");
levelMap.Set("920","C-");

function getlevelName(str)
{
   return  levelMap.Get(str);
}
