// JavaScript that fetches and prints how to say “Hello” depending on the language
'use strict';
$(() => {
  const fetchTranslation = () => {
    const APIURL = 'https://fourtonfish.com';
    const languageCode = $('INPUT#language_code').val();
    $.get(`${APIURL}/hellosalut/?lang=${languageCode}`, (langdata, status) => {
      $('DIV#hello').html(langdata.hello);
    });
  };

  $('INPUT#btn_translate').click(fetchTranslation);
  $('INPUT#language_code').keydown((keyboardEvent) => {
    if (keyboardEvent.key === 'Enter') fetchTranslation();
  });
});
