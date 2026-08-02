/**
 * Dynamic Vector Input Builder & Handler
 */
function generateVectorGrid(containerId, dim, prefix = "v", defaults = [1, 2, 3]) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let html = `<div class="d-flex flex-wrap gap-2 justify-content-center">`;
    for (let i = 0; i < dim; i++) {
        const cellId = `${prefix}_${i}`;
        const defVal = (defaults && defaults[i] !== undefined) ? defaults[i] : (i + 1);
        html += `<div class="text-center">
            <small class="text-muted d-block">v<sub>${i+1}</sub></small>
            <input type="number" step="any" class="matrix-cell-input" id="${cellId}" value="${defVal}">
        </div>`;
    }
    html += `</div>`;
    container.innerHTML = html;
}

function getVectorValues(containerId, dim, prefix = "v") {
    const vector = [];
    for (let i = 0; i < dim; i++) {
        const input = document.getElementById(`${prefix}_${i}`);
        const val = input ? parseFloat(input.value) : 0;
        vector.push(isNaN(val) ? 0 : val);
    }
    return vector;
}
