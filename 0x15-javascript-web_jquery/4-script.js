let tmp = 0;

$('DIV#toggle_header').click(function () {
    if (tmp === 0) {
        tmp = 1;
        $('header').removeClass('green');
        $('header').addClass('red');
    }
    else {
        tmp = 0;
        $('header').removeClass('red');
        $('header').addClass('green');
    }
});


$('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });