package com.example.APIAnalitica.controladores;


import com.example.APIAnalitica.modelos.Usuario;
import com.example.APIAnalitica.servicios.UsuarioServicio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/usuarios")
public class UsuarioControlador {
    @Autowired
    UsuarioServicio servicio;

    //Guardar
    @PostMapping
    public ResponseEntity<?>guardar(@RequestBody Usuario datos){
        try{
            return ResponseEntity
                    .status(HttpStatus.CREATED)
                    .body(this.servicio.guardarUsuario(datos));
        } catch (Exception e) {
            return ResponseEntity
                    .status(HttpStatus.BAD_REQUEST)
                    .body(e.getMessage());
        }
    }

    //BuscarTodos
    @GetMapping
    public ResponseEntity<?>buscar(){
        try{
            return ResponseEntity
                    .status(HttpStatus.OK)
                    .body(this.servicio.buscarUsuarios());
        } catch (Exception e) {
            return ResponseEntity
                    .status(HttpStatus.BAD_REQUEST)
                    .body(e.getMessage());
        }

    }
}
