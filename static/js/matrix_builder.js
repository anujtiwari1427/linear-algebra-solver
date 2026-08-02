/**
 * Dynamic Matrix Input Builder & Preset Handler
 */
function generateMatrixGrid(containerId, rows, cols, prefix = "m") {
    const container = document.getElementById(containerId);
    if (!container) return;

    let html = `<div class="matrix-bracket"><table class="matrix-input-table">`;
    for (let i = 0; i < rows; i++) {
        html += `<tr>`;
        for (let j = 0; j < cols; j++) {
            const cellId = `${prefix}_${i}_${j}`;
            const defaultVal = (i === j && rows === cols) ? 1 : 0;
            html += `<td>
                <input type="number" step="any" class="matrix-cell-input" id="${cellId}" value="${defaultVal}">
            </td>`;
        }
        html += `</tr>`;
    }
    html += `</table></div>`;
    container.innerHTML = html;
}

function getMatrixValues(containerId, rows, cols, prefix = "m") {
    const matrix = [];
    for (let i = 0; i < rows; i++) {
        const row = [];
        for (let j = 0; j < cols; j++) {
            const cellId = `${prefix}_${i}_${j}`;
            const input = document.getElementById(cellId);
            const val = input ? parseFloat(input.value) : 0;
            row.push(isNaN(val) ? 0 : val);
        }
        matrix.push(row);
    }
    return matrix;
}

function fillMatrixPreset(containerId, rows, cols, type, prefix = "m") {
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const cellId = `${prefix}_${i}_${j}`;
            const input = document.getElementById(cellId);
            if (!input) continue;

            if (type === 'identity') {
                input.value = (i === j) ? 1 : 0;
            } else if (type === 'zero') {
                input.value = 0;
            } else if (type === 'random') {
                input.value = Math.floor(Math.random() * 11) - 5;
            } else if (type === 'symmetric') {
                if (i <= j) {
                    const randVal = Math.floor(Math.random() * 9) - 4;
                    input.value = randVal;
                    // Mirror to symmetric element
                    const symId = `${prefix}_${j}_${i}`;
                    const symInput = document.getElementById(symId);
                    if (symInput) symInput.value = randVal;
                }
            }
        }
    }
}

function parseMatrixPaste(text, rows, cols, prefix = "m") {
    if (!text) return false;
    const cleanStr = text.replace(/\[/g, '').replace(/\]/g, '').trim();
    const numbers = cleanStr.split(/[\s,;]+/).map(x => parseFloat(x)).filter(x => !isNaN(x));

    if (numbers.length !== rows * cols) {
        return false;
    }

    let idx = 0;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const input = document.getElementById(`${prefix}_${i}_${j}`);
            if (input) {
                input.value = numbers[idx++];
            }
        }
    }
    return true;
}
