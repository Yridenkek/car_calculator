def load_styles():
    return """
    <style>

    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }

    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2563EB;
        border-left: 4px solid #2563EB;
        padding-left: 12px;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .total-margin {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
    }

    .total-margin .label {
        font-size: 1rem;
    }

    .total-margin .value {
        font-size: 2.2rem;
        font-weight: 800;
    }

    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #CBD5E1, transparent);
        margin: 1rem 0;
    }

    .accent-metric {
        background: #F0F9FF;
        border-radius: 8px;
        padding: 0.5rem;
        text-align: center;
        border: 1px solid #BAE6FD;
    }

    [data-testid="stSidebar"] {
        background: #F8FAFC;
    }

    .stButton button {
        border-radius: 8px;
        font-weight: 600;
    }

    .info-block {
        background: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 0.75rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }

    </style>
    """