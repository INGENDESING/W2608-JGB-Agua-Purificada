/* ==========================================================================
   W2608 — Lógica Interactiva del Portal Técnico de Ingeniería (JGB, Cali)
   Contenido 100 % técnico, normativo y de entregables (sin datos comerciales)
   ========================================================================== */

const LOOP_DETAILS = {
  tanque: {
    title: "Tanque Pulmón Común de 3.000 L",
    unidades: "Incidencia transversal en unidades 01, 08, 15 y 22",
    memoria: "Interfaces comunes en W2608PRCAL001 a W2608PRCAL004",
    desc: "Almacenamiento intermedio y alimentación común del sistema de agua purificada. La revisión de sus reportes de videoscopia y líquidos penetrantes se ejecuta una sola vez y sus efectos sanitarios e hidráulicos se vinculan trazablemente con cada uno de los cuatro anillos."
  },
  farma: {
    title: "Anillo de Distribución Farma",
    unidades: "Unidades de análisis 01 a 07",
    memoria: "W2608PRCAL001 (Semana 4)",
    desc: "Red de distribución asociada a operaciones farmacéuticas. Evaluación bajo Resolución MSPS 1160 de 2016 (modificada por 2190 de 2020), OMS TRS 1033 Anexo 3, USP-NF y criterios de ingeniería higiénica ASME BPE-2026 / 3-A."
  },
  cosmeticos: {
    title: "Anillo de Distribución Cosméticos",
    unidades: "Unidades de análisis 08 a 14",
    memoria: "W2608PRCAL002 (Semana 4)",
    desc: "Red de distribución para fabricación cosmética. Contraste técnico con Resolución Andina CAN 2206 de 2021 (numerales 12.8.1–12.8.4), lista de verificación CAN 2214 de 2021 (ítems 77–80) e ISO 22716:2007."
  },
  suplementos: {
    title: "Anillo de Distribución Suplementos",
    unidades: "Unidades de análisis 15 a 21",
    memoria: "W2608PRCAL003 (Semana 4)",
    desc: "Red de distribución vinculada a la línea de suplementos dietarios. Evaluación conforme al Decreto 3249 de 2006 (anexo 1, numeral 5.1, según categoría aplicable), diseño sanitario y comportamiento hidrodinámico."
  },
  pw: {
    title: "Anillo de Distribución PW (Agua Purificada)",
    unidades: "Unidades de análisis 22 a 28",
    memoria: "W2608PRCAL004 (Semana 4)",
    desc: "Anillo de agua purificada e interconexiones con el sistema de generación y almacenamiento. Modelado de caudales, presiones, velocidades, pérdidas de carga y verificación de puntos muertos."
  }
};

