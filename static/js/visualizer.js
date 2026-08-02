/**
 * Interactive Plotly Visualizer for Vectors and Linear Systems
 */
function renderVector2DPlot(containerId, u, v, uPlusV = null, projUV = null) {
    const container = document.getElementById(containerId);
    if (!container || !window.Plotly) return;

    const traces = [
        {
            x: [0, u[0]], y: [0, u[1]],
            mode: 'lines+markers+text',
            name: 'Vector u',
            line: { color: '#6366f1', width: 4 },
            text: ['', `u (${u[0]}, ${u[1]})`]
        },
        {
            x: [0, v[0]], y: [0, v[1]],
            mode: 'lines+markers+text',
            name: 'Vector v',
            line: { color: '#ec4899', width: 4 },
            text: ['', `v (${v[0]}, ${v[1]})`]
        }
    ];

    if (uPlusV) {
        traces.push({
            x: [0, uPlusV[0]], y: [0, uPlusV[1]],
            mode: 'lines+markers+text',
            name: 'u + v',
            line: { color: '#10b981', width: 3, dash: 'dash' },
            text: ['', 'u+v']
        });
    }

    if (projUV) {
        traces.push({
            x: [0, projUV[0]], y: [0, projUV[1]],
            mode: 'lines+markers+text',
            name: 'proj_v(u)',
            line: { color: '#f59e0b', width: 3 },
            text: ['', 'proj']
        });
    }

    const layout = {
        title: '2D Vector Space Plot',
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        font: { color: '#f8fafc' },
        xaxis: { gridcolor: '#334155', zerolinecolor: '#64748b' },
        yaxis: { gridcolor: '#334155', zerolinecolor: '#64748b' },
        height: 400,
        margin: { l: 40, r: 40, t: 40, b: 40 }
    };

    Plotly.newPlot(containerId, traces, layout, { responsive: true });
}

function renderVector3DPlot(containerId, u, v, crossUV = null) {
    const container = document.getElementById(containerId);
    if (!container || !window.Plotly) return;

    const traces = [
        {
            type: 'scatter3d',
            x: [0, u[0]], y: [0, u[1]], z: [0, u[2]],
            mode: 'lines+markers',
            name: 'Vector u',
            line: { color: '#6366f1', width: 6 }
        },
        {
            type: 'scatter3d',
            x: [0, v[0]], y: [0, v[1]], z: [0, v[2]],
            mode: 'lines+markers',
            name: 'Vector v',
            line: { color: '#ec4899', width: 6 }
        }
    ];

    if (crossUV) {
        traces.push({
            type: 'scatter3d',
            x: [0, crossUV[0]], y: [0, crossUV[1]], z: [0, crossUV[2]],
            mode: 'lines+markers',
            name: 'u × v (Cross Product)',
            line: { color: '#10b981', width: 6 }
        });
    }

    const layout = {
        title: '3D Vector Space Plot',
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        font: { color: '#f8fafc' },
        scene: {
            xaxis: { gridcolor: '#334155', zerolinecolor: '#64748b' },
            yaxis: { gridcolor: '#334155', zerolinecolor: '#64748b' },
            zaxis: { gridcolor: '#334155', zerolinecolor: '#64748b' }
        },
        height: 450,
        margin: { l: 20, r: 20, t: 40, b: 20 }
    };

    Plotly.newPlot(containerId, traces, layout, { responsive: true });
}
