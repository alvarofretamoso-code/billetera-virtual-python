# 💰 Billetera Virtual CLI - Python & SQLite

Este proyecto es una aplicación de gestión financiera por línea de comandos (CLI) diseñada con un enfoque en la **integridad de datos** y la **programación orientada a objetos (POO)**. 

El objetivo del proyecto fue construir un sistema robusto donde la lógica de negocio y la persistencia en base de datos estén desacopladas y verificadas.

## 🛠️ Tecnologías y Herramientas
- **Lenguaje:** Python 3.13
- **Base de Datos:** SQLite (Relacional)
- **Testing:** Pytest
- **Control de Versiones:** Git / GitHub

## 🌟 Características Principales
- **Gestión de Usuarios:** Registro y consulta de información personal.
- **Transacciones Seguras:** Depósitos, extracciones y transferencias entre cuentas con validación de saldo.
- **Historial de Movimientos:** Registro detallado de cada operación financiera.
- **Persistencia SQL:** Uso de Foreign Keys y transacciones para asegurar la consistencia de la información.

## 📐 Arquitectura del Proyecto
El sistema sigue una arquitectura modular para facilitar el mantenimiento y escalabilidad:
- `models.py`: Definición de clases (Usuario, Billetera, Cuenta, Movimiento).
- `db_manager.py`: Capa de persistencia y consultas SQL.
- `main.py`: Interfaz de usuario por consola y flujo lógico.
- `tests/`: Suite de pruebas automatizadas.

## 🧪 Calidad y Testing (9/9 PASSED) ✅
Se implementaron 9 tests automatizados que cubren:
1. Validaciones de modelos de datos.
2. Integración con la base de datos (usando bases temporales para pruebas limpias).
3. Lógica de saldos y transferencias.

> ⚠️ **Transparencia técnica:** Si bien la lógica de negocio y la arquitectura SQL son de autoría propia, la estructura de los tests de integración contó con el apoyo de herramientas de IA, lo que permitió abarcar el proceso de testeo de manera exhaustiva.

**Para ejecutar los tests:**
```bash
python -m pytest -v