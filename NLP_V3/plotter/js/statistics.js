$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['picture', 'focus', 'size', 'lens'],
datasets: [{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[14.37882154882155, 2.0, 5.75, 1.9222222222222223]}]};
var myLineChart = new Chart(ctx).Bar(data,{});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var data = [
{
value: 43.75,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 56.25,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{});
});