const EVALUACIONES_MATRIZ = [
  {
    num: 1,
    informe: "W2608PRINF001",
    semana: "Semana 4",
    titulo: "Interpretación de videoscopia y tintas penetrantes",
    detalle: "Revisión técnica de los informes de ensayo suministrados sobre el tanque pulmón de 3.000 L y zonas inspeccionadas, localización de indicaciones, limitaciones de evidencia y análisis de su incidencia sanitaria y operativa en cada anillo.",
    unidades: { farma: "01", cosmeticos: "08", suplementos: "15", pw: "22" }
  },
  {
    num: 2,
    informe: "W2608PRINF002",
    semana: "Semana 4",
    titulo: "Inspección en campo y levantamiento físico",
    detalle: "Contraste de la instalación existente con los planos suministrados (17-PT-A-G-0017 y 18-PT-A-G-0018), identificación de líneas, válvulas, accesorios, pendientes, soportación y registro de condiciones observadas por anillo.",
    unidades: { farma: "02", cosmeticos: "09", suplementos: "16", pw: "23" }
  },
  {
    num: 3,
    informe: "W2608PRINF003",
    semana: "Semana 5",
    titulo: "Identificación y evaluación de puntos muertos",
    detalle: "Inventario y localización de derivaciones, ramales ciegos, instrumentos y conexiones con posible retención o estancamiento, geometría verificable y relación con el régimen hidráulico de recirculación.",
    unidades: { farma: "03", cosmeticos: "10", suplementos: "17", pw: "24" }
  },
  {
    num: 4,
    informe: "W2608PRINF004",
    semana: "Semana 5",
    titulo: "Diagnóstico general integrado",
    detalle: "Evaluación conjunta del estado sanitario, constructivo, hidráulico y operativo de cada anillo y de las interfaces comunes con el tanque de 3.000 L, identificando cuellos de botella y restricciones operativas.",
    unidades: { farma: "04", cosmeticos: "11", suplementos: "18", pw: "25" }
  },
  {
    num: 5,
    informe: "W2608PRINF005",
    semana: "Semana 6",
    titulo: "Identificación trazable de no conformidades",
    detalle: "Comparación sistemática de las evidencias levantadas con el requisito normativo aplicable por sector y uso, diferenciando desviaciones sustentadas de condiciones pendientes de verificación documental o física.",
    unidades: { farma: "05", cosmeticos: "12", suplementos: "19", pw: "26" }
  },
  {
    num: 6,
    informe: "W2608PRINF006",
    semana: "Semana 6",
    titulo: "Clasificación de criticidad y riesgo",
    detalle: "Priorización de hallazgos según su impacto sanitario, microbiológico y operativo mediante criterios explícitos, distinguiendo la clasificación regulatoria del orden técnico de intervención.",
    unidades: { farma: "06", cosmeticos: "13", suplementos: "20", pw: "27" }
  },
  {
    num: 7,
    informe: "W2608PRINF007",
    semana: "Semana 7",
    titulo: "Propuesta de rediseño y acciones de mejora",
    detalle: "Formulación de alternativas de modificación geométrica, hidráulica y sanitaria sustentadas en las memorias de cálculo, con prioridades de implementación e integración con el sistema común.",
    unidades: { farma: "07", cosmeticos: "14", suplementos: "21", pw: "28" }
  }
];

