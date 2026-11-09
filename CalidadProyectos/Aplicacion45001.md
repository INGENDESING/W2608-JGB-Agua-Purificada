# Aplicación de ISO 45001:2018 al diseño de procesos fisicoquímicos

**Digesto operativo JAGDESING para proyectos derivados de la plantilla MASTER**

| Campo | Valor |
|---|---|
| Documento | Aplicacion45001.md (digesto operativo) |
| Norma base | ISO 45001:2018, *Occupational health and safety management systems — Requirements with guidance for use* [1] |
| Aplicable a | Todo proyecto JAGDESING instanciado con `scripts/new_project.py` |
| Fecha de emisión | 25/09/2026 |
| Estado | REV 1 — vigente (REV 0: 25/09/2026) |

---

## Resumen

**Objetivo.** Establecer cómo los requisitos de ISO 45001:2018 se traducen en decisiones, cálculos, documentos y entregables de ingeniería de procesos fisicoquímicos dentro de la metodología JAGDESING, de modo que todo proyecto derivado de la plantilla demuestre trazabilidad entre los peligros identificados, los controles de diseño adoptados y la evidencia documental generada.

**Métodos.** Se contrastó el texto oficial de ISO 45001:2018 [1,2] con fuentes primarias y técnicas sobre prevención mediante el diseño (NIOSH PtD) [3,4,5,6], análisis de riesgo de procesos (HAZOP, LOPA, bow-tie) [10,11,12], seguridad funcional (IEC 61511) [13,14] y el marco legal colombiano de seguridad y salud en el trabajo (Decreto 1072 de 2015, Resolución 0312 de 2019) [7,8,9].

**Resultados.** Se obtuvo un mapeo normativo entre las cláusulas 4–10 de ISO 45001:2018 y los artefactos concretos de la plantilla (`bases_diseno.yaml`, memorias MC-XXX, informe LaTeX, planos SVG, memorias Excel, Listado de Documentos); una tabla de jerarquía de controles traducida a decisiones de diseño; un catálogo de entregables de SST con criterio de verificación; y un checklist de auditoría aplicable por etapa del proyecto.

**Conclusiones.** ISO 45001:2018 no es un requisito documental añadido al final del proyecto: es una filosofía de diseño. La capacidad de influir sobre la seguridad es máxima en las etapas tempranas (conceptual, FEED) y decrece conforme el diseño se congela [5]; por tanto, la plantilla JAGDESING integra la identificación de peligros y la jerarquía de controles desde `bases_diseno.yaml` y lo propaga a cada memoria, plano e informe.

**Palabras clave:** ISO 45001; seguridad y salud en el trabajo; diseño de procesos; jerarquía de controles; HAZOP; LOPA; seguridad funcional; SG-SST; prevención mediante el diseño.

---

## 1. Alcance y propósito

Este digesto aplica a todo proyecto de ingeniería de procesos fisicoquímicos (química, farmacéutica, alimentaria, energética) ejecutado con la plantilla JAGDESING. Cubre: diseño de proceso y layout; selección de equipos (reactores, tanques, bombas, válvulas, intercambiadores); sistemas de tuberías e instrumentación; modos operativos (normal, arranque, paro, mantenimiento, emergencia); y la generación de evidencias para auditoría de SST. No sustituye la norma ISO 45001:2018 [1] ni el sistema de gestión del cliente; define **cómo la ingeniería JAGDESING alimenta ese sistema** con entregables trazables.

## 2. Criterios de desarrollo del digesto

Este digesto deriva directamente del texto oficial de ISO 45001:2018, consultado en la Plataforma de Bolsillo Oficial (OBP) de ISO [1,2], y de fuentes técnicas públicas [3–18]. No reproduce texto protegido de la norma: los requisitos se parafrasean y se remite a la fuente oficial para su consulta. Las decisiones de alcance adoptadas se consignan en la Tabla 1.

Tabla 1. Decisiones de alcance y desarrollo del digesto.

