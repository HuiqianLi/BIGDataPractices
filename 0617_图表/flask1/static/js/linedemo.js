$(document).ready(function(){

        //echarts进行初始化

		var myChart = echarts.init(document.getElementById("Line"),'walden');

		myChart.setOption({

            //图标题

			title:{text: 'up主折线图'},

            //图提示框

			tooltip:{
				show:true,
				trigger: 'axis',//数据项图形触发
				axisPointer:{ //指示样式
					type: 'shadow',
					axis:'auto',
					},
				padding: 5,
				textStyle:{//提示框内容格式
					color: "#fff"
					}
			 },

            //图例

			legend: {
				
				data: ['总播放量', '总弹幕量', '总点赞量', '总投币数', '总收藏数']
				
				},
			
			grid: {
				
				left: '3%',
				right: '4%',
				bottom: '3%',
                containLabel: true
				
			},

            //x轴属性

			xAxis:{
				 type : 'category',
				 boundaryGap: false,
				 data:[]

			},

            //y轴属性

			yAxis:{
				name: '用户数量',
				
				},
			//可拖动时间轴	
			dataZoom: [
            {
                type: 'slider',
                show: true,
                start: 94,//数据窗口范围起始百分比94%
                end: 100,
                handleSize: 8
				//showDetail:false //选中时显示详细信息
            },
            {
                type: 'inside',//类型
                start: 94,
                end: 100
            },
            {
                type: 'slider',
                show: true,
                yAxisIndex: 0,//设置dataZoom组件控制的y轴
                filterMode: 'empty',//数据过滤类型
                width: 12,
                height: '70%',
                handleSize: 8,
                showDataShadow: false,
                left: '93%'
            }
        ],	

			//数据存放

			series:[

				{
            name: '总播放量',
            type: 'line',
            stack: '总量',
            data: []
			},
        {
            name: '总弹幕量',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '总点赞量',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '总投币数',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '总收藏数',
            type: 'line',
            stack: '总量',
            data: []
        }			
		]
		});

        //使用jQuery中的$.get()获取data.json文件，使用done函数;

        //done(function(data))中data表示调用的函数返回的数据

		$.getJSON('../static/data/DetailResultsLine.json').done(function(data){

			myChart.setOption({

				xAxis:{

					data:data.up_name

				},
				series:[{
				
						name: '总播放量',
						data: data.plays,},
			
        
           {
			    name: '总弹幕量',
				data: data.video_reviews,},
       
           {
			    name: '总点赞量',
				data: data.likes,},
			
            {
				name: '总投币数',
            data: data.coins,},
			
            {name: '总收藏数',
            data: data.favorites}]
       			
				

			});

		});		

		});// JavaScript Document