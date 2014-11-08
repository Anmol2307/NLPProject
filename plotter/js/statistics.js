$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['battery'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[1]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(232,78,64,0.5)",
strokeColor: "rgba(232,78,64,0.8)",
highlightFill: "rgba(232,78,64,0.75)",
highlightStroke: "rgba(232,78,64,1)",
data:
[0]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
$(function(){
$("#perChart").hide()
});
$(function(){
$("#sentiPerChart").hide()
});
$(function(){
$("#negChart").hide()
});
