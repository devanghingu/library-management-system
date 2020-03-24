

$(document).ready(function(){
    

    $("#filestyle-0").change(function(){
        var formdata = new FormData();
        
        var ext={'png':'png','jpeg':'jpeg','jpg':'jpg'};
        var file = $(this).val().split('.').pop();
        if($(this).val()==""){
            alert('Please Select File')
        }
        if(file in ext){
            formdata.append('image',this.files[0])
            formdata.append('csrfmiddlewaretoken',$('input[type=hidden]').val());
            $.ajax({
                url:"/profile_upload",
                method:'POST',
                data:formdata,
                enctype: 'application/x-www-form-urlencoded',
                processData:false,
                contentType:false,
                success:function(data){
                    $('#profile_pic').attr('src',data.url)
                },
                error:function(error){
                    alert(error.error)
                }
            });
            return false;
        }else{
            alert(file+' format not allow')
        }  
        return false;
    });
    // $('#image_upload_form').submit(function(e){
    //     // e.preventDefault();
    //     var formData = new FormData(this);
    //     alert(formData)
    //     var ext={'png':'png','jpeg':'jpeg','jpg':'jpg'};
    //     var file = $(this).val().split('.').pop();
    //     // var csrf=$('input[name=csrfmiddlewaretoken]').val()
    //     if(file in ext){
    //         $.ajax({
    //             url:"/profile_upload",
    //             method:'POST',
    //             data:formdata,
    //             enctype: 'multipart/form-data',
    //             processData:false,
    //             contentType:false,
    //             success:function(data){
    //                 alert(JSON.parse(data))
    //                 return false;
    //             },
    //             error:function(error){
    //                 alert(JSON.parse(error))
    //                 return false;
    //             }
    //         });
    //         return false;
    //     }else{
    //         alert(file+' format not allow')
    //     }  
    //     return false;
    // });
});