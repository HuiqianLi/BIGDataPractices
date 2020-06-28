//***************************商业价值柱状图函数************************************************************************/
$(document).ready(function () {

    //echarts进行初始化

    var myChart = echarts.init(document.getElementById("Bar"), 'walden');

    var option = {

        //图标题

        //title:{text: '百大up主商业价值'},

        //背景色
        backgroundColor: '',

        //图提示框

        tooltip: {
            show: true,
            trigger: 'item',//数据项图形触发
            axisPointer: { //指示样式
                type: 'shadow',
                axis: 'auto',
            },
            padding: 5,
            textStyle: {//提示框内容格式
                color: "#fff"
            }
        },

        //图例

        legend: {

            data: ['up主商业价值', 'up主作品价值']

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

            top: '12%',
            left: '1%',
            right: '10%',
            containLabel: true,


        },

        //x轴属性

        xAxis: {
            axisLabel: {
                interval: 0,
                rotate: 45,
            },//逆时针旋转45
            type: 'category',
            data: []

        },

        //y轴属性

        yAxis: {
            name: '个人价值',

        },
        //可拖动时间轴	
        dataZoom: [
            {
                type: 'slider',
                show: true,
                start: 94,//数据窗口范围起始百分比94%
                end: 100,
                handleSize: 8,
                filterMode: 'filter'//主轴
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

                name: 'up主商业价值',
                type: 'bar',//图类型：柱状图
                legendHoverLink: true,
                label: {
                    show: false, //在柱形上显示数据
                    position: 'insideTop'
                },
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
                barWith: '5',
                barGap: '0.1',
                barCategoryGap: '2',// 柱形间距	
                //color:['#C0FF3E'],//设置图像颜色
                //opacity: 0.5,//图形透明度
                data: []//图表数据
            },
            {

                name: 'up主作品价值',
                type: 'bar',//图类型：柱状图
                legendHoverLink: true,
                label: {
                    show: false, //在柱形上显示数据
                    position: 'insideTop'
                },
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
                barWith: '5',
                barCategoryGap: '10',// 柱形间距	
                //color:['#C0FF3E'],//设置图像颜色
                //opacity: 0.5,//图形透明度

                data: []//图表数据
            }
        ]
    };

    //使用jQuery中的$.get()获取data.json文件，使用done函数;

    //done(function(data))中data表示调用的函数返回的数据
    myChart.clear();//清理画布
    $.getJSON('../static/data/BusinessResult.json').done(function (data) {

        myChart.setOption({

            xAxis: {

                data: data.UPname

            },
            series: [
                {

                    name: 'up主商业价值',

                    data: data.Business

                },
                {

                    name: 'up主作品价值',

                    data: data.Works

                },

            ]

        });

    });

    myChart.setOption(option);
    // 使用刚指定的配置项和数据显示图表。
    //var ecConfig = echarts.config;
	/*myChart.off('click', function (params) {
		     drawradarchart(100);
			  drawpiechart(100);
		    
		});//渲染点击事件前清除之前点击事件*/
    var i = 0;
    myChart.on('click', function (params) {
        //Salert(params.dataIndex);
        if (parseInt(params.dataIndex) == i) {//判断是否为同一up主
            //alert(i);
        }
        else {
            drawpiechart(100);
            drawradarchart(100);
        }

        if (params.seriesIndex == 0)//点击商业价值显示雷达图
        {
            drawradarchart(params.dataIndex);//数值序列，x轴上当前点是 第几个点第几个点 up主自身数据

            //drawradarchart(100);
        }
        else                        //点击作品价值显示分区饼图
        {
            drawpiechart(params.dataIndex);//up主各分区投稿数

            //drawpiechart(100);
        }

        i = params.dataIndex;
        //drawradarchart(params.dataIndex);

        //drawpiechart(params.dataIndex);//up主各分区投稿数
        drawrWordsCloudchart(params.dataIndex);//词云
    });
});
// JavaScript Document