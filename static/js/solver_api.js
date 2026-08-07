/**
 * REST API Client & Result Renderer with MathJax Support
 * Premium Web Design System Engine
 */
async function submitCalculation(endpoint, payload, resultCardId = "resultCard", spinnerId = "loadingSpinner") {
    const resultCard = document.getElementById(resultCardId);

    // Hide any active error alerts
    document.querySelectorAll('.alert-danger').forEach(alert => alert.classList.add('d-none'));

    // Dynamically locate elements inside resultCard for instant loading state feedback
    const prefix = resultCardId.endsWith("Card") ? resultCardId.slice(0, -4) : resultCardId;
    const latexEl = document.getElementById(prefix + "Latex") || (resultCard ? resultCard.querySelector('[id$="Latex"]') : null);
    const stepsContainer = document.getElementById(prefix + "Steps") || (resultCard ? resultCard.querySelector('[id$="Steps"]') : null);
    const explanationEl = document.getElementById(prefix + "Explanation") || (resultCard ? resultCard.querySelector('[id$="Explanation"]') : null);
    const complexityEl = document.getElementById(prefix + "Complexity") || (resultCard ? resultCard.querySelector('[id$="Complexity"]') : null);

    if (resultCard) {
        resultCard.classList.add("active");
        if (latexEl) {
            latexEl.innerHTML = `<div class="d-flex align-items-center justify-content-center gap-2 py-4 text-primary">
                <div class="spinner-border spinner-border-sm text-primary" role="status"></div>
                <span class="fw-semibold">Computing Derivation...</span>
            </div>`;
        }
        if (stepsContainer) stepsContainer.innerHTML = '';
        if (explanationEl) explanationEl.innerHTML = '';
        if (complexityEl) complexityEl.innerHTML = '';
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!data.success) {
            if (latexEl) latexEl.innerHTML = '';
            showErrorAlert(data.error || "An unexpected calculation error occurred.", resultCardId);
            return;
        }

        renderResultCard(data, resultCardId);
    } catch (err) {
        if (latexEl) latexEl.innerHTML = '';
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
    if (!card) {
        console.error("Target result card container not found:", resultCardId);
        return;
    }

    const prefix = resultCardId.endsWith("Card") ? resultCardId.slice(0, -4) : resultCardId;

    const latexEl = document.getElementById(prefix + "Latex") ||
                    document.getElementById("resultLatex") ||
                    card.querySelector('[id$="Latex"]');

    const stepsContainer = document.getElementById(prefix + "Steps") ||
                           document.getElementById("resultSteps") ||
                           card.querySelector('[id$="Steps"]');

    const explanationEl = document.getElementById(prefix + "Explanation") ||
                          document.getElementById("resultExplanation") ||
                          card.querySelector('[id$="Explanation"]');

    const complexityEl = document.getElementById(prefix + "Complexity") ||
                         document.getElementById("resultComplexity") ||
                         card.querySelector('[id$="Complexity"]');

    if (latexEl) {
        if (data.latex_result) {
            latexEl.innerHTML = `$$${data.latex_result}$$`;
            window.currentLatex = data.latex_result;
        } else if (data.result !== undefined) {
            latexEl.innerHTML = `$$\\text{Result} = ${typeof data.result === 'object' ? JSON.stringify(data.result) : data.result}$$`;
        }
    }

    if (explanationEl && data.explanation) {
        explanationEl.innerHTML = `<span class="badge-tech me-2">💡 Context</span><span>${data.explanation}</span>`;
    }

    if (complexityEl && data.time_complexity) {
        complexityEl.innerHTML = `<span class="badge-tech">⚡ Time Complexity: <code>${data.time_complexity}</code></span>`;
    }

    if (stepsContainer) {
        if (data.steps && data.steps.length > 0) {
            let html = '<h6 class="fw-bold mt-4 mb-3 text-gradient-primary">Step-by-Step Breakdown:</h6>';
            data.steps.forEach((step, idx) => {
                const cleanStep = typeof step === 'string' ? step.replace(/^#+\s*/, '') : step;
                html += `<div class="step-card">
                    <div class="step-badge">Step ${idx + 1}</div>
                    <div>${cleanStep}</div>
                </div>`;
            });
            stepsContainer.innerHTML = html;
        } else {
            stepsContainer.innerHTML = '';
        }
    }

    card.classList.add("active");

    // Safe MathJax typesetting with type checking
    try {
        if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
            window.MathJax.typesetPromise([card]);
        } else if (window.MathJax && typeof window.MathJax.typeset === 'function') {
            window.MathJax.typeset([card]);
        }
    } catch (e) {
        console.warn("MathJax typesetting notice:", e);
    }

    // Smooth scroll to result
    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