const ENTREGABLES = [
  {
    num: 1,
    codigo: "W2608PRINF001",
    tipo: "INF",
    titulo: "Informe de evaluación de videoscopia y tintas penetrantes",
    descripcion: "Interpretación de los reportes suministrados, localización de indicaciones, limitaciones de la evidencia y análisis de su incidencia sanitaria y operativa, con recomendaciones de verificación.",
    cobertura: "Tanque común de 3.000 L e incidencia en los cuatro anillos",
    entrega: "Semana 4",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 2,
    codigo: "W2608PRINF002",
    tipo: "INF",
    titulo: "Informe de inspección en campo",
    descripcion: "Registro de las condiciones documentadas en las visitas, contraste con planos e identificación de equipos, líneas y conexiones, con observaciones por anillo e implicaciones hidráulicas.",
    cobertura: "Los cuatro anillos y las interfaces comunes",
    entrega: "Semana 4",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 3,
    codigo: "W2608PRINF003",
    tipo: "INF",
    titulo: "Informe de identificación de puntos muertos",
    descripcion: "Inventario y localización de derivaciones y zonas con posible retención o estancamiento, geometría verificable y criterio de evaluación, con relación al funcionamiento hidráulico y a las acciones de mejora.",
    cobertura: "Los cuatro anillos",
    entrega: "Semana 5",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 4,
    codigo: "W2608PRINF004",
    tipo: "INF",
    titulo: "Informe de diagnóstico general",
    descripcion: "Integración del estado del sistema, su comportamiento hidráulico y las evidencias sanitarias y operativas; restricciones, condiciones relevantes y necesidades de mejora por anillo y para el conjunto.",
    cobertura: "Los cuatro anillos y las interfaces comunes",
    entrega: "Semana 5",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 5,
    codigo: "W2608PRINF005",
    tipo: "INF",
    titulo: "Informe de identificación de no conformidades",
    descripcion: "Matriz de hallazgos vinculados con requisito aplicable, ubicación, evidencia e implicación técnica, con distinción entre desviaciones sustentadas y condiciones pendientes de verificación.",
    cobertura: "Los cuatro anillos",
    entrega: "Semana 6",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 6,
    codigo: "W2608PRINF006",
    tipo: "INF",
    titulo: "Informe de clasificación de criticidad",
    descripcion: "Priorización de hallazgos según los criterios sanitarios y operativos acordados, con justificación de impacto y urgencia; diferencia la clasificación regulatoria de la prioridad de intervención.",
    cobertura: "Los cuatro anillos",
    entrega: "Semana 6",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 7,
    codigo: "W2608PRINF007",
    tipo: "INF",
    titulo: "Informe de propuestas de rediseño y acciones de mejora",
    descripcion: "Propuestas técnicas de modificación y mejora sustentadas en cálculos, con prioridades, interfaces y verificaciones requeridas para su implementación en los cuatro anillos.",
    cobertura: "Los cuatro anillos e integración del sistema",
    entrega: "Semana 7",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 8,
    codigo: "W2608PRINF008",
    tipo: "EJEC",
    titulo: "Informe general ejecutivo",
    descripcion: "Síntesis para la dirección de los resultados del diagnóstico, hallazgos principales, prioridades y hoja de ruta, con remisión a los informes y memorias que sustentan las decisiones técnicas.",
    cobertura: "Sistema completo",
    entrega: "Semana 8",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 9,
    codigo: "W2608PRCAL001",
    tipo: "CAL",
    titulo: "Memoria de cálculo hidráulico del anillo Farma",
    descripcion: "Datos y fuentes, hipótesis, geometría, modelo estacionario, escenarios, resultados de caudal, presión, velocidad y pérdidas de carga, verificaciones dimensionales y comparación con mejoras modeladas.",
    cobertura: "Anillo Farma e interfaces comunes pertinentes",
    entrega: "Semana 4",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 10,
    codigo: "W2608PRCAL002",
    tipo: "CAL",
    titulo: "Memoria de cálculo hidráulico del anillo Cosméticos",
    descripcion: "Modelado hidráulico del anillo Cosméticos: entradas verificadas, curvas y demandas, evaluación de régimen de flujo, velocidades de retorno, caídas de presión y escenarios de mejora.",
    cobertura: "Anillo Cosméticos e interfaces comunes pertinentes",
    entrega: "Semana 4",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 11,
    codigo: "W2608PRCAL003",
    tipo: "CAL",
    titulo: "Memoria de cálculo hidráulico del anillo Suplementos",
    descripcion: "Modelado hidráulico del anillo Suplementos: caracterización geométrica, pérdidas por fricción y accesorios sanitarios, distribución de presiones y sensibilidad operativa.",
    cobertura: "Anillo Suplementos e interfaces comunes pertinentes",
    entrega: "Semana 4",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 12,
    codigo: "W2608PRCAL004",
    tipo: "CAL",
    titulo: "Memoria de cálculo hidráulico del anillo PW",
    descripcion: "Modelado hidráulico del anillo PW: balance de masa y energía, condiciones de frontera con el tanque de 3.000 L, caudales de recirculación y verificación de condiciones hidrodinámicas.",
    cobertura: "Anillo PW e interfaces comunes pertinentes",
    entrega: "Semana 4",
    responsable: "J.Arboleda (Elab.) / J.Micolta (Rev.)"
  },
  {
    num: 13,
    codigo: "W2608PRLIS001",
    tipo: "LIS",
    titulo: "Listado maestro de documentos",
    descripcion: "Registro de código, título, revisión, responsables, estado y fechas de los trece entregables técnicos para control documental de su preparación, revisión y emisión.",
    cobertura: "Los trece documentos del estudio",
    entrega: "Semana 1 / Cierre Semana 8",
    responsable: "J.Micolta / J.Arboleda"
  }
];

