


$(document).ready(function() {
  // $('#example').DataTable();
  console.log("ddv_sample.js pierwsza czesc");

    var dt_table = $('#example').dataTable({
        "oLanguage": oLanguages,
        "bFilter": true,
        "aLengthMenu": [[25, 50, 100, 200], [25, 50, 100, 200]],
        "iDisplayLength" : 25,
        "aaSorting": [[ 0, "desc" ]],
        "bAutoWidth": true,
        "aoColumns": [
                        { "sType": "locale-compare", "targets": 0 },
                        // { "bSortable": true, "bSearchable": true},
                        // { "bSortable": true, "bSearchable": true},
                        // { "bSortable": true, "bSearchable": true},
                        // { "bSortable": true, "bSearchable": true},
                        ],
        "bProcessing": true,
        "bServerSide": true,
        "bStateSave": true,
        "sAjaxSource": USERS_LIST_JSON_URL
    });
});
