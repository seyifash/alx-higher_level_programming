$('#toggle_header').click(function () {
  const headChange = $('header');
  if (headChange.hasClass('red')) {
    headChange.removeClass('red');
    headChange.addClass('green');
  } else if (headChange.hasClass('green')) {
    headChange.removeClass('green');
    headChange.addClass('red');
  }
});