const NORMATIVA = [
  {
    ambito: "colombia",
    ref: "Resolución 1160 de 2016 y Resolución 2190 de 2020 (MSPS)",
    naturaleza: "BPM de medicamentos; anexos según operaciones y productos fabricados [1, 2]",
    aplicacion: "Revisión de especificaciones de agua, equipos en contacto, planos actualizados, limpieza y evidencia de calificación y validación; anexo 1, numerales 13.9, 13.13 y 15.14–15.17."
  },
  {
    ambito: "andina",
    ref: "Resolución 2206 de 2021 (Comunidad Andina — CAN)",
    naturaleza: "Reglamento Técnico Andino de BPM en productos cosméticos [3]",
    aplicacion: "Evaluación de calidad del agua según uso, sanitización, materiales, corrosión, contaminación, estancamiento, identificación y monitoreo, conforme a numerales 12.8.1–12.8.4."
  },
  {
    ambito: "andina",
    ref: "Resolución 2214 de 2021 (Comunidad Andina — CAN)",
    naturaleza: "Lista de verificación armonizada de BPM cosméticas [4]",
    aplicacion: "Relación trazable de los hallazgos del sistema con los ítems 77–80 sobre sistemas de agua."
  },
  {
    ambito: "colombia",
    ref: "Decreto 3249 de 2006 y modificaciones",
    naturaleza: "Régimen regulatorio de suplementos dietarios en Colombia [14]",
    aplicacion: "Contraste del anexo 1, numeral 5.1 (tratamiento, sanitización de tuberías, puntos de muestreo y control de calidad) según la categoría aplicable al anillo Suplementos."
  },
  {
    ambito: "internacional",
    ref: "OMS, TRS 1033, Anexo 3 (2021)",
    naturaleza: "Guía técnica de buenas prácticas de agua para uso farmacéutico [5]",
    aplicacion: "Revisión de almacenamiento, distribución, sanitización, materiales, monitoreo e instrumentos, secciones 6–15."
  },
  {
    ambito: "internacional",
    ref: "USP-NF: Purified Water y capítulos <643>, <645> y <1231>",
    naturaleza: "Referencia farmacopeica requerida por el RUS FO-AS-150 [6, 21]",
    aplicacion: "Revisión de especificaciones fisicoquímicas, carbono orgánico total (TOC), conductividad, control microbiológico y representatividad del muestreo."
  },
  {
    ambito: "ingenieria",
    ref: "ASME BPE (Edición 2026)",
    naturaleza: "Estándar de ingeniería de equipos de bioprocesamiento con altas exigencias higiénicas [7]",
    aplicacion: "Sustento técnico para la evaluación de materiales, diseño drenable, fabricación, uniones soldadas y desmontables, acabados superficiales e inspección."
  },
  {
    ambito: "ingenieria",
    ref: "3-A Sanitary Standards (00-02, 33-03, 54-02, 58-02, 63-04, 64-00)",
    naturaleza: "Estándares y prácticas de diseño higiénico por familia de componentes [8, 9, 18–20]",
    aplicacion: "Criterios generales (00-02), tubería metálica (33-03), accesorios sanitarios (63-04), válvulas de diafragma (54-02), retención/vacío (58-02) y regulación de presión (64-00)."
  },
  {
    ambito: "ingenieria",
    ref: "ASTM A270/A270M-24, ASTM A380/A380M-25 y ASTM A967/A967M-25",
    naturaleza: "Especificaciones de tubería sanitaria inoxidable y pasivación química [10–12]",
    aplicacion: "Contraste de identificación de tubería austenítica, certificados de fabricación y registros de limpieza, decapado y pasivación."
  },
  {
    ambito: "sst",
    ref: "ISO 22716:2007",
    naturaleza: "Guía de Buenas Prácticas de Manufactura para productos cosméticos [13]",
    aplicacion: "Complemento técnico para la revisión de equipos, drenabilidad, limpieza y documentación operativa cuando sea adoptada por el establecimiento."
  },
  {
    ambito: "sst",
    ref: "ISO 45001:2018 (+Amd 1:2024), Decreto 1072 de 2015 y Resolución 0312 de 2019",
    naturaleza: "Gestión preventiva de Seguridad y Salud en el Trabajo (SST) en el diseño [15–17]",
    aplicacion: "Identificación de peligros de presión, temperatura, agentes químicos de sanitización y accesos; aplicación de la jerarquía de controles (cláusula 8.1.2)."
  }
];

/* ==========================================================================
   Inicialización de Interacciones
   ========================================================================== */
