$(document).ready(function () {

    //echarts进行初始化

    var myChart = echarts.init(document.getElementById("Line"), 'walden');

    myChart.setOption({

        //图标题

        title: { text: 'up主折线图' },

        //图提示框

        tooltip: {
            show: true,
            trigger: 'axis',//数据项图形触发
            formatter: function (params) {//让tooltip内容降序显示，忽略错误
       
				let newParams = [];
		        let tooltipString = [];
		        newParams = [...params];
		        newParams.sort((a,b) => {return b.value - a.value});
                newParams.forEach((p) => {
                    const cont = p.marker + ' ' + p.seriesName + ': ' + p.value + '<br/>';
                    tooltipString.push(cont);
                });
                return tooltipString.join('');
            },
            axisPointer: { //指示样式
                type: 'shadow',
                axis: 'auto',
            },
            padding: 5,
            textStyle: {//提示框内容格式
                color: "#fff"
            },
			
        },

        //图例

        legend: {

            data: ['总评论量', '总弹幕量', '总点赞量', '总投币数', '总收藏数']

        },
        
		//工具箱
        toolbox: {
            show: true,
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                dataView: {
                    show: true,
                    readOnly: false
                },
                magicType: { type: ['line', 'bar'] },
                saveAsImage: {},//保存
                restore: {},   //刷新

            },
        },
		
        grid: {

            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true

        },

        //x轴属性

        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []

        },

        //y轴属性

        yAxis: {
            name: '用户数量',
			type: 'value',
			splitNumber:  20

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

        series: [

            {
                name: '总评论量',
                type: 'line',
                //stack: '总量',
				itemStyle: {
                    normal: {
                        //柱形图圆角，初始化效果
                        barBorderRadius: [18, 18, 0, 0],
                        opacity: 0.8,
                        color: new echarts.graphic.LinearGradient(//渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(251,116,151)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(249,182,200)'
                            }, {
                                offset: 1,
                                color: '#F9DEE5'
                            }]
                        ),

                    },
                    emphasis: {
                        //barBorderRadius: 30,//圆角大小
						color: new echarts.graphic.LinearGradient(//高亮渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(249,200,213)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(249,133,163)'
                            }, {
                                offset: 1,
                                color: 'rgb(249,11,74)'
                            }]
                        ),


                    },
                    
                },
                data: []
            },
            {
                name: '总弹幕量',
                type: 'line',
                //stack: '总量',
				itemStyle: {
                    normal: {
                        //柱形图圆角，初始化效果
                        barBorderRadius: [18, 18, 0, 0],
						color: new echarts.graphic.LinearGradient(//渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(0,161,214)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(67,186,235)'
                            }, {
                                offset: 1,
                                color: 'rgb(215,229,235)'
                            }]
                        )
                    },
                    emphasis: {
                        //barBorderRadius: 30,//圆角大小
						color: new echarts.graphic.LinearGradient(//高亮渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(165,215,235)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(81,190,235)'
                            }, {
                                offset: 1,
                                color: 'rgb(0,167,235)'
                            }]
                        )

                    },
                    
                },
                data: []
            },
            {
                name: '总点赞量',
                type: 'line',
                //stack: '总量',
				itemStyle: {
                    normal: {
                        //柱形图圆角，初始化效果
                        barBorderRadius: [18, 18, 0, 0],
                        opacity: 0.8,
                        color: new echarts.graphic.LinearGradient(//渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(255,215,120)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(255,223,147)'
                            }, {
                                offset: 1,
                                color: 'rgb(255,243,215)'
                            }]
                        ),

                    },
                    emphasis: {
                        //barBorderRadius: 30,//圆角大小
						color: new echarts.graphic.LinearGradient(//高亮渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(255,239,201)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(255,211,108)'
                            }, {
                                offset: 1,
                                color: 'rgb(255,190,36)'
                            }]
                        ),


                    },
                    
                },
                data: []
            },
            {
                name: '总投币数',
                type: 'line',
                //stack: '总量',
				itemStyle: {
                    normal: {
                        //柱形图圆角，初始化效果
                        barBorderRadius: [18, 18, 0, 0],
                        opacity: 0.8,
                        color: new echarts.graphic.LinearGradient(//渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(109,199,129)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(136,199,150)'
                            }, {
                                offset: 1,
                                color: 'rgb(214,252,176)'
                            }]
                        ),

                    },
					emphasis: {
                        //barBorderRadius: 30,//圆角大小
						color: new echarts.graphic.LinearGradient(//高亮渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(201,252,151)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(44,199,78)'
                            }, {
                                offset: 1,
                                color: 'rgb(82,199,108)'
                            }]
                        ),


                    },
                    
                },
                data: []
			},

            {
                name: '总收藏数',
                type: 'line',
                //stack: '总量',
				itemStyle: {
                    normal: {
                        //柱形图圆角，初始化效果
                        barBorderRadius: [18, 18, 0, 0],
                        opacity: 0.8,
                        color: new echarts.graphic.LinearGradient(//渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(136,135,237)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(173,172,237)'
                            }, {
                                offset: 1,
                                color: 'rgb(228,228,237)'
                            }]
                        ),

                    },
					emphasis: {
                        //barBorderRadius: 30,//圆角大小
						color: new echarts.graphic.LinearGradient(//高亮渐变色
                            0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgb(198,197,237)'
                            }, {
                                offset: 0.5,
                                color: 'rgb(159,158,237)'
                            }, {
                                offset: 1,
                                color: 'rgb(92,90,237)'
                            }]
                        ),


                    },
                    
                },
                data: []
            }
        ]
    });

    //使用jQuery中的$.get()获取data.json文件，使用done函数;

    //done(function(data))中data表示调用的函数返回的数据

    $.getJSON('jsonData/DetailResultsLine.json').done(function (data) {

        myChart.setOption({

            xAxis: {

                data: data.up_name

            },
            series: [{

                name: '总评论量',
                data: data.comments,
            },


            {
                name: '总弹幕量',
                data: data.video_reviews,
            },

            {
                name: '总点赞量',
                data: data.likes,
            },

            {
                name: '总投币数',
                data: data.coins,
            },

            {
                name: '总收藏数',
                data: data.favorites
            }]



        });

    });

});// JavaScript Document