| No. | Decisión | Justificación | Dónde se desarrolla |
|---|---|---|---|
| 1 | Parafrasear los requisitos y remitir a la OBP oficial; no reproducir texto protegido de la norma | Propiedad intelectual de ISO [1,2] | Todo el documento |
| 2 | Desarrollar explícitamente la cláusula 8.1.2 (eliminación de peligros y jerarquía de controles) | Núcleo técnico auditable de la aplicación al diseño [15,16,17,18] | Secciones 4.5 y 5; Tabla 4 |
| 3 | Desarrollar explícitamente la cláusula 8.2 (preparación y respuesta ante emergencias) | Vínculo directo con NFPA 15, drenajes de emergencia y sistemas de alivio | Sección 4.8 |
| 4 | Desarrollar explícitamente la cláusula 5.4 (participación y consulta de los trabajadores) | Requisito de registro de participación en actas de revisión [4] | Sección 4.2 |
| 5 | Incluir el marco legal colombiano (Decreto 1072 de 2015, Resolución 0312 de 2019) | Marco donde los entregables sirven como evidencia del SG-SST [7,8,9] | Sección 3.3 |
| 6 | Usar la sigla MDP/MDT para diseño a presión | Sigla correcta y coherente con ASME VIII y API 650 | Todo el documento |

## 3. Contexto normativo

### 3.1 Estructura de ISO 45001:2018

ISO 45001:2018 especifica los requisitos de un sistema de gestión de seguridad y salud en el trabajo (SST) y se estructura en diez cláusulas: 1 Alcance, 2 Referencias normativas, 3 Términos y definiciones, y 4–10 los requisitos evaluables (contexto de la organización, liderazgo y participación de los trabajadores, planificación, apoyo, operación, evaluación del desempeño y mejora) [1]. El marco sigue el ciclo PDCA (planificar-hacer-verificar-actuar) de la estructura de alto nivel común a las normas ISO de sistemas de gestión [1]. Para efectos de diseño de ingeniería, la cláusula 8.1.2 obliga a aplicar la jerarquía de controles en orden estricto: eliminación, sustitución, controles de ingeniería y reorganización del trabajo, controles administrativos (incluida la formación), y equipos de protección personal (EPP) como última barrera [15,16,17,18].

### 3.2 Prevención mediante el diseño (Prevention through Design, PtD)

La iniciativa nacional PtD del NIOSH, lanzada en 2007, sostiene que la forma más eficaz de prevenir lesiones y enfermedades laborales es eliminar los peligros y minimizar los riesgos **durante el diseño o rediseño** de instalaciones, procesos, equipos y métodos de trabajo, en lugar de añadir controles retroactivos [3,5,6]. El modelo se apoya en la jerarquía de controles, priorizando la eliminación y la sustitución, y en revisiones de seguridad del diseño realizadas por equipos multidisciplinarios que incluyen a operadores y mantenedores experimentados; el estándar ANSI/ASSP Z590.3 aporta herramientas para ese proceso [4]. La evidencia reporta que el diseño es contribuyente significativo en una fracción sustancial de las fatalidades laborales: un estudio australiano lo identificó en el 37 % de los casos [3]. La capacidad de influir sobre la seguridad es máxima en las etapas iniciales del proyecto y cae abruptamente a medida que el diseño avanza [5]; este principio justifica que la plantilla JAGDESING integre la SST desde `bases_diseno.yaml` y no como revisión final.

### 3.3 Marco legal colombiano

En Colombia, el Sistema de Gestión de Seguridad y Salud en el Trabajo (SG-SST) se reglamenta en el Capítulo 2.2.4.6 del Decreto 1072 de 2015 (Decreto Único Reglamentario del Sector Trabajo), con 42 artículos que desarrollan política, organización, planificación, ejecución, verificación y mejora [8,9]. La Resolución 0312 de 2019 del Ministerio del Trabajo define los estándares mínimos del SG-SST, graduados por número de trabajadores y nivel de riesgo, con autoevaluación documentada y plan de mejoramiento [7]. La estructura del SG-SST colombiano es coherente con el ciclo de mejora continua de ISO 45001, por lo que los entregables de ingeniería de este digesto sirven simultáneamente como evidencia para certificación ISO 45001 y para evaluación de estándares mínimos ante el Ministerio del Trabajo y las ARL [7,8,9]. Todo proyecto JAGDESING ejecutado en Colombia debe declarar en `bases_diseno.yaml` el cumplimiento aplicable de este marco.

### 3.4 Normas y guías técnicas complementarias

Tabla 2. Marco técnico complementario aplicable al diseño con criterio SST.

