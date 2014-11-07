$(function(){
var nodes_1 = [
{id: 1, label: "size"},
{id: 2, label: "small"},
{id: 3, label: "enough"},
{id: 4, label: "easily"},
{id: 5, label: "coat"},
{id: 6, label: "pocket"},
{id: 7, label: "purse"},
{id: 8, label: "size"},
{id: 9, label: "perfect"},
{id: 10, label: "little"},
{id: 11, label: "hands"},
{id: 12, label: "perhaps"},
{id: 13, label: "uncomfortable"},
{id: 14, label: "awkward"},
{id: 15, label: "person"},
{id: 16, label: "canon"},
{id: 17, label: "slr"},
{id: 18, label: "so"},
{id: 19, label: "very"},
{id: 20, label: "compact"},
{id: 21, label: "also"},
{id: 22, label: "travel"},
];
var edges_1 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
{from: 1, to: 6},
{from: 1, to: 7},
{from: 1, to: 8},
{from: 1, to: 9},
{from: 1, to: 10},
{from: 1, to: 11},
{from: 1, to: 12},
{from: 1, to: 13},
{from: 1, to: 14},
{from: 1, to: 15},
{from: 1, to: 16},
{from: 1, to: 17},
{from: 1, to: 18},
{from: 1, to: 19},
{from: 1, to: 20},
{from: 1, to: 21},
{from: 1, to: 22},
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
{id: 1, label: "lens"},
{id: 2, label: "digital"},
{id: 3, label: "zoom"},
{id: 4, label: "as"},
{id: 5, label: "good"},
{id: 6, label: "pictures"},
{id: 7, label: "optical"},
{id: 8, label: "built-in"},
{id: 9, label: "lot"},
{id: 10, label: "price"},
{id: 11, label: "range"},
];
var edges_2 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
{from: 1, to: 6},
{from: 1, to: 7},
{from: 1, to: 8},
{from: 1, to: 9},
{from: 1, to: 10},
{from: 1, to: 11},
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
{id: 1, label: "battery"},
{id: 2, label: "nt"},
{id: 3, label: "big"},
{id: 4, label: "offensive"},
{id: 5, label: "pics"},
{id: 6, label: "battery"},
{id: 7, label: "life"},
{id: 8, label: "ok"},
{id: 9, label: "rechargable"},
{id: 10, label: "not"},
{id: 11, label: "last"},
{id: 12, label: "long"},
{id: 13, label: "especially"},
{id: 14, label: "flash"},
{id: 15, label: "lot"},
{id: 16, label: "short"},
{id: 17, label: "side"},
{id: 18, label: "adequate"},
{id: 19, label: "most"},
{id: 20, label: "situations"},
{id: 21, label: "great"},
{id: 22, label: "pictures"},
{id: 23, label: "excellent"},
{id: 24, label: "canon"},
{id: 25, label: "s"},
{id: 26, label: "batteries"},
{id: 27, label: "proprietary"},
{id: 28, label: "really"},
{id: 29, label: "time"},
{id: 30, label: "recharge"},
{id: 31, label: "fairly"},
{id: 32, label: "quickly"},
{id: 33, label: "camera"},
{id: 34, label: "power"},
{id: 35, label: "even"},
{id: 36, label: "knockoff"},
{id: 37, label: "charger"},
{id: 38, label: "spare"},
{id: 39, label: "right"},
{id: 40, label: "here"},
{id: 41, label: "amazon"},
];
var edges_3 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
{from: 1, to: 6},
{from: 1, to: 7},
{from: 1, to: 8},
{from: 1, to: 9},
{from: 1, to: 10},
{from: 1, to: 11},
{from: 1, to: 12},
{from: 1, to: 13},
{from: 1, to: 14},
{from: 1, to: 15},
{from: 1, to: 16},
{from: 1, to: 17},
{from: 1, to: 18},
{from: 1, to: 19},
{from: 1, to: 20},
{from: 1, to: 21},
{from: 1, to: 22},
{from: 1, to: 23},
{from: 1, to: 24},
{from: 1, to: 25},
{from: 1, to: 26},
{from: 1, to: 27},
{from: 1, to: 28},
{from: 1, to: 29},
{from: 1, to: 30},
{from: 1, to: 31},
{from: 1, to: 32},
{from: 1, to: 33},
{from: 1, to: 34},
{from: 1, to: 35},
{from: 1, to: 36},
{from: 1, to: 37},
{from: 1, to: 38},
{from: 1, to: 39},
{from: 1, to: 40},
{from: 1, to: 41},
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
{id: 1, label: "video"},
{id: 2, label: "audio"},
{id: 3, label: "video"},
{id: 4, label: "also"},
{id: 5, label: "mono"},
{id: 6, label: "fairly"},
{id: 7, label: "acceptable"},
{id: 8, label: "quiet"},
{id: 9, label: "little"},
{id: 10, label: "distortions"},
];
var edges_4 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
{from: 1, to: 6},
{from: 1, to: 7},
{from: 1, to: 8},
{from: 1, to: 9},
{from: 1, to: 10},
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
{id: 1, label: "picture"},
{id: 2, label: "pictures"},
{id: 3, label: "razor-sharp"},
{id: 4, label: "even"},
{id: 5, label: "macro"},
{id: 6, label: "slightest"},
{id: 7, label: "shakes"},
{id: 8, label: "totally"},
{id: 9, label: "distorts"},
{id: 10, label: "image"},
{id: 11, label: "just"},
{id: 12, label: "shoot"},
{id: 13, label: "photos"},
{id: 14, label: "great"},
{id: 15, label: "camera"},
{id: 16, label: "everywhere"},
{id: 17, label: "constantly"},
{id: 18, label: "quality"},
{id: 19, label: "number"},
{id: 20, label: "different"},
{id: 21, label: "ways"},
{id: 22, label: "daylight"},
{id: 23, label: "brilliant"},
{id: 24, label: "indoor"},
{id: 25, label: "shots"},
{id: 26, label: "very"},
{id: 27, label: "good"},
{id: 28, label: "lengthy"},
{id: 29, label: "extensive"},
{id: 30, label: "journey"},
{id: 31, label: "feature-loaded"},
{id: 32, label: "high"},
{id: 33, label: "performance"},
{id: 34, label: "travel"},
{id: 35, label: "size"},
{id: 36, label: "initially"},
{id: 37, label: "little"},
{id: 38, label: "gem"},
{id: 39, label: "superior"},
{id: 40, label: "picture"},
{id: 41, label: "mega"},
{id: 42, label: "pixel"},
{id: 43, label: "tv"},
{id: 44, label: "excellent"},
{id: 45, label: "automatic"},
{id: 46, label: "mode"},
{id: 47, label: "beautiful"},
{id: 48, label: "crisp"},
{id: 49, label: "hundreds"},
];
var edges_5 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
{from: 1, to: 6},
{from: 1, to: 7},
{from: 1, to: 8},
{from: 1, to: 9},
{from: 1, to: 10},
{from: 1, to: 11},
{from: 1, to: 12},
{from: 1, to: 13},
{from: 1, to: 14},
{from: 1, to: 15},
{from: 1, to: 16},
{from: 1, to: 17},
{from: 1, to: 18},
{from: 1, to: 19},
{from: 1, to: 20},
{from: 1, to: 21},
{from: 1, to: 22},
{from: 1, to: 23},
{from: 1, to: 24},
{from: 1, to: 25},
{from: 1, to: 26},
{from: 1, to: 27},
{from: 1, to: 28},
{from: 1, to: 29},
{from: 1, to: 30},
{from: 1, to: 31},
{from: 1, to: 32},
{from: 1, to: 33},
{from: 1, to: 34},
{from: 1, to: 35},
{from: 1, to: 36},
{from: 1, to: 37},
{from: 1, to: 38},
{from: 1, to: 39},
{from: 1, to: 40},
{from: 1, to: 41},
{from: 1, to: 42},
{from: 1, to: 43},
{from: 1, to: 44},
{from: 1, to: 45},
{from: 1, to: 46},
{from: 1, to: 47},
{from: 1, to: 48},
{from: 1, to: 49},
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
$(function(){
var nodes_6 = [
{id: 1, label: "general"},
{id: 2, label: "easy"},
{id: 3, label: "enough"},
{id: 4, label: "grandmother"},
];
var edges_6 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
];
var container_6 = document.getElementById("container_6");
var data_6= {
nodes: nodes_6,
edges: edges_6
};
var options_6 = {
width: "600px",
height: "600px"
};
var network_6 = new vis.Network(container_6, data_6, options_6);
});
$(function(){
var nodes_7 = [
{id: 1, label: "price"},
{id: 2, label: "great"},
{id: 3, label: "price"},
{id: 4, label: "features"},
{id: 5, label: "camera"},
{id: 6, label: "affordable"},
{id: 7, label: "cheap"},
];
var edges_7 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
{from: 1, to: 6},
{from: 1, to: 7},
];
var container_7 = document.getElementById("container_7");
var data_7= {
nodes: nodes_7,
edges: edges_7
};
var options_7 = {
width: "600px",
height: "600px"
};
var network_7 = new vis.Network(container_7, data_7, options_7);
});
