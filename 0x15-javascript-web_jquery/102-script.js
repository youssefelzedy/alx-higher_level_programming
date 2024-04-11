$('document').ready(function () {
    $('INPUT#btn_translate').click(function () {
      const parm = { lang: $('INPUT#language_code').val() };
      console.log(parm);
      $.get('https://hellosalut.stefanbohacek.dev/', parm, function (data) {
        $('DIV#hello').text(data.hello);
      });
    });
  });