| Referencia | Rol en el diseño JAGDESING |
|---|---|
| ISO 45001:2018 [1] | Sistema de gestión SST; requisitos cláusulas 4–10 |
| ISO 31000 | Gestión del riesgo; criterios de aceptación |
| ANSI/ASSP Z590.3 [4] | Prevención mediante el diseño; revisiones de seguridad del diseño |
| CCPS — Guidelines for Hazard Evaluation Procedures [10] | HAZID, What-if, HAZOP por etapa |
| CCPS — LOPA [11,12] | Asignación semicuantitativa de capas de protección; determinación de SIL |
| IEC 61511 [13,14] | Ciclo de vida de seguridad funcional; SIS, SIF, SIL, verificación y pruebas periódicas |
| API RP 750/751/752/753 | Gestión de atmósferas peligrosas, HF, ubicación de edificaciones |
| NFPA 15 / NFPA 400 | Sistemas fijos de protección por agua; materiales sólidos oxidantes y piróforos |
| ASME VIII / API 650 / API 620 | Diseño mecánico a presión (MDP/MDT) y almacenamiento |
| Decreto 1072 de 2015 [8,9] | SG-SST Colombia; gestión del cambio; investigación de incidentes |
| Resolución 0312 de 2019 [7] | Estándares mínimos SG-SST; indicadores de SST |

## 4. Mapeo cláusula ISO 45001 ↔ artefactos de la plantilla JAGDESING

La Tabla 3 es el núcleo operativo de este digesto: cada cláusula evaluable de ISO 45001:2018 se traduce en acciones concretas y artefactos nombrables de la plantilla. Todo proyecto derivado debe poder demostrar, fila por fila, dónde vive cada evidencia.

Tabla 3. Mapeo entre cláusulas 4–10 de ISO 45001:2018 y los artefactos de la plantilla JAGDESING.

| Cláusula ISO 45001 | Requisito (parafraseado) [1] | Artefacto JAGDESING que genera la evidencia |
|---|---|---|
| 4.1–4.3 | Contexto de la organización, partes interesadas, alcance del sistema | Sección «Alcance» del informe (`02_informe_tex/sections/`); contexto del cliente en `00_bases_diseno/bases_diseno.yaml` |
| 5.1 | Liderazgo y compromiso de la alta dirección | Acta de aprobación de decisiones de diseño con impacto SST (registro en `07_comunicaciones/`); compromiso documentado en el acta de apertura del proyecto |
| 5.2 | Política de SST | Referencia de la política del cliente en el informe; coherencia de objetivos de diseño con la política |
| 5.3 | Roles, responsabilidades y autoridades | Matriz de responsabilidades del proyecto (plan en `task/todo.md`); designación del responsable SST por etapa |
| 5.4 | Participación y consulta de los trabajadores | Actas de HAZOP/HAZID con participación registrada de operación y mantenimiento [4]; constancias en la memoria de revisión |
| 6.1.2 | Identificación de peligros | Matriz de identificación de peligros por etapa (conceptual, FEED, básico, detalle) — plantilla en la Sección 7; insumo desde `bases_diseno.yaml` |
| 6.1.2 | Evaluación de riesgos y oportunidades | Matriz de riesgos con criterios de aceptación; LOPA para escenarios mayores [11,12]; registro de acciones en `task/todo.md` |
| 6.1.3 | Requisitos legales y otros | Sección de normativa aplicable del informe; para Colombia: Decreto 1072 y Res. 0312 [7,8,9]; registro en `bases_diseno.yaml` |
| 6.2 | Objetivos de SST y planificación | Objetivos medibles integrados a hitos del proyecto (ej.: reducir puntos de fuga potencial antes de FEED); seguimiento en revisiones de `task/todo.md` |
| 7.2 | Competencia | Matriz de competencias del equipo de revisión; registros HAZOP/LOPA con roles; requisitos en plan del proyecto |
| 7.3 | Toma de conciencia | Comunicación de riesgos y restricciones a operación/mantenimiento en entregables (datasheets, P&ID) |
| 7.4 | Comunicación | Actas, minutas HSE-ingeniería (`07_comunicaciones/`); transmittals |
| 7.5 | Información documentada | **Sistema completo de la plantilla**: códigos guía de codificación del proyecto, `listado_documentos.csv`, control de revisiones [19] |
| 8.1.1 | Planificación y control operacional | Diseño «con controles incorporados», no solo procedimental: bandejas de contención, drenaje cerrado, acoples con contención (Sección 5) |
| 8.1.2 | Eliminación de peligros; jerarquía de controles | Justificación documentada por decisión de diseño (Tabla 4); memoria MC-XXX con sección «Impacto SST» |
| 8.1.3 | Gestión del cambio (MOC/ECR) | Procedimiento de control de cambios con evaluación de impacto SST; checklist MOC (Sección 7) |
| 8.1.4 | Compras, contratistas y externalización | Especificaciones de compra con requisitos SST; evaluación de contratistas (art. 2.2.4.6.4 Decreto 1072 [8]) |
| 8.2 | Preparación y respuesta ante emergencias | Diseño de sistemas de alivio, drenajes de emergencia, NFPA 15; escenarios de emergencia en HAZOP; plan de respuesta referenciado en el informe |
| 9.1 | Seguimiento, medición, análisis | Verificación de eficacia de salvaguardas (cálculos PSV, SIL verification [13,14]); indicadores de diseño |
| 9.2 | Auditoría interna | Checklist de auditoría de diseño SST (Sección 7) ejecutado por etapa |
| 9.3 | Revisión por la dirección | Cierre de etapa con revisión de acciones abiertas; acta en `07_comunicaciones/` |
| 10 | Mejora | Acciones correctivas de auditorías; lecciones aprendidas en `memoria/lecciones/` propagadas a la plantilla |

### 4.1 Cláusulas 4 — Contexto de la organización

El diseño no ocurre en vacío. El informe JAGDESING declara el alcance del sistema SST aplicable al proyecto (qué instalaciones, qué modos operativos, qué partes interesadas: operadores, contratistas, comunidad, autoridad laboral) y lo congrida con el contexto del cliente. En `bases_diseno.yaml` se registra la normativa legal aplicable por jurisdicción; para Colombia, el capítulo 2.2.4.6 del Decreto 1072 de 2015 y la Resolución 0312 de 2019 [7,8,9].

### 4.2 Cláusula 5 — Liderazgo y participación de los trabajadores

Toda decisión de diseño con impacto SST (sustitución de contención, reducción de especificación de material, simplificación de instrumentación) requiere minuta de revisión HSE-ingeniería con justificación técnica y matriz costo-riesgo. La cláusula 5.4 exige participación y consulta: las revisiones HAZOP/HAZID deben registrar asistencia de operación y mantenimiento, cuya experiencia operativa es fuente primaria de identificación de peligros [4]. La plantilla exige que toda acta de estas sesiones conste en el Listado de Documentos del Proyecto.

### 4.3 Cláusula 6 — Planificación

La identificación de peligros se ejecuta por etapa con la profundidad que la complejidad exige: HAZID o What-if en etapa conceptual; HAZOP en diseño básico; LOPA para escenarios de consecuencia mayor [10,11,12]. Los resultados se traducen en requisitos de ingeniería trazables: contención primaria y secundaria, segregación por incompatibilidad química, ventilación localizada, zonificación ATEX, distancias y pantallas. Los objetivos de SST son medibles y se integran a los hitos del plan del proyecto (ejemplo de objetivo medible: reducir en 50 % los puntos de potencial fuga antes de FEED mediante selección de rutas y juntas aprobadas).

### 4.4 Cláusula 7 — Apoyo

La competencia del equipo de revisión se demuestra con matriz de competencias y registros de asistencia metodológica (HAZOP, LOPA, bow-tie). La comunicación se materializa en datasheets, P&ID y layouts que comunican riesgos y restricciones al personal de operación y mantenimiento. La información documentada es un punto fuerte natural de la plantilla: el sistema de codificación guía de codificación del proyecto y el `listado_documentos.csv` [19] proporcionan el control documental que la cláusula 7.5 exige.

### 4.5 Cláusula 8.1 — Planificación y control operacional

El principio rector es que el control operacional se **diseña**, no se delega exclusivamente a procedimientos: bandejas de contención con drenaje cerrado, puntos de conexión que minimizan maniobras manuales, doble contención en servicios tóxicos, instrumentación de seguridad con independencia del BPCS conforme a IEC 61511 [13,14]. El diseño JAGDESING documenta cada barrera con tipo, ubicación y requisitos de mantenimiento.

### 4.6 Cláusula 8.1.3 — Gestión del cambio

Todo cambio de diseño (ECR/MOC), temporal o permanente, se evalúa por su impacto en SST antes de su implementación [16]. La plantilla exige que el registro del cambio vincule la acción a los documentos afectados (P&ID, especificaciones, cálculos) y cierre con verificación.

### 4.7 Cláusula 8.1.4 — Compras y contratistas

Las especificaciones de compra incorporan requisitos SST (certificaciones ATEX, materiales, pruebas). La gestión de contratistas sigue el artículo 2.2.4.6.4 del Decreto 1072 de 2015: verificación previa del SG-SST del contratista, afiliación a ARL e inducción [8].

