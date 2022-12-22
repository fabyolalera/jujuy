var cad2=`
<div class="contenedor-galeria">
`
    for(let i=0; i< data2.length ; i++){
        cad2 +=
            `
             <div class="tarjeta">
                                
                <img src="${data2[i].image}" alt="foto">
                <div class="cuerpo">
                    <h4> ${data2[i].titulo}</h4>
                    <p> ${data2[i].reseña}</p>
                    
                </div> 
            </div> 
            `
    }
    cad2+=`
    </div>
`    
document.getElementById("fotos2").innerHTML=cad2
