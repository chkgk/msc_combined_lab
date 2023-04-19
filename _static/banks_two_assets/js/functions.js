document.getElementById('asset_a').onkeyup = function() {
    findTotal();
    if($.trim($(this).val()) === "") {
        $(this).val("0");
    }
};

document.getElementById('asset_b').onkeyup = function() {
    findTotal();
    if($.trim($(this).val()) === "") {
        $(this).val("0");
    }
};


// set field values to two decimal places
function setTwoNumberDecimal(e) {
    e.value = parseFloat(e.value).toFixed(0);
}


// determine sum of invested money
function findTotal(){
    var button = document.getElementById('btn-next');
    var arr = document.getElementsByClassName('inv');
    var tot = 0;
    for(var i = 0; i < arr.length; i++){
        if(parseFloat(arr[i].value))
            tot += parseFloat(arr[i].value);
    }
    document.getElementById('total').value = tot.toFixed(0);
    document.getElementById('total').setAttributeNS('null', 'data-value', tot);

    // change color of sum-field to green if sum is correct, red otherwise
    // hide "next"-button if sum is incorrect, show otherwise
    if (tot === 100) {
        document.getElementById('total').classList.add('correct');
        document.getElementById('total').classList.remove('incorrect');
        button.style.visibility = 'visible';
    } else {
        document.getElementById('total').classList.add('incorrect');
        document.getElementById('total').classList.remove('correct');
        button.style.visibility = 'hidden';
    }
}


// disable enter key
function no_enter() {
    return !(window.event && window.event.keyCode === 13);
}
