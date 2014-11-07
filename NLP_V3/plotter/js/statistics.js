$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['size', 'lens', 'price', 'battery', 'general', 'picture', 'video'],
datasets: [{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[8.655154173312068, 2.991666666666667, 4.230769230769231, 5.2582545956459, 2.0625, 14.153229672997117, 2.35]}]};
var myLineChart = new Chart(ctx).Bar(data,{});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var data = [
{
value: 6.666666666666671,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 93.33333333333333,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{});
});