### 4.8 Cláusulas 8.2, 9 y 10 — Emergencias, evaluación y mejora

La preparación ante emergencias se traduce en diseño: sistemas de alivio dimensionados y verificados, drenajes de emergencia, protección fija por agua conforme a NFPA 15, escenarios de emergencia analizados en HAZOP. La evaluación del desempeño exige verificación de eficacia de salvaguardas: cálculo y datasheet de PSV, SIL verification de funciones instrumentadas [13,14], plan de inspección y prueba. La mejora alimenta `memoria/lecciones/` de la plantilla, cerrando el ciclo PDCA [1].

## 5. Jerarquía de controles aplicada al diseño de procesos fisicoquímicos

La cláusula 8.1.2 de ISO 45001:2018 exige establecer, implementar y mantener un proceso de eliminación de peligros y reducción de riesgos siguiendo la jerarquía de controles en orden de preferencia: eliminación, sustitución, controles de ingeniería y reorganización del trabajo, controles administrativos incluida la formación, y EPP [15,16,17,18]. La razón del orden es de confiabilidad: cuanto más cerca del origen del peligro actúa el control, menos depende del comportamiento humano; el EPP es la barrera más propensa a fallar y nunca sustituye a los niveles superiores [16,17]. La Tabla 4 traduce cada nivel a decisiones concretas de ingeniería de procesos y al artefacto JAGDESING donde se documenta la decisión.

Tabla 4. Jerarquía de controles de ISO 45001:2018 (cláusula 8.1.2) traducida a decisiones de diseño de procesos fisicoquímicos.

| Nivel | Definición [1,18] | Decisiones de diseño típicas | Artefacto JAGDESING de evidencia |
|---|---|---|---|
| 1. Eliminación | Retirar el peligro por completo | Eliminar inventario de sustancia tóxica (just-in-time, almacenamiento mínimo); eliminar transferencias manuales; evitar servicios criogénicos si el proceso lo permite | Memoria MC-XXX «Impacto SST»; balance de masa en `01_calculos/` |
| 2. Sustitución | Reemplazar por procesos, operaciones, materiales o equipos menos peligrosos | Solvente de menor toxicidad; bomba hermética (mag-drive) en vez de bomba con sello mecánico; junta soldada en vez de brida para servicio fuga-prone | Comparativo en memoria; especificación de equipo; MOC si aplica |
| 3. Controles de ingeniería y reorganización del trabajo | Aislar a las personas del peligro | Doble contención; ventilación localizada; bandejas y drenaje cerrado; zonificación ATEX con equipos certificados; pantallas y distancias de seguridad; acoples rápidos con contención; instrumentación de seguridad (SIS) según IEC 61511 [13,14] | P&ID y layouts SVG; layout con zonas de riesgo; cálculo de PSV; SRS/SIL verification |
| 4. Controles administrativos, incluida la formación | Procedimientos, señalización, permisos, competencia | Procedimientos de transferencia; permisos de trabajo; señalización de líneas; matrices de compatibilidad química en `bases_diseno.yaml` | Sección de procedimientos del informe; actas de capacitación (cliente) |
| 5. EPP | Equipo de protección personal adecuado | Definición de EPP por tarea en transferencia, muestreo y mantenimiento | Recomendación al cliente en el informe (el EPP se gestiona en operación, fuera del alcance del diseño) |

Regla de auditoría JAGDESING: toda memoria de cálculo que toque un peligro identificado debe contener una tabla de decisión que recorra la jerarquía de arriba hacia abajo y justifique por escrito por qué los niveles superiores no fueron razonablemente practicables antes de aceptar controles de niveles inferiores [16,17].

## 6. Casos prácticos y verificación

Los tres casos prácticos siguientes se desarrollan con el marco técnico de las Secciones 3–5. Todo caso debe cerrar con evidencia documental registrada en el Listado de Documentos del Proyecto.

### 6.1 Caso A — Reactor con riesgo de fuga de gases tóxicos

El peligro es la liberación de gas tóxico por falla de sello o sobrepresión. La jerarquía de controles se aplica así: eliminación mediante reducción del inventario de gas disponible; sustitución mediante sello doble o compresor hermético; controles de ingeniería mediante doble contención con captura o recuperación, interlock de alta presión con acción a estado seguro, y PSV dimensionada y verificada; controles administrativos mediante procedimiento de prueba de sellos; EPP como complemento. Evidencias: P&ID con instrumentación y válvulas, revisión LOPA si el escenario lo exige [11,12], plan de inspección de sellos y liners, cálculo y datasheet de PSV, SRS con SIL asignado según IEC 61511 cuando el SIS toma crédito [13,14].

