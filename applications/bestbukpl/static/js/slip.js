document.addEventListener("DOMContentLoaded", function(event) { 
    var stack = parseFloat(local_storage.get('stawka'));
    if(stack && stack > 0)
        $('#coupon-stack').val(stack);
    
    var tmp = local_storage.get('kupon');
    if(tmp){
        var coupon = jQuery.parseJSON(tmp);
        create_coupon(coupon, null);
    }
    
    if(local_storage.get('coupon_minimalize')==1){
        coupon_minimalize(1);
    }
});

function coupon_add(obj){
    local_storage.set('coupon_stake', '');
    local_storage.set('coupon', '');
}

function coupon_add(obj){
    obj = $(obj);
    local_storage.set('coupon',obj.attr('odd'));
    
}
