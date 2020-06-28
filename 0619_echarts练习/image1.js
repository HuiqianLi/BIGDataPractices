// 基于准备好的dom，初始化echarts实例，ECharts 库使用 json 格式来配置。
var myChart = echarts.init(document.getElementById('main'), 'walden');
 
// 指定图表的配置项和数据
var option = {
    title: {
        text: '啊吗粽-'+'这四个up主 好有文化！ (第三期)'
    },
    //配置提示信息：
    tooltip: {},
    legend: {
        data:['数量']
    },
    //配置要在 X 轴显示的项
    xAxis: {
        data: ["comment","play","video_review","favorite","coin","share","like"]
    },
    //配置要在 Y 轴显示的项
    yAxis: {},
    //每个系列通过 type 决定自己的图表类型
    //type: 'bar'：柱状/条形图
    series: [{
        name: '数量',  // 系列名称
        type: 'bar',  // 系列图表类型
        data: [6953,1943709,22485,25715,41614,6936,215477]  // 系列中的数据内容
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);