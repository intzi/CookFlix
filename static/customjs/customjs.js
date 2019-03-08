$(document).ready(function(){
  $("[type=file]").on("change", function(){
    // Name of file and placeholder
    var file = this.files[0].name;
    var dflt = $(this).attr("name");
    var prefix = "Selected thumbnail: ";
    if(dflt == "video_file"){
          prefix = "Selected video: ";
    }
    if($(this).val()!=""){
      $(this).next().text(prefix+file);
    } else {
      $(this).next().text(dflt);
    }
  });
});
