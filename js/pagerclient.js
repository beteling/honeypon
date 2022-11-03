function Pagerclient(tableName, itemsPerPage) {
    this.tableName = tableName;
    this.itemsPerPage = itemsPerPage;
    this.currentPage = 1;
    this.pages = 0;
    this.inited = false;

    this.showRecords = function(from, to) {
        var rows = document.getElementById(tableName).rows;
        // i starts from 1 to skip table header row
        for (var i = 1; i < rows.length; i++) {
            if (i < from || i > to)
                rows[i].style.display = 'none';
            else
                rows[i].style.display = '';
        }
    }

    this.showPage = function(pageNumber) {
    	if (! this.inited) {
    		alert("not inited");
    		return;
    	}

        var oldPageAnchor = document.getElementById('pgc'+this.currentPage);
        oldPageAnchor.className = 'pgc-normalclient';

        this.currentPage = pageNumber;
        var newPageAnchor = document.getElementById('pgc'+this.currentPage);
        newPageAnchor.className = 'pgc-selectedclient';

        var from = (pageNumber - 1) * itemsPerPage + 1;
        var to = from + itemsPerPage - 1;
        this.showRecords(from, to);
    }

    this.prev = function() {
        if (this.currentPage > 1)
            this.showPage(this.currentPage - 1);
    }

    this.next = function() {
        if (this.currentPage < this.pages) {
            this.showPage(this.currentPage + 1);
        }
    }

    this.init = function() {
        var rows = document.getElementById(tableName).rows;
        var records = (rows.length - 1);
        this.pages = Math.ceil(records / itemsPerPage);
        this.inited = true;
    }

    this.showPageNav = function(pagerName, positionId) {
    	if (! this.inited) {
    		alert("not inited");
    		return;
    	}
    	var element = document.getElementById(positionId);

    	var pagerHtml = '<span onclick="' + pagerName + '.prev();" class="pgc-normalclient"> &#171</span>';
        for (var page = 1; page <= this.pages; page++){
	    if (page>5){
                pagerHtml += '<span hidden id="pgc' + page + '" class="pgc-normalclient" onclick="' + pagerName + '.showPage(' + page + ');">' + page + '</span>';}

       	    else{
	        pagerHtml += '<span id="pgc' + page + '" class="pgc-normalclient" onclick="' + pagerName + '.showPage(' + page + ');">' + page + '</span>';}}

	 pagerHtml += '<span onclick="'+pagerName+'.next();" class="pgc-normalclient">&#187;</span>';

        element.innerHTML = pagerHtml;
    }
}
