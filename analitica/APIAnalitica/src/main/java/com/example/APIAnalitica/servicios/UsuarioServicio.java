package com.example.APIAnalitica.servicios;

import com.example.APIAnalitica.modelos.Usuario;
import com.example.APIAnalitica.repositorios.IUsuarioRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service

public class UsuarioServicio {

    @Autowired
    IUsuarioRepositorio repositorio;

    //Guardar
    public boolean guardarUsuario(Usuario datos)throws Exception{
        try {
            this.repositorio.save(datos);
            return true;
        }catch (Exception error){
            throw new Exception(error.getMessage());
        }

    }

    //BuscarTodos
    public List<Usuario> buscarUsuarios()throws Exception{
        try{
            return this.repositorio.findAll();
        }catch (Exception error){
            throw new Exception(error.getMessage());
        }
    }

}
