function drawpiechart(i) {
    var myChart = echarts.init(document.getElementById('Pie'), 'walden');
    // 指定图表的配置项和数据
	myChart.clear();//清理画布
    $.getJSON('jsonData/PieUp.json').done(function (data) {
        myChart.setOption({
            title: {
                text: data.data[i].UPname[0]+' 视频各区分布图',
                //x: 'left'
            },
            tooltip: {

                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} 个视频，所占百分比({d}%)"//a系列名,b数据项名,c数据值
            },
            toolbox: {
                feature: {
                    dataView: { readOnly: false },
                    restore: {},
                    saveAsImage: {}
                }
            },
            legend: {
                top: 50,
                orient: 'vertical',
                left: 10,
                top: 50,
                data: ['鬼畜', '生活', '时尚', '知识', '游戏', '娱乐', '动画', '资讯', '音乐', '舞蹈', '影视', '纪录片', '国创', '数码', '电影']

            },
            stillShowZeroSum: false,
            series: [
                {
                    name: data.data[i].UPname[0]+'所投稿分区',
                    type: 'pie',
                    radius: ['50%', '70%'],//生成圆环
					center: ['50%', '50%'],
                    avoidLabelOverlap: false,
                    label: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        label: {
                            show: true,
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    },
                    labelLine: {
                        show: false
                    },
                    data: [
                        { value: data.data[i].value[0], name: data.data[i].name[0] },
                        { value: data.data[i].value[1], name: data.data[i].name[1] },
                        { value: data.data[i].value[2], name: data.data[i].name[2] },
                        { value: data.data[i].value[3], name: data.data[i].name[3] },
                        { value: data.data[i].value[4], name: data.data[i].name[4] },
                        { value: data.data[i].value[5], name: data.data[i].name[5] },
                        { value: data.data[i].value[6], name: data.data[i].name[6] },
                        { value: data.data[i].value[7], name: data.data[i].name[7] },
                        { value: data.data[i].value[8], name: data.data[i].name[8] },
                        { value: data.data[i].value[9], name: data.data[i].name[9] },
                        { value: data.data[i].value[10], name: data.data[i].name[10] },
                        { value: data.data[i].value[11], name: data.data[i].name[11] },
                        { value: data.data[i].value[12], name: data.data[i].name[12] },
                        { value: data.data[i].value[13], name: data.data[i].name[13] },
                        { value: data.data[i].value[14], name: data.data[i].name[14] },
                    ],
					
					itemStyle: {

                        shadowBlur: 200,//阴影大小
                        shadowColor: 'rgba(0, 0, 0, 0.25)'
                    },
					animationType: 'scale',
                    animationEasing: 'elasticOut',
                    animationDelay: function (idx) {
                        return Math.random() * 200;
                    }
                }
            ]
        });
    });

}
// 基于准备好的dom，初始化echarts实例

// 使用刚指定的配置项和数据显示图表。
//myChart.setOption(option);