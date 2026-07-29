# 🚀 Roadmap: Cloud DevOps Architect

![OS](https://img.shields.io/badge/OS-Linux_antiX-blue?style=for-the-badge&logo=linux)
![Scripting](https://img.shields.io/badge/Scripting-Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Language](https://img.shields.io/badge/Language-Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Development-orange?style=for-the-badge)

Repositorio central para documentar mi avance técnico, scripts de automatización SysAdmin e Infraestructura como Código (IaC).

---

## 🛠️ Stack Tecnológico

| Categoría | Tecnologías | Estado |
| :--- | :--- | :--- |
| **Sistemas Operativos** | Linux (antiX / Debian), Bash Scripting | Dominado / En uso ✅ |
| **Lenguajes & BD** | Python (SysAdmin & Automation), SQL (SQLite/Postgres) | En progreso 🏗️ |
| **Seguridad & Redes** | SSH, Firewalls (UFW), Networking L2/L3, AWS IAM | En progreso 🏗️ |
| **Contenedores** | Docker, Docker Compose, Multi-stage builds | Pendiente ⚠️ |
| **Infraestructura** | Terraform (IaC), Ansible, AWS (EC2, VPC, S3) | Pendiente ⚠️ |
| **Orquestación & CI/CD**| Kubernetes, Helm, GitHub Actions | Pendiente ⚠️ |
| **Observabilidad** | Prometheus, Grafana, Alertmanager | Pendiente ⚠️ |

---

## 📈 Estado del Aprendizaje

- **Fase 1: Fundamentos y Administración Local** `[████████░░] 80%`
  - *Gestión de procesos, permisos, manipulación de archivos, Bash scripting, Python básico y SQL.*
- **Fase 2: Redes y Cloud Networking** `[████░░░░░░] 40%`
  - *Interfaces, DNS, diagnóstico con `mtr`/`ss`, arquitectura de VPCs en AWS.*
- **Fase 3: Seguridad y SSH** `[░░░░░░░░░░] 0%`
  - *Hardening de servidor, criptografía ED25519, UFW y políticas AWS IAM.*
- **Fase 4: Contenedores (Docker)** `[░░░░░░░░░░] 0%`
  - *Dockerfiles optimizados, Docker Compose, escaneo con Trivy y AWS ECR.*
- **Fase 5: Infraestructura como Código (Terraform & Ansible)** `[░░░░░░░░░░] 0%`
  - *Aprovisionamiento declarativo en AWS/GCP, estados `.tfstate` y Playbooks de Ansible.*
- **Fase 6: Orquestación y CI/CD (Kubernetes & GitHub Actions)** `[░░░░░░░░░░] 0%`
  - *Pods, Deployments, Helm charts, pipelines automatizados y GitOps.*
- **Fase 7: Observabilidad (Prometheus & Grafana)** `[░░░░░░░░░░] 0%`
  - *Métricas, agregación de logs con Loki y alertas críticas.*

---

## 📂 Estructura del Repositorio y Roles a Futuro

La arquitectura del repositorio sigue una modularidad orientada a proyectos de producción[cite: 5]:

```text
.
├── .github/
│   └── workflows/        # [CI/CD] Pipelines automatizados de GitHub Actions.
├── containers/           # [Fase 4] Empaquetado y ejecución de aplicaciones.
│   └── docker/           # Dockerfiles, docker-compose.yml y configs de Trivy.
├── docs/                 # [Documentación] Arquitectura y archivos de datos.
│   ├── architecture/     # Diagramas de flujo y red hechos en Mermaid.js.
│   └── json_yaml/        # Ejercicios y plantillas de configuración JSON/YAML.
├── infrastructure/       # [Fase 5] Infraestructura como Código (IaC).
│   └── terraform/        # Archivos .tf, módulos de AWS/GCP e inventarios Ansible.
├── monitoring/           # [Fase 7] Telemetría y métricas del sistema.
│   # Guardará configs de Prometheus, dashboards de Grafana y reglas de Alertmanager.
├── scripts/              # [Fase 1] Automatización SysAdmin y utilidades.
│   ├── bash/             # Scripts Bash para mantenimiento local y auditorías.
│   ├── python/           # Automatizaciones con os, subprocess, Boto3 y reportes Pandas.
│   └── sql/              # Schemas de base de datos SQLite y scripts SQL.
└── README.md             # Visión general y bitácora del repositorio.