import{buscarUsuario,guardarUsuarios} from "../services/servicioUsuario.js"




//capturar los datos del formulario
let cajaNombreUsuario =document.getElementById("nombre")
let cajaContrasenaUsuario=document.getElementById("contrasena")
let cajaFechaUsuario=document.getElementById("fecha")
let botonFormulario=document.getElementById("boton")

botonFormulario.addEventListener("click",(evento)=>{
    evento.preventDefault()
    let datos={
        nombre:cajaNombreUsuario.value,
        contrasena:cajaContrasenaUsuario.value,
        fechaNacimiento:cajaFechaUsuario.value

    }
    
    guardarUsuarios(datos)
    .then(function(respuesta){
        if(respuesta){
            Swal.fire("Buen trabajo");
        }else{
            Swal.fire("Algo salio mal en el registro");
        }
    })
}

)
//llamar al api

//mostrar mensaje de exito