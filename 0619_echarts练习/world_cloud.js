// 基于准备好的dom，初始化echarts实例，ECharts 库使用 json 格式来配置。
var myChart = echarts.init(document.getElementById('worldcloud'), 'walden');

option = {
    title: {
        text: '词云',//标题
        x: 'center',
        textStyle: {
            fontSize: 23
        }

    },
    // backgroundColor: '#F7F7F7',
    tooltip: {
        show: true
    },
    series: [{
        name: '热点分析',//数据提示窗标题
        type: 'wordCloud',
        sizeRange: [6, 66],//画布范围，如果设置太大会出现少词（溢出屏幕）
        rotationRange: [-45, 90],//数据翻转范围
        //shape: 'circle',
        textPadding: 0,
        autoSize: {
            enable: true,
            minSize: 6
        },
        drawOutOfBound: true,//词云显示完整，超出画布的也显示
        textStyle: {
            //正常情况下的样式
            normal: {
                // color: '#00A1F1'    
                color: function() {
                    return 'rgb(' + [
                        Math.round(Math.random() * 255),
                        Math.round(Math.random() * 255),
                        Math.round(Math.random() * 255)
                    ].join(',') + ')';
                }
            },
            //鼠标悬浮时的样式
            emphasis: {                       	
                fontWeight:'bolder', 
                // fontSize:30,
                color: '#f97396',
            }
        },
        data: [] //data是通过ajax取的，这里先空着，取完之后再重新渲染
    }]
};

//通过ajax取数据
$.ajax({
        type:"get",
        url:"json/cloud.json",
        dataType: "json",
        success:function(data){
            //ajax请求成功时执行
            window.onload = setTimeout(function(){
                var list = [];
                for (var i = 0; i < data.dataCloud.length; i++){
                    list.push({
                        name:data.dataCloud[i].name,
                        value:Number(data.dataCloud[i].value)
                    })		    			
                }		    				    		
                myChart.setOption({
                    series:[{
                        type: 'wordCloud',
                        data:list
                    }]
                });
            },100)
            myChart.hideLoading();
        },
        
        error:function(errorMsg){
            //ajax请求失败时执行
            alert("图表请求数据失败!");
            myChart.hideLoading();	    		
        }

});

myChart.setOption(option);