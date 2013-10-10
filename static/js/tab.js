$(function(){
/*最初のタブの背景色*/

$("#Top").css("backgroundColor","#dcdcdc");
$("#Portfolio").css("backgroundColor","#666");
$("#Artifact").css("backgroundColor","#666"); 
$("#Goal").css("backgroundColor","#666");

/*タブの移動*/
  $("#move_tab").css("float", "right");

/*タブの文字の色*/
$("#topcolor").css("color", "#666");
$("#portcolor").css("color", "#fff");
$("#artcolor").css("color", "#fff");
$("#goalcolor").css("color", "#fff");

/*mouseover*/
  /*ポートフォリオ*/
  $("li#Portfolio").mouseover(function(){
    $("#Portfolio").css("backgroundColor","#dcdcdc");
    $("#portcolor").css("color", "#666");
  });
  $("li#Portfolio").mouseout(function(){
    $("#Portfolio").css("backgroundColor","#666");
    $("#portcolor").css("color", "#fff");
  });

  /*成果物管理*/
  $("li#Artifact").mouseover(function(){
    $("#Artifact").css("backgroundColor","#dcdcdc");
    $("#artcolor").css("color", "#666");
  });
  $("li#Artifact").mouseout(function(){
    $("#Artifact").css("backgroundColor","#666");
    $("#artcolor").css("color", "#fff");
  });

  /*ゴール*/
  $("li#Goal").mouseover(function(){
    $("#Goal").css("backgroundColor","#dcdcdc");
    $("#goalcolor").css("color", "#666");
  });
  $("li#Goal").mouseout(function(){
    $("#Goal").css("backgroundColor","#666");
    $("#goalcolor").css("color", "#fff");
  });

  /*border- riadius*/
  $("#Top").css("border-radius","5px 5px 0px 0px");
  $("#Portfolio").css("border-radius","5px 5px 0px 0px");
  $("#Artifact").css("border-radius","5px 5px 0px 0px");
  $("#Goal").css("border-radius","5px 5px 0px 0px");
 
  /*padding*/
  $("#Top").css("padding","5px");
  $("#Portfolio").css("padding","5px");
  $("#Artifact").css("padding","5px");
  $("#Goal").css("padding","5px");
});