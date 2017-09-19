/**
 * Created by tormod on 01.04.17.
 */

$(document).ready(function(){
    $(".messages li")
        .each(function(){
            var $el = $(this);
            $el.toggleClass('active');
            setTimeout(function(){
                $el.toggleClass('active');
            }, 3000);
        });
});
