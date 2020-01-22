
$(document).ready(function(){
    $('.formset_add').on('click', function(){
        $('#formset').clone().appendTo($("#supp_form"))
    })
});

 $('#formset').on('formAdded', function(event) {
    newForm = event.target;
//     //Do Stuff
//     console.log("Ok c'est cool mon event est déclenché")
// });

<script>jQuery(function($) {
        $("#formset").formset({
            animateForms: true
        });
	});</script>