document.addEventListener("DOMContentLoaded", () => {
  initSchematicNodes();
  renderMatrixTable("all");
  selectUnit("01");
  renderDeliverables("ALL", "");
  renderNormativa("all");
  initFilterControls();
});

function initSchematicNodes() {
  const nodes = document.querySelectorAll("[data-loop-key]");
  const banner = document.getElementById("schematic-detail-banner");
  nodes.forEach((node) => {
    node.addEventListener("click", () => {
      const key = node.getAttribute("data-loop-key");
      const info = LOOP_DETAILS[key];
      if (!info || !banner) return;
      banner.innerHTML = `
        <strong>${info.title}</strong> · <span style="font-family: var(--font-mono); font-size: 0.78rem;">${info.unidades} · ${info.memoria}</span><br/>
        <span>${info.desc}</span>
      `;
    });
  });
}

function renderMatrixTable(loopFilter) {
  const tbody = document.getElementById("matrix-tbody");
  if (!tbody) return;

  tbody.innerHTML = EVALUACIONES_MATRIZ.map((row) => {
    const makeBtn = (loopKey, unitCode) => {
      const dimmed = loopFilter !== "all" && loopFilter !== loopKey ? "dimmed" : "";
      return `<button type="button" class="unit-btn ${dimmed}" data-unit="${unitCode}" onclick="selectUnit('${unitCode}')">${unitCode}</button>`;
    };

    return `
      <tr>
        <td><span class="code-pill">${row.informe}</span></td>
        <td>
          <strong style="color: var(--ink-primary);">${row.num}. ${row.titulo}</strong><br/>
          <span style="font-size: 0.84rem; color: var(--ink-muted);">${row.detalle}</span>
        </td>
        <td style="text-align:center;">${makeBtn("farma", row.unidades.farma)}</td>
        <td style="text-align:center;">${makeBtn("cosmeticos", row.unidades.cosmeticos)}</td>
        <td style="text-align:center;">${makeBtn("suplementos", row.unidades.suplementos)}</td>
        <td style="text-align:center;">${makeBtn("pw", row.unidades.pw)}</td>
      </tr>
    `;
  }).join("");
}

window.selectUnit = function selectUnit(unitCode) {
  document.querySelectorAll(".unit-btn").forEach((btn) => {
    btn.classList.toggle("selected", btn.getAttribute("data-unit") === unitCode);
  });

  const loopMap = {
    farma: { nombre: "Anillo Farma", cal: "W2608PRCAL001", Marco: "Res. 1160/2016, 2190/2020, OMS TRS 1033, USP-NF, ASME BPE" },
    cosmeticos: { nombre: "Anillo Cosméticos", cal: "W2608PRCAL002", Marco: "Res. CAN 2206/2021 (12.8.1–12.8.4), CAN 2214/2021 (77–80), ISO 22716" },
    suplementos: { nombre: "Anillo Suplementos", cal: "W2608PRCAL003", Marco: "Decreto 3249/2006 (Anexo 1, num. 5.1), ASME BPE, 3-A" },
    pw: { nombre: "Anillo PW (Agua Purificada)", cal: "W2608PRCAL004", Marco: "USP <1231>/<643>/<645>, OMS TRS 1033, ASME BPE-2026" }
  };

  let foundRow = null;
  let foundLoopKey = null;

  for (const row of EVALUACIONES_MATRIZ) {
    for (const [k, code] of Object.entries(row.unidades)) {
      if (code === unitCode) {
        foundRow = row;
        foundLoopKey = k;
        break;
      }
    }
  }

  if (!foundRow || !foundLoopKey) return;
  const loopInfo = loopMap[foundLoopKey];
  const panel = document.getElementById("unit-inspector-content");
  if (!panel) return;

  panel.innerHTML = `
    <span class="inspector-badge">UNIDAD DE ANÁLISIS #${unitCode} DE 28</span>
    <h3 class="inspector-title">${foundRow.titulo} — ${loopInfo.nombre}</h3>
    <p style="font-size: 0.9rem; color: var(--ink-secondary); line-height: 1.6; margin: 0;">
      ${foundRow.detalle}
    </p>
    <div class="inspector-meta-list">
      <div class="inspector-row">
        <strong>Informe de evaluación:</strong>
        <span class="code-pill">${foundRow.informe}</span>
      </div>
      <div class="inspector-row">
        <strong>Memoria hidráulica vinculada:</strong>
        <span class="code-pill">${loopInfo.cal}</span>
      </div>
      <div class="inspector-row">
        <strong>Anillo / Sistema:</strong>
        <span>${loopInfo.nombre} + Tanque 3.000 L</span>
      </div>
      <div class="inspector-row">
        <strong>Primera entrega programada:</strong>
        <span>${foundRow.semana}</span>
      </div>
      <div class="inspector-row">
        <strong>Marco normativo primario:</strong>
        <span style="text-align: right;">${loopInfo.Marco}</span>
      </div>
    </div>
    <div style="font-size: 0.8rem; color: var(--ink-muted);">
      Trazabilidad: Requisito aplicable → Evidencia de campo / END → Modelo hidráulico (${loopInfo.cal}) → Hallazgo y recomendación en ${foundRow.informe}.
    </div>
  `;
};

