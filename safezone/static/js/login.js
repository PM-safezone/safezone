$.ajaxSetup({
    headers: {"X-CSRFToken": '{{csrf_token}}'}
});

$(document).ready(function(){
    $('.ml-select option').each(function(index, option){
        $(option).addClass('option-class-' + index);
    });
});