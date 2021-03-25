//khlee add 21/03/25
function searchajax(){
    $('#search-input').keyup(function(){
        var words = $("#search-input").val();
        if(words != ''){
            console.log(words);
            
            $.ajax({
                type: 'POST',
                url: '/prj1App/browser/searchData/',
                data: {searchinputs : words},
                dataType: 'json',
                
                success: function(result){
                    console.log(result);
                
                    if(result.length > 0){
                        var str = ''
                        for(var i=0; i<result.length; i=i+2){
                            str += '<li><a href="/prj1App/BlogDetail/' + result[i] + '">' + result[i+1] + '</a></li>';
                        }
                        $("#results-container").html(str);
                    }else{
                        $("#results-container").html("");
                    }
                },
                error: function(e) {console.log('error:'+e.status);}
            })
        }else{
            $("#result-container").html("");
        }
    })
}