### 6.2 Caso B — Líneas criogénicas

El peligro es la rotura frágil, el congelamiento de materiales y la exposición por derrame de fluido criogénico. Decisiones de diseño: selección de materiales con suficiencia de tenacidad a la temperatura de servicio (coherente con ASME VIII y requisitos de impacto), pantallas y distancias de seguridad, detección de fugas y ventilación de áreas confinadas, límites de operación declarados (MDP/MDT). Evidencias: especificación de materiales, layout con zonas de riesgo, memoria térmica, actas de revisión con priorización documentada de la seguridad sobre el costo (cláusula 5.1) [1].

### 6.3 Caso C — Sistema de carga y descarga

El peligro es la exposición por conexiones manuales y derrame en mangueras. Decisiones de diseño: acoples rápidos con contención de gotas, bandejas de contención con drenaje cerrado, altura y posicionamiento de estaciones para minimizar posturas y esfuerzos (ergonomía en layout), reducción del número de conexiones. Evidencias: layout con criterio ergonómico, especificación del sistema de drenaje cerrado, registro de revisión HSE del diseño.

## 7. Entregables, checklist y plantillas de auditoría

### 7.1 Entregables típicos de SST en un proyecto JAGDESING

Todo entregable se codifica según guía de codificación del proyecto y se registra en `06_entregables/listado_documentos.csv` [19]. Tabla 5 lista el catálogo mínimo.

Tabla 5. Catálogo de entregables de SST para auditoría.

| No. | Entregable | Contenido mínimo | Momento del proyecto |
|---|---|---|---|
| 1 | Matriz de identificación de peligros por etapa | Peligro, actividad de diseño asociada, riesgo, control propuesto, evidencia | Cierre de cada etapa |
| 2 | Acta de HAZID/What-if/HAZOP | Desviaciones, escenarios, recomendaciones, responsables, plazo, estado | Diseño básico |
| 3 | Matriz de trazabilidad Peligro–Diseño–Control–Documento | Vínculo de cada requisito SST a P&ID, layout, especificación y memoria | FEED y detalle |
| 4 | Registro LOPA y determinación de SIL | Escenarios, frecuencia iniciadora, IPLs, PFD, SIL objetivo | Diseño básico [11,12,13] |
| 5 | Plan de verificación de salvaguardas | Criterios de aceptación, métodos de verificación (cálculo, prueba), responsables | Detalle |
| 6 | Checklist MOC por impacto SST | Cambio, evaluación de impacto, aprobación, documentos afectados | Continuo |
| 7 | Matriz de competencias del equipo de revisión | Roles, formación, experiencia | Inicio |

### 7.2 Checklist de auditoría de diseño SST

Tabla 6. Checklist de auditoría de diseño con criterio SST (criterios ordenados por cláusula ISO 45001).

| No. | Criterio | Cláusula ISO 45001 |
|---|---|---|
| 1 | Se realizó identificación de peligros por etapa y se documentó | 6.1.2 |
| 2 | Se aplicaron metodologías acordes a la complejidad (HAZID/What-if/HAZOP) | 6.1.2 [10] |
| 3 | Existe trazabilidad de acciones a P&ID, planos y especificaciones | 6.1.2, 7.5 |
| 4 | Los cambios (MOC/ECR) se evaluaron por impacto SST | 8.1.3 |
| 5 | Las salvaguardas tienen criterios de aceptación y verificación definidos | 9.1 |
| 6 | Las barreras de diseño están especificadas con tipo, ubicación y mantenimiento | 8.1.1, 8.1.2 |
| 7 | Los equipos críticos tienen requisitos de integridad mecánica e inspección | 8.1.1 |
| 8 | La instrumentación de seguridad tiene documentación e independencia del BPCS | 8.1.2 [13,14] |
| 9 | Se evaluaron escenarios de emergencia y los sistemas de respuesta están dimensionados | 8.2 |
| 10 | Operación y mantenimiento participaron en las revisiones | 5.4 [4] |
| 11 | El equipo de revisión acredita competencia metodológica | 7.2 |
| 12 | Los riesgos se comunicaron a operación y mantenimiento en los entregables | 7.3, 7.4 |
| 13 | Se documentó la justificación de la jerarquía de controles aplicada | 8.1.2 |
| 14 | Se verificó la eficacia de salvaguardas (cálculo PSV, SIL verification) | 9.1 [13,14] |

