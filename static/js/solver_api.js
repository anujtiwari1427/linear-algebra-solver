/**
 * REST API Client & Result Renderer with MathJax Support
 * Premium Web Design System Engine
 */
async function submitCalculation(endpoint, payload, resultCardId = "resultCard", spinnerId = "loadingSpinner") {
    const resultCard = document.getElementById(resultCardId);
    const spinner = document.getElementById(spinnerId);

    // Hide any active error alerts
    document.querySelectorAll('.alert-danger').forEach(alert => alert.classList.add('d-none'));

    if (spinner) spinner.classList.add("active");
    if (resultCard) resultCard.classList.remove("active");

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (spinner) spinner.classList.remove("active");

        if (!data.success) {
            showErrorAlert(data.error || "An unexpected calculation error occurred.", resultCardId);
            return;
        }

        renderResultCard(data, resultCardId);
    } catch (err) {
        if (spinner) spinner.classList.remove("active");
        showErrorAlert("Server communication failed: " + err.message, resultCardId);
    }
}

function showErrorAlert(message, resultCardId = "resultCard") {
    const prefix = resultCardId.endsWith("Card") ? resultCardId.slice(0, -4) : resultCardId;
    let errorAlert = document.getElementById(prefix.replace(/Result$/, "") + "Error") ||
                     document.getElementById("singleError") ||
                     document.getElementById("dualError") ||
                     document.getElementById("errorAlert");

    if (errorAlert) {
        errorAlert.innerHTML = `<strong>⚠️ Validation Error:</strong> ${message}`;
        errorAlert.classList.remove("d-none");
        errorAlert.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function copyLatexToClipboard(latexText) {
    const targetText = latexText || window.currentLatex;
    if (!targetText) return;
    navigator.clipboard.writeText(targetText).then(() => {
        const btn = document.getElementById("copyLatexBtn");
        if (btn) {
            const originalText = btn.innerHTML;
            btn.innerHTML = "✓ LaTeX Copied!";
            btn.classList.add("btn-success");
            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.classList.remove("btn-success");
            }, 2000);
        }
    });
}

function renderResultCard(data, resultCardId = "resultCard") {
    const card = document.getElementById(resultCardId);
    if (!card) return;

    // Helper to resolve child elements dynamically by suffix (Latex, Steps, Explanation, Complexity)
    const findEl = (suffix) => {
        const prefix = resultCardId.endsWith("Card") ? resultCardId.slice(0, -4) : resultCardId;
        const targetId = prefix + suffix;
        return document.getElementById(targetId) ||
               document.getElementById("result" + suffix) ||
               card.querySelector(`[id$="${suffix}"]`) ||
               card.querySelector(`[id*="${suffix}"]`);
    };

    const latexEl = findEl("Latex");
    const stepsContainer = findEl("Steps");
    const explanationEl = findEl("Explanation");
    const complexityEl = findEl("Complexity");

    if (latexEl && data.latex_result) {
        latexEl.innerHTML = `$$${data.latex_result}$$`;
        window.currentLatex = data.latex_result;
    }

    if (explanationEl && data.explanation) {
        explanationEl.innerHTML = `<span class="badge-tech me-2">💡 Context</span><span>${data.explanation}</span>`;
    }

    if (complexityEl && data.time_complexity) {
        complexityEl.innerHTML = `<span class="badge-tech">⚡ Time Complexity: <code>${data.time_complexity}</code></span>`;
    }

    if (stepsContainer && data.steps && data.steps.length > 0) {
        let html = '<h6 class="fw-bold mt-4 mb-3 text-gradient-primary">Step-by-Step Breakdown:</h6>';
        data.steps.forEach((step, idx) => {
            html += `<div class="step-card">
                <div class="step-badge">Step ${idx + 1}</div>
                <div>${step}</div>
            </div>`;
        });
        stepsContainer.innerHTML = html;
    } else if (stepsContainer) {
        stepsContainer.innerHTML = '';
    }

    card.classList.add("active");

    // Trigger MathJax re-render
    if (window.MathJax) {
        MathJax.typesetPromise();
    }

    // Smooth scroll to result
    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
