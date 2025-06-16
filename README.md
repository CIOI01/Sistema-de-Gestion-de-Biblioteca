# 📚 Sistema de Gestión de Biblioteca

Un sistema de gestión de biblioteca completo desarrollado en Python que permite administrar libros, usuarios y préstamos de manera eficiente.

## 🌟 Características Principales

- **Gestión de Libros**: Añadir, eliminar, buscar y listar libros
- **Préstamos**: Registrar préstamos y devoluciones de libros
- **Búsqueda**: Buscar libros por título, autor o ISBN
- **Persistencia de Datos**: Los datos se guardan automáticamente en JSON
- **Interfaz Amigable**: Menú intuitivo con emojis y mensajes claros
- **Historial**: Registro de préstamos históricos por usuario

## ⚙️ Requisitos

- Python 3.8 o superior
- No se requieren dependencias externas

## 🚀 Instalación y Uso

1. Clona el repositorio:
```bash
git clone https://github.com/CIOI01/Sistema-de-Gestion-de-Biblioteca.git
cd gestion-biblioteca
```

2. Ejecuta el sistema:
```bash
python main.py
```

3. Sigue las instrucciones del menú principal.

## 🧩 Estructura del Proyecto

```
gestion-biblioteca/
├── main.py              # Programa principal y menú
├── book_manager.py      # Lógica de gestión de libros
├── data_handler.py      # Manejo de datos (carga/guardado)
├── books.json           # Datos de libros (se crea automáticamente)
└── README.md            # Este archivo
```


![Listado de Libros](https://via.placeholder.com/600x400?text=Listado+de+Libros)

## 🛠️ Funcionalidades Detalladas

### Agregar Libro
```text
1. Add Book
   - Ingresa título, autor y ISBN
   - Validación de campos y duplicados
```

### Prestar Libro
```text
3. Borrow Book
   - Busca libro por ISBN
   - Marca como no disponible
   - Registra el préstamo
```

### Buscar Libros
```text
6. Search Books
   - Búsqueda por título, autor o ISBN
   - Resultados con estado de disponibilidad
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Sigue estos pasos:

1. Haz un fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

---
✨ Desarrollado con Python por [Tu Nombre]
