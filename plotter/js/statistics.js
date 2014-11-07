$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['shutter', 'storage', 'general', 'vedio', 'service', 'picture', 'price', 'size', 'lens', 'focus', 'design', 'battery'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[0, 17, 34, 15, 17, 109, 57, 25, 35, 4, 32, 164]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(232,78,64,0.5)",
strokeColor: "rgba(232,78,64,0.8)",
highlightFill: "rgba(232,78,64,0.75)",
highlightStroke: "rgba(232,78,64,1)",
data:
[4.0, 0, 0, 1.0, 1, 12, 3, 0, 9, 0, 20.0, 52.0]}
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
