console.log("ali");
var i=0;
var slidImag=["{% static 'imag/man_weman/9.jpg' %}","{% static 'imag/man_weman/9.jpg' %}","{% static 'imag/man_weman/9.jpg' %}","{% static 'imag/man_weman/9.jpg' %}","{% static 'imag/man_weman/9.jpg' %}","{% static 'imag/man_weman/9.jpg' %}","{% static 'imag/man_weman/9.jpg' %}","{% static 'imag/man_weman/9.jpg' %}"];

var slidShow=function(){
    
    document.slidshow.src=slidImag[i];
    if (i < slidImag.length-1){
        i++;
    }else{
        i=0;
    }
    setTimeout("slidShow()",2000);
}
slidShow()

