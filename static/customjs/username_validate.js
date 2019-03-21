
$("#id_username").change(function () {
  var username = $(this).val();

  $.ajax({
    url: '/ajax/validate_username/',
    data: {
      'username': username
    },
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        $("#id_username").css("background-color","tomato");
      }else{
        $("#id_username").css("background-color","white");
      }
    }
  });

});
