(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion")

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click',(e)=>{
            const confimacion = confirm("¿Seguro de eliminar el curso?");
            if(!confimacion){
                e.preventDefault();
            }
        });
    });
    
})();