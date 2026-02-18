Asignatura: Tecnologías Emergentes
Carrera: Tecnologías de la Información
Institución: Universidad de las Fuerzas Armadas – ESPE

Repositorio de prácticas SDN y NFV

Este repositorio contiene scripts en Python para la creación de topologías SDN en Mininet y scripts de automatización para la gestión de reglas REST de un firewall virtualizado utilizando el controlador Ryu.

Estructura del repositorio

topologias

- mi-topo-1.py: Topología básica con un switch y dos hosts.
- mi-topo-2.py: Topología extendida con un switch y cuatro hosts.

firewall

- enable_firewall.py: Script para habilitar el firewall REST en el controlador SDN.
- add_rule_icmp.py: Script para agregar una regla que permite tráfico ICMP entre hosts.
- delete_rules.py: Script para eliminar todas las reglas del firewall.

Uso general

1. Iniciar el controlador SDN con soporte para firewall REST.
2. Ejecutar una topología desde Mininet.
3. Ejecutar los scripts de automatización para gestionar las reglas de seguridad.
4. Verificar la conectividad entre hosts.