### 7.3 Plantilla de matriz Peligro–Diseño–Control–Verificación

Tabla 7. Formato estándar de matriz de trazabilidad (una fila por peligro identificado).

| Peligro | Fuente | Etapa de diseño | Control de diseño (con nivel de jerarquía, Tabla 4) | Responsable | Evidencia (código de documento) | Verificación (método y fecha) |
|---|---|---|---|---|---|---|
| *(ej.: exposición a vapores tóxicos)* | *(ej.: bomba P-101)* | *(ej.: diseño básico)* | *(ej.: sello doble, nivel 3)* | *(rol)* | *(código guía de codificación del proyecto)* | *(cálculo / prueba)* |

### 7.4 Formato de registro de revisión HAZOP/What-if

Tabla 8. Campos mínimos del registro de sesión.

| Campo | Contenido |
|---|---|
| Proyecto / Fecha | Código JAGDESING y fecha de sesión |
| Equipo participante | Incluye obligatoriamente HSE, instrumentación e integridad mecánica, y operación/mantenimiento del cliente |
| Metodología | HAZID, What-if o HAZOP (guidewords) |
| Secciones revisadas | Nodos o sistemas |
| Desviaciones / escenarios | Causa, consecuencia, salvaguardas existentes |
| Recomendaciones | Acción, responsable, plazo |
| Estado | Abierto / cerrado |
| Evidencia documental | Código(s) de documento en el Listado |

## 8. Cómo citar ISO 45001 en el informe LaTeX de la plantilla

Todo informe JAGDESING (`02_informe_tex/`) que toque decisiones con impacto SST debe: declarar ISO 45001:2018 en la sección de normativa aplicable junto al marco legal colombiano cuando aplique (Decreto 1072 de 2015, Resolución 0312 de 2019) [7,8,9]; incluir una subsección «Seguridad y salud en el diseño» dentro de Metodología o Discusión que recorra la Tabla 4 para los peligros relevantes del proyecto; y referenciar los entregables de la Tabla 5 por su código de documento guía de codificación del proyecto [19]. Ejemplo de redacción lista para adaptar:

> «El diseño se desarrolló bajo los requisitos de ISO 45001:2018 [ref], aplicando la jerarquía de controles de su cláusula 8.1.2. Los peligros identificados y los controles de diseño adoptados se documentan en la matriz Peligro–Diseño–Control–Verificación [código guía de codificación del proyecto], y la eficacia de las salvaguardas se verificó conforme a IEC 61511 [ref]. Para Colombia, los entregables sirven como evidencia del SG-SST del titular ante los estándares mínimos de la Resolución 0312 de 2019 [ref].»

## 9. Conclusiones

Primero, ISO 45001:2018 se aplica al diseño de procesos fisicoquímicos mediante la integración de la SST en cada decisión de ingeniería, no como capa documental final; la capacidad de influir es máxima en etapas tempranas [5]. Segundo, la cláusula 8.1.2 convierte la jerarquía de controles en regla de diseño auditable: eliminar y sustituir antes que confiar en procedimientos y EPP [15,16,17,18]. Tercero, la plantilla JAGDESING ya posee el esqueleto de trazabilidad que la norma exige (fuente única en YAML, memorias versionadas, códigos guía de codificación del proyecto, Listado de Documentos); este digesto define el contenido SST que debe fluir por ese esqueleto. Cuarto, en Colombia los mismos entregables sirven doble propósito: certificación ISO 45001 y evaluación de estándares mínimos del SG-SST [7,8,9]. Quinto, la trazabilidad completa exige que toda memoria que toque un peligro justifique por escrito el nivel de jerarquía de controles adoptado y que toda salvaguarda cuente con método de verificación; ambos criterios quedan operativos en las Secciones 5 y 7.

## Referencias

[1] ISO. *ISO 45001:2018(en), Occupational health and safety management systems — Requirements with guidance for use*. Plataforma de Bolsillo Oficial (OBP). https://www.iso.org/obp/ui/en/#!iso:std:63787:en (consulta: 25/09/2026).

[2] ISO. *ISO 45001:2018(es), Sistemas de gestión de la seguridad y salud en el trabajo — Requisitos con guía de uso*. OBP, vista en español. https://www.iso.org/obp/ui/es/#iso:std:iso:45001:ed-1:v1:e (consulta: 25/09/2026).

