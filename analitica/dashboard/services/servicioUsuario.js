export async function guardarUsuarios(datos) {
    
    //1.Para donde voy
    let url="http://localhost:8080/usuarios"
    //2.configurar peticion
    let peticion={
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(datos)

    }
    //3.activar el fetch
    let respuesta=await fetch(url,peticion)
    return await respuesta.json()
}
export async function buscarUsuario() {
    let url="http://localhost:8080/usuarios"
    let peticion={
        method:"GET",
        headers:{
            "Content-Type":"application/json"
        }
    }
    let respuesta=await fetch(url,peticion)
    return await respuesta.json()

}