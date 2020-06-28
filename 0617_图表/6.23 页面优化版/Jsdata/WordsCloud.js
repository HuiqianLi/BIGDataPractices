// 
//
//
/////////////记得添加		drawrWordsCloudchart(params.dataIndex);
///////////在触发js文件后添加


function drawrWordsCloudchart(i)
{

	//echarts进行初始化

	var myChart = echarts.init(document.getElementById("WordsCloud"),'walden');
	option = {
		tooltip: {
			show: true
		},
		
		series: [{
			type: 'wordCloud',
			gridSize: 1,
			sizeRange: [10,90],
			rotationRange: [-45,0,45,90],
			shape: 'circle',

			textStyle: {
				normal: {
					//随机生成颜色
					color: function()
					{
						var colors = [
							"#f97396",
							"#00a1d6",
							"#ffd778",
							"#6dc781",
							"#73c9e5",
							"#ffba7b",
							'#9796ed',
							'#7b78eb',
							'#ff5c7a',
							'#17ad8a',
							'#f39800',
							'#58d598',
							'#48cfe5',
							'#ff9dc6',
							'#1765bb'];
						return colors[parseInt(Math.random() * 10)];
					}
				}
			},
			left: 'center',
			top: 'center',
			// width: '96%',
			// height: '100%',
			right: null,
			bottom: null,
			// width: 300,
			// height: 200,
			// top: 20,S
			data: []
		}]
	}
	$.getJSON('jsonData/Word.json').done(function(data)
	{
		// 填入数据
		myChart.setOption({
			series: [
				{
					data: data.data[i]
				}
			]
		});
	});
	myChart.setOption(option);
};// JavaScript Documenta