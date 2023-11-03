# Security Question
---
### Componentes

- Aplicación movil (Android iOS)
- Aplicación web (Next.js)
- Base de datos (MySQL)
- Backend (FastApi)
- Pesonal
    - 12 ingenieros de software con acceso completo
    - 3 empleados atención al cliente con acceso a datos de cliente (pueden realizar cambios)
    - 1 empleado de ventas

### Consideraciones de seguridad
- Emplear una politica de minimos privilegios para impedir que usuarios finales o empleados de venta puedan modificar datos, ademas de usar validaciones de identidad (como autenticación 2FA) para los empleados de atención al cliente.

- Asegurar que los ingenieros deshabiliten el listado de directorios del servidor web para asegurar que los metadatos de la app no puedan ser accedidos a traves de la raiz del sitio web.

- Asegurar que los ingenieros usen protocolos de transferencia de datos seguros en el desarrollo de la app, no usar protocolos antiguos como FTP y SMTP.

- Asegurarse de identificar datos sensibles como contraseñas e información personal para cifrarlos tanto en trafico como en reposo (en la base de datos), es decir, no guardar datos sensibles en texto claro.

- Implemente validaciones de entradas de datos en el servidor, utilizando "listas blancas".

- Tomar precausiones y controles SQL para evitar inyecciones sql.

- Asegurarse de haber usado estandares y patrones de desarrollo de software seguros y confiables para evitar vulnerabilidades de seguridad a nivel de codigo.

- Asegurarse de que todas las dependencias y componentes usan versiones actualizadas de simismas, ademas de eliminar dependencias que no estén en uso y no se tenga planeado utilizar.

- Llevar un monitoreo continuo de inicios de sesión, control de acceso y validación de entradas de datos para identificar anomalias y posibles fallas de seguridad, ademas de monitorear tambien los diferentes componentes en el lado del servidos implementando firewalls para mantener controlado el trafico. 