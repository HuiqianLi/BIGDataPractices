

//***************************雷达图函数************************************************************************/
//var i ;
function drawradarchart(i) {

    //echarts进行初始化

    var myChart = echarts.init(document.getElementById("Radar"), 'walden');

    //使用jQuery中的$.get()获取data.json文件，使用done函数;

    //done(function(data))中data表示调用的函数返回的数据
     myChart.clear();//清理画布
    $.getJSON('../static/data/RadarAverage.json').done(function (data) {
        //alert(data.data[i].max);测试弹窗

        myChart.setOption({
            title: { 
			    text: data.UPname[i]+' ' ,
				
				
				},

            //图提示框

            tooltip: {
				trigger: 'item',
				//formatter: "{a} <br/>{b} : {c} 个视频"//a系列名,b数据项名,c数据值
				},

            //图例

            toolbox: {

                show: true,
                feature: {

                    //magicType: {type: ['line', 'bar']},
                    saveAsImage: {},//保存
                    restore: {},   //刷新

                },

            },

            legend: {

                data: ['up主雷达图']

            },

            radar: {

                shape: 'circle',  //雷达图形状
                splitNumber: 8,  //圈数
                name: {
                    textStyle: {
                        borderRadius: 3,
                        padding: [3, 5]
                    }
                },
                splitArea: {
                    show: false, //关闭阴影显示
                    areaStyle: {
                        color: 'transparent',
                    }, //背景色

                },
                indicator: [
                    { name: '视频平均评论数', max: data.data[i].maxNum },
                    { name: '视频平均弹幕数', max: data.data[i].maxNum },
                    { name: '视频平均收藏数', max: data.data[i].maxNum },
                    { name: '视频平均投币数', max: data.data[i].maxNum },
                    { name: '视频平均分享数', max: data.data[i].maxNum },
                    { name: '视频平均点赞数', max: data.data[i].maxNum }
                ],

            },

            series: [
                {
                    name: data.UPname[i]+'：',
                    type: 'radar',//图类型：雷达图
                    legendHoverLink: true,
                    data: [
                        {
                            value: data.data[i].value
                        }
                    ],//图表数据
                    areaStyle: {  //填充样式
                        opacity: 0.5
                    }

                }]


        });

    });
   
};// JavaScript Document