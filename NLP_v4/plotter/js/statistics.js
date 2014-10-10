$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['battery', 'size', 'camera', 'lens', 'picture'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[3, 3, 5, 1, 15]}
]};
var myLineChart = new Chart(ctx).Bar(data,{});
});
$(function(){
var ctx = document.getElementById("negChart").getContext("2d");
var data = {labels:
['battery', 'size', 'camera', 'lens', 'picture'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(232,78,64,0.5)",
strokeColor: "rgba(232,78,64,0.8)",
highlightFill: "rgba(232,78,64,0.75)",
highlightStroke: "rgba(232,78,64,1)",
data:
[2, 0, 0, 1, 0]}
]};
var myLineChart = new Chart(ctx).Bar(data,{});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var data = [
{
value: 30.0,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 70.0,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{});
});
$(function(){
var ctx = document.getElementById("sentiPerChart").getContext("2d");
var data = [
{
value: 10.0,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 90.0,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{});
});
