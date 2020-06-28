// 基于准备好的dom，初始化echarts实例，ECharts 库使用 json 格式来配置。
var myChart = echarts.init(document.getElementById('worldcloud'), 'walden');

var maskImage = new Image();

var option = {
        title: {
            text: 'China Daily热词'
        },
        //自定义提示工具，加了一张bilibili_tv的图片
    tooltip : {
        formatter:"<img style='width:20px;height:20px;' src='bilibiliTV.png'/> 热度:{c}",	          	
        backgroundColor:'rgba(255,255,255,0)',
        textStyle:{
            fontWeight:'bold', 
            fontSize:20,
            color:'#88878e',
        }
    },
    toolbox: {
        right:'5%',
        feature: {
            dataView: {readOnly: true},															
            restore: {},
            saveAsImage: {}
        }
    },
    series: [ {
        type: 'wordCloud',
        sizeRange: [10, 30],
        rotationRange: [0, 0],  //设置为不旋转                
        gridSize: 2,            //字符之间的间隔
        shape: 'pentagon',
        maskImage: maskImage,  //自定义图案
        drawOutOfBound: false,
        textStyle: {
                //正常情况下的样式
                normal: {
                    color: '#00A1F1'    	
                },
                //鼠标悬浮时的样式
                emphasis: {                       	
                    fontWeight:'bolder', 
                    fontSize:30,
                    color: '#f97396'
                }
        },
        data:[]  //data是通过ajax取的，这里先空着，取完之后再重新渲染

    }],
    graphic: {
        elements: [{
            type: 'image',
            style: {
                width: 280,
                height: 40,
                opacity: 0.9

            },
            right: 'center',
            bottom: '18%',
        }]
    }
};
//
maskImage.onload = function () {
    option.series[0].maskImage
    myChart.setOption(option);
}

myChart.showLoading();

//自定义图案的路径
maskImage.src = 'bilibiliTV.png';

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

//添加点击事件
myChart.on('click',function(params){
        var name = params.name;
        var value = params.value;
        console.log(name + ":" + value);
});

//图表自适应
window.onresize = function () {
    myChart.resize();
}