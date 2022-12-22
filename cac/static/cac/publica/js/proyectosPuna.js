
const renderProyecto = (proyecto) => {
    
        var cad = `
        <div class="contenedor-galeria">
            <div class="tarjeta">
          
                <div class="cuerpo">
                    <img src= "${proyecto.image} " >
                    <h4> ${proyecto.titulo}</h4>
                    <p> ${proyecto.reseña}</p>
                    
                </div> 
            </div> 
        </div>
        `;
    
    return cad;

}

const divProyectosPuna = document.querySelector("#divProyectosPuna");

fetch('/api_proyectos_puna')
  .then((response) => response.json())
  .then((data) => {
   
        console.log(data);
        let proyectos = data.data;
       
        proyectos.forEach(proyecto => {
            
                let cad = renderProyecto(proyecto);
                divProyectosPuna.insertAdjacentHTML('beforeend', cad);
          
        });
    
  });
