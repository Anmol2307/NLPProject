$(function(){
var nodes_1 = [
{id: 1, label: "picture"},
{id: 2, label: "good"},
{id: 3, label: "lengthy"},
{id: 4, label: "easy"},
];
var edges_1 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
];
var container_1 = document.getElementById("container_1");
var data_1= {
nodes: nodes_1,
edges: edges_1
};
var options_1 = {
width: "600px",
height: "600px"
};
var network_1 = new vis.Network(container_1, data_1, options_1);
});
$(function(){
var nodes_2 = [
{id: 1, label: "battery"},
{id: 2, label: "not"},
{id: 3, label: "adequate"},
{id: 4, label: "fairly"},
{id: 5, label: "right"},
];
var edges_2 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
];
var container_2 = document.getElementById("container_2");
var data_2= {
nodes: nodes_2,
edges: edges_2
};
var options_2 = {
width: "600px",
height: "600px"
};
var network_2 = new vis.Network(container_2, data_2, options_2);
});
$(function(){
var nodes_3 = [
{id: 1, label: "camera"},
{id: 2, label: "nt"},
{id: 3, label: "compact"},
{id: 4, label: "easy"},
];
var edges_3 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
];
var container_3 = document.getElementById("container_3");
var data_3= {
nodes: nodes_3,
edges: edges_3
};
var options_3 = {
width: "600px",
height: "600px"
};
var network_3 = new vis.Network(container_3, data_3, options_3);
});
$(function(){
var nodes_4 = [
{id: 1, label: "size"},
{id: 2, label: "perfect"},
];
var edges_4 = [
{from: 1, to: 2},
];
var container_4 = document.getElementById("container_4");
var data_4= {
nodes: nodes_4,
edges: edges_4
};
var options_4 = {
width: "600px",
height: "600px"
};
var network_4 = new vis.Network(container_4, data_4, options_4);
});
$(function(){
var nodes_5 = [
{id: 1, label: "lens"},
{id: 2, label: "fairly"},
];
var edges_5 = [
{from: 1, to: 2},
];
var container_5 = document.getElementById("container_5");
var data_5= {
nodes: nodes_5,
edges: edges_5
};
var options_5 = {
width: "600px",
height: "600px"
};
var network_5 = new vis.Network(container_5, data_5, options_5);
});
