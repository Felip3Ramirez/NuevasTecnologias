package com.example.APIAnalitica.repositorios;


import com.example.APIAnalitica.modelos.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IUsuarioRepositorio extends JpaRepository<Usuario, Integer> {
}