function renderDeliverables(typeFilter, query) {
  const tbody = document.getElementById("deliverables-tbody");
  const counter = document.getElementById("deliverables-count");
  if (!tbody) return;

  const q = query.trim().toLowerCase();
  const filtered = ENTREGABLES.filter((item) => {
    const matchesType = typeFilter === "ALL" || item.tipo === typeFilter;
    const matchesQuery =
      !q ||
      item.codigo.toLowerCase().includes(q) ||
      item.titulo.toLowerCase().includes(q) ||
      item.descripcion.toLowerCase().includes(q) ||
      item.cobertura.toLowerCase().includes(q) ||
      item.entrega.toLowerCase().includes(q);
    return matchesType && matchesQuery;
  });

  if (counter) {
    counter.textContent = `Mostrando ${filtered.length} de 13 documentos técnicos planificados`;
  }

  tbody.innerHTML = filtered
    .map(
      (d) => `
    <tr>
      <td><span style="font-family: var(--font-mono); color: var(--ink-muted);">${String(d.num).padStart(2, "0")}</span></td>
      <td><span class="code-pill">${d.codigo}</span></td>
      <td>
        <strong style="color: var(--ink-primary);">${d.titulo}</strong><br/>
        <span style="font-size: 0.85rem;">${d.descripcion}</span>
      </td>
      <td>${d.cobertura}</td>
      <td><span style="font-family: var(--font-mono); font-size: 0.8rem;">${d.entrega}</span></td>
      <td><span style="font-size: 0.82rem; color: var(--ink-muted);">${d.responsable}</span></td>
    </tr>
  `
    )
    .join("");
}

function renderNormativa(scopeFilter) {
  const tbody = document.getElementById("normativa-tbody");
  if (!tbody) return;

  const filtered = NORMATIVA.filter(
    (item) => scopeFilter === "all" || item.ambito === scopeFilter
  );

  tbody.innerHTML = filtered
    .map(
      (n) => `
    <tr>
      <td><strong style="color: var(--ink-primary);">${n.ref}</strong></td>
      <td>${n.naturaleza}</td>
      <td>${n.aplicacion}</td>
    </tr>
  `
    )
    .join("");
}

function initFilterControls() {
  // Filtro de matriz por anillo
  document.querySelectorAll("[data-matrix-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-matrix-filter]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderMatrixTable(btn.getAttribute("data-matrix-filter"));
    });
  });

  // Filtro de entregables
  let currentDelivType = "ALL";
  const searchInput = document.getElementById("deliverables-search");

  document.querySelectorAll("[data-deliv-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-deliv-filter]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentDelivType = btn.getAttribute("data-deliv-filter");
      renderDeliverables(currentDelivType, searchInput ? searchInput.value : "");
    });
  });

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      renderDeliverables(currentDelivType, e.target.value);
    });
  }

  // Filtro de normativa
  document.querySelectorAll("[data-norm-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-norm-filter]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderNormativa(btn.getAttribute("data-norm-filter"));
    });
  });
}
