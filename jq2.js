$("#example").dataTable({
    "aaData":[
	["Sitepoint", "http://sitepoint.com","Blog","2013-10-15 10:30:00"],
	["Flippa",    "http://flippa.com","Marketplace","null"],
	["99designs", "http://99designs.com","Marketplace","null"],
	["Learnable", "http://learnable.com","Online courses","null"],
	["Rubysource","http://rubysource.com","Blog","2013-01-10 12:00:00"] ],

    "aoColumnDefs":[
	{ "sTitle":"Site name" ,	 // optional
	  "bSortable": true, 
	  "aTargets": [ "site_name" ] } // target can be the header name or the class

	// make the URL clickable

	,{ "sTitle":"URL",
	   "aTargets": [ 1 ] ,
	   "bSortable": false,	// disable sorting; default is sortable
	   "mRender": function ( url, type, full )  { return  '<a href="'+url+'">' + url + '</a>'; } }

	,{ "aTargets":[ 3 ] ,
	   "sType": "date" ,	// javascript type
	   "mRender": function(date, type, full) { return date=='null' ? "n/a" : date } }

    ]
});