[3] NIOSH. *Prevention through Design Plan for the National Initiative* (DHHS NIOSH Publication 2011-121). https://www.cdc.gov/niosh/docs/2011-121/pdfs/2011-121.pdf (consulta: 25/09/2026).

[4] CDC/NIOSH. *Prevention through Design (PtD) Award — priorities and process; referencia al estándar ANSI/ASSP Z590.3*. https://www.cdc.gov/niosh/ptd/awards/index.html (consulta: 25/09/2026).

[5] NIOSH. Capítulo 2.4 «Manage occupational safety and health risks» (jerarquía de controles; curva de influencia del diseño adaptada de Szymberski, 1997). https://stacks.cdc.gov/view/cdc/201516/cdc_201516_DS1.pdf (consulta: 25/09/2026).

[6] NIOSH Science Blog. *Prevention through Design to Address Continuing Construction Workplace Deaths and Injuries*. https://www.cdc.gov/niosh/blogs/2024/ptd-construction.html (consulta: 25/09/2026).

[7] Ministerio del Trabajo de Colombia (compilación SafetyA). *Resolución 0312 de 2019 — Estándares Mínimos del SG-SST*. https://safetya.co/normatividad/resolucion-0312-de-2019/ (consulta: 25/09/2026).

[8] De Seguridad. *Decreto 1072 de 2015, SG-SST en Colombia — estructura del Capítulo 2.2.4.6 (arts. 2.2.4.6.9–2.2.4.6.14)*. https://deseguridad.net/decreto-1072-de-2015-sgsst-colombia-2026/ (consulta: 25/09/2026).

[9] Sabentis. *Decreto 1072 de 2015 (Colombia) — qué es y marco normativo (Ley 1562 de 2012, Decreto 1443 de 2014, Resolución 0312 de 2019)*. https://www.sabentis.com/explora/decreto-1072-de-2015-colombia/ (consulta: 25/09/2026).

[10] University of Michigan, SAFEChE Process Safety. *Layers of Protection (LOPA) — tutorial*. https://safeche.engin.umich.edu/tutorials/lopa-tutorial/ (consulta: 25/09/2026).

[11] Kim, Y., Han, S., Song, H., Jung, S. (2025). *Risk Assessment of an Off-Site Hydrogen Refueling Station: A Hybrid IEC 61511-CCPS LOPA Framework*. Energies, 18(23), 6242. https://www.mdpi.com/1996-1073/18/23/6242. DOI: 10.3390/en18236242 (consulta: 25/09/2026).

[12] SILSafe. *LOPA: Layer of Protection Analysis Explained — ecuación de frecuencia mitigada; LOPA incorporada en IEC 61511-3 Anexo F*. https://silsafe.net/layer-of-protection-analysis-lopa/ (consulta: 25/09/2026).

[13] Mangan Software. *What Is IEC 61511? Functional Safety Standard Explained*. https://mangansoftware.com/docs/iec-61511/ (consulta: 25/09/2026).

[14] Tagsight. *What is IEC 61511? Functional safety standard for process industries (ed. 2016; armonización ANSI/ISA 84)*. https://tagsight.io/learn/what-is-iec-61511 (consulta: 25/09/2026).

[15] AI4HSE. *ISO 45001 Clause 8 — Operation* (estructura 8.1.1–8.1.4 y 8.2; evidencias de auditoría). https://ai4hse.com/iso-45001/clauses/operation (consulta: 25/09/2026).

[16] Igera Solutions. *ISO 45001 Clause 8: Operational Planning and Control* (orden de la jerarquía de controles; MOC temporal y permanente). https://igerasolutions.com/en/blog/iso-45001-clause-8-operational-planning-control (consulta: 25/09/2026).

[17] ISO Certification Group. *Clause 8.1.2 — ISO 45001 Eliminating Hazards and Reducing Risks*. https://isocertificationgroup.com.au/resources/clause-8-1-2-iso-45001-eliminating-hazards-and-reducing-risks/ (consulta: 25/09/2026).

[18] Auditor Training Online. *ISO 45001 Clause 8.1.2 Eliminating hazards and reducing OH&S risks* (texto del requisito a)–e) y jerarquía). https://blog.auditortrainingonline.com/blog/iso-45001-clause-8-1-2 (consulta: 25/09/2026).

[19] JAGDESING. *guía de codificación del proyecto — Norma de documentación de proyectos*; digesto operativo en `Plantilla/08_codificacion/codificacion.md` (código `WyyxxEETTTNNN`; Listado de Documentos). Documento interno, 2026.
