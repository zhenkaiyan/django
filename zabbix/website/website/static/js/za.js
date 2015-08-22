require.config({
	paths: {
		echarts: 'http://echarts.baidu.com/build/dist'
	}
});
require(
	[
		'echarts',
		'echarts/chart/bar' // 使用柱状图就加载bar模块，按需加载
	],
	function (ec) {
		var myechart = ec.init(document.getElementById('barch'));
		var option = {
			tooltip:{
				show:true
			},
			legend:{
				data:['概览']
			},
			xAxis :[
				{
					type : 'category',
				data : ["memory","disk","load","PING"]
				}
			],
			yAxis :[
				{
					type : 'value'
				}
			],
			series :[
				{
					name:'概览',
					type:"bar",
					data : [a,b,c,d]
				}
			],

		}
		myechart.setOption(option);
	}
)
require.config(
	{
		paths: {
			echarts: 'http://echarts.baidu.com/build/dist'
		}
	});
require(
		[
			'echarts',
			'echarts/chart/pie' 
		],
function (ec) {
			// 基于准备好的dom，初始化echarts图表
			var myechart = ec.init(document.getElementById('main')); 
			var idx = 1
			var option = {
			tooltip : {
				trigger: 'item',
				formatter: "{a} <br/>{b} : {c} ({d}%)"
			},
			legend: {
				data:['memory','disk','load','PING']
			},
			toolbox: {
				show : true,
				x:'center',
				y:'bottom',
				feature : {
					mark : {show: true},
					dataView : {show: true, readOnly: false},
					magicType : {
						show: true, 
						type: ['pie', 'funnel'],
						option: {
							funnel: {
								y: 'bottom',
								width: '50%',
								funnelAlign: 'left',
								max: 1700
							}
						}
					},
					restore : {show: true},
					saveAsImage : {show: true}
				}
			},
			series : [
				{
					name:'一天内报警数量',
					type:'pie',
					center: ['50%', '45%'],
					radius: '50%',
					data:[
					{value: idx * 128 + a,  name:'memory'},
					{value: idx * 64  + b,  name:'disk'},
					{value: idx * 32  + c,  name:'load'},
					{value: idx * 16  + d,  name:'PING'},
					]
				}
			]
		}
			// 为echarts对象加载数据 
			myechart.setOption(option); 
		}
	);
