# Guía de codificación del proyecto W2608

## Autoridad y alcance

Convención local establecida por las instrucciones expresas del usuario durante la inicialización del proyecto. Aplica a informes, ofertas, memorias, planos, presentaciones y demás documentos emitidos para JGB. El proponente es J.Arboleda, con identidad gráfica JAGDESING.

## Código compacto

El código concatena los segmentos sin guiones, espacios ni otros separadores:

```
WyyxxEETTTNNN
W2608PRINF001
```

| Segmento | Contenido |
|---|---|
| Wyyxx | Prefijo W, dos dígitos del año y dos del proyecto; en este proyecto: W2608 |
| EE | Dos letras de especialidad |
| TTT | Tipo de documento de uno a tres caracteres, según tabla |
| NNN | Consecutivo de tres dígitos, independiente por especialidad y tipo |

El código de proyecto W2608 queda congelado. El consecutivo ocupa los tres últimos dígitos. Se utilizan mayúsculas. El validador rechaza los códigos con prefijo P y los códigos con separadores.

| Ejemplo | Lectura |
|---|---|
| W2608PRINF001 | Informe de proceso, consecutivo 001 |
| W2608PRCAL001 | Memoria de cálculo de proceso, consecutivo 001 |
| W2608TUPLN001 | Plano de tubería, consecutivo 001 |
| W2608PRM3D001 | Modelo 3D de proceso, consecutivo 001 |

Los ejemplos explican la forma del código y no implican documentos emitidos ni consecutivos reservados. El código de la oferta se definirá según su tipo y alcance antes de la emisión.

## Tablas de especialidad y tipo

### Tabla A — Especialidad → sigla (2 letras)

| Especialidad | Sigla |
|---|---|
| Dirección | DI |
| Proceso | PR |
| Civil | CI |
| Mecánica | ME |
| Estructura | ES |
| Tubería | TU |
| Eléctrica | EL |
| Instrumentación y control | IC |
| Contraincendios | SC |
| Aire Acondicionado | HV |

### Tabla B — Tipo de documento → sigla → sub-carpeta

| Tipo de documento | Sigla | Sub-carpeta guía de codificación del proyecto |
|---|---|---|
| Actas | ACT | ADMINISTRATIVOS |
| Correspondencia | TR | ADMINISTRATIVOS |
| Cronograma | CRO | ADMINISTRATIVOS |
| Organigrama | ORG | ADMINISTRATIVOS |
| Presentación | PRE | ADMINISTRATIVOS |
| Informe | INF | INFORMES |
| Hoja de datos de equipo o instrumento | DTS | HOJAS DE DATOS |
| Requerimiento de Cotización | RFQ | DOCUMENTOS TÉCNICOS |
| Documento técnico | DOC | DOCUMENTOS TÉCNICOS |
| Especificación | ESP | ESPECIFICACIONES |
| Memoria de cálculo | CAL | MEMORIAS DE CÁLCULO |
| Modelo 3D | M3D | MEMORIAS DE CÁLCULO |
| Nube de puntos | PCL | MEMORIAS DE CÁLCULO |
| Isométrico | ISO | PLANOS |
| Plano, LayOut, PFD, PID | PLN | PLANOS |
| Listado | LIS | LISTADOS |
| Análisis de precios unitarios | APU | PRESUPUESTO |
| Presupuesto | PTO | PRESUPUESTO |
| Volumen de obra | VO | PRESUPUESTO |


## Revisión, fecha y firmas

La revisión inicial es 0. Solo la última revisión aprobada y registrada es vigente. Las fechas se expresan como dd/mm/aaaa. La fecha de preparación de un borrador no se presenta como fecha de aprobación. Las firmas emitidas siguen el formato X.Y.APELLIDO; la autoría de trabajo se conserva como J.Arboleda por instrucción del usuario. No se asignan revisores ni aprobadores no confirmados.

## Archivos y emisión

El nombre recomendado es `WyyxxEETTTNNN_Rev<n>_titulo-breve.ext`. El código se conserva íntegro y sin guiones. El título descriptivo puede utilizar guiones. El maestro LaTeX puede llamarse `W2608PRINF001 Rev0.tex`, y su metadato documentcode debe coincidir con el código.

Los borradores internos se alojan en `task/borradores_internos/`. La información y los archivos de preparación de la oferta se reúnen en `1.0 Oferta/`. Los documentos finales emitidos se controlan desde `06_entregables/REV<n>/`, con su fila en `06_entregables/listado_documentos.csv`.

## Verificación antes de emitir

1. Confirmar el código de proyecto, la especialidad, el tipo y el consecutivo disponible.
2. Ejecutar `python 08_codificacion/validar_codigo.py W2608PRINF001` usando el código correspondiente al documento real.
3. Verificar coherencia del código en el archivo, metadatos, encabezado y listado.
4. Revisar contenido técnico, revisión, fecha, autor, firmas, cliente y logo personal.
5. Registrar el documento y su estado en el listado y ubicar la emisión en la carpeta de revisión.

## Fuente de las reglas

Las instrucciones del usuario establecen W2608, el cambio de prefijo a WXXXX, la concatenación de segmentos sin guiones, JGB como empresa objeto del estudio y la autoría personal. Las tablas de especialidad y tipo proceden de la estructura de trabajo heredada y se adoptan como convención local. Este archivo es la autoridad operativa de codificación del proyecto; no se conserva dentro del proyecto una norma corporativa de otra entidad.
