package com.example.APIAnalitica.modelos;

import jakarta.persistence.*;

import java.time.LocalDate;

@Entity
@Table(name = "usuario")
public class Usuario {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 50,nullable = false,unique = false)
    private String nombre;

    @Column(length = 10,nullable = false)
    private String contrasena;

    private LocalDate fechaNacimiento;

    public Usuario() {
    }

    public Usuario(Integer id, LocalDate fechaNacimiento, String contrasena, String nombre) {
        this.id = id;
        this.fechaNacimiento = fechaNacimiento;
        this.contrasena = contrasena;
        this.nombre = nombre;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getContrasena() {
        return contrasena;
    }

    public void setContrasena(String contrasena) {
        this.contrasena = contrasena;
    }

    public LocalDate getFechaNacimiento() {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(LocalDate fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }
}
