let x = 0;
function load() {
    if (x < 1){
        window.open('{{direct_link}}');
        window.history.back();
        x +=1;
    };
};
