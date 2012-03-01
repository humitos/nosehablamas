$(document).ready(function(){
    $('div[id^="more-"]').click(function(event){
	var news_id = $(this).attr('id').replace('more-', '');
	var article_divs = 'div[name="article-news-' + news_id + '"]';
	$(article_divs).show();
	$(this).hide()
	return false;
    });
});
