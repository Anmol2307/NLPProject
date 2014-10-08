$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['design', 'price', 'storage', 'picture', 'service', 'media', 'lens', 'sound', 'size', 'battery'],
datasets: [{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[2.333333333333333, 6.341975308641975, 5.0, 175.60855255855256, -5.0, -2.0, 3.083333333333333, 12.559523809523808, 50.36094246310965, 30.68758888170653]}]};
var myLineChart = new Chart(ctx).Bar(data,{});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var data = [
{
value: 50.0,
color: "#46BFBD",
highlight: "#5AD3D1",
label: "Done"
},
{
value: 50.0,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{});
});
