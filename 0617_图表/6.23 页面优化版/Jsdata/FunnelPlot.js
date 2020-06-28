
//echarts进行初始化
var myChart = echarts.init(document.getElementById("Funnel"), 'walden');

//alert(data.data[i].UPname);//测试弹窗
myChart.setOption({
    title: {
        text: '各区投稿人数分布图',
    },
    tooltip: {
        trigger: 'item',
        formatter: "{b}区投稿人数 :<br/> {c}个up主"//a系列名,b数据项名,c数据值
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
        data: ['鬼畜', '生活', '时尚', '知识', '游戏', '娱乐', '动画', '音乐', '舞蹈', '影视', '纪录片', '国创', '数码']
    },

    series: [
        {
            name: '投稿人数：',
            type: 'funnel',
            left: '10%',
            top: 100,
            //x2: 80,
            bottom: 60,
            width: '80%',
            // height: {totalHeight} - y - y2,
            min: 0,
            max: 100,
            minSize: '0%',
            maxSize: '100%',
            sort: 'descending',//漏斗,ascending金字塔形
            gap: 2,
            label: {
                show: true,
                position: 'inside'
            },
            labelLine: {
                length: 10,
                lineStyle: {
                    width: 1,
                    type: 'solid'
                }
            },
            itemStyle: {
               /* color: {
                    type: 'linear',
                    x: 0,
                    y: 0.5,
                    x2: 0,
                    y2: 1,
                    colorStops: [{
                        offset: 0, color: '#f97396' // 0% 处的颜色
                    }, {
                        offset: 1, color: '#1765bb' // 100% 处的颜色
                    }],
                    global: false // 缺省为 false
                },
                */
                borderColor: '#fff',
                borderWidth: 1
            },
            emphasis: {
                label: {
                    fontSize: 20
                }
            },
            data: [
                { value: 11, name: '鬼畜' },
                { value: 84, name: '生活' },
                { value: 10, name: '时尚' },
                { value: 13, name: '知识' },
                { value: 47, name: '游戏' },
                { value: 6, name: '娱乐' },
                { value: 14, name: '动画' },
                { value: 27, name: '音乐' },
                { value: 3, name: '舞蹈' },
                { value: 12, name: '影视' },
                { value: 1, name: '纪录片' },
                { value: 6, name: '国创' },
                { value: 9, name: '数码' },
            ]
        }
    ]
	

});

myChart.on('click', function (params) {
        //alert(params.dataIndex);
		//alert(param.seriesIndex);
        //drawradarchart(params.dataIndex);//数值序列，x轴上当前点是 第几个点第几个点 up主自身数据
        //drawfunnelchart(params.dataIndex);   
        //drawpiechart(params.dataIndex);//up主各分区投稿数
		//drawrWordsCloudchart(params.dataIndex);//词云
    });




// JavaScript Document