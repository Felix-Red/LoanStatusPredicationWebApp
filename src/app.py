import joblib
from pathlib import Path
from dash import Dash, Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate


classifier = joblib.load(Path(__file__).with_name("classifierModel.plk"))

app = Dash(__name__, assets_folder="assets")
server = app.server


def money(value):
    """Format an amount in rupees without implying a currency conversion."""
    return f"₹{int(value or 0):,}"


def field(label, component, help_text=None, class_name=""):
    children = [html.Label(label, className="field-label", htmlFor=component.id)]
    children.append(component)
    if help_text:
        children.append(html.Div(help_text, className="field-help"))
    return html.Div(children, className=f"field {class_name}".strip())


def select(options, placeholder, component_id):
    return dcc.Dropdown(
        id=component_id,
        options=options,
        placeholder=placeholder,
        clearable=False,
        className="select-control",
    )


def range_input(component_id, minimum, maximum, value, step=1):
    return dcc.Input(
        id=component_id,
        type="range",
        min=minimum,
        max=maximum,
        step=step,
        value=value,
        className="range-control",
    )


app.layout = html.Div(
    [
        html.Header(
            [
                html.Div(
                    [
                        html.Div("L", className="brand-mark", **{"aria-hidden": "true"}),
                        html.Div(
                            [
                                html.Div("LOANWISE", className="brand-name"),
                                html.Div("A calmer way to plan", className="brand-caption"),
                            ]
                        ),
                    ],
                    className="brand-lockup",
                ),
                html.Div(
                    [html.Span(className="secure-dot"), "Your details stay private"],
                    className="privacy-note",
                ),
            ],
            className="topbar page-shell",
        ),
        html.Main(
            [
                html.Section(
                    [
                        html.Div("LOAN ELIGIBILITY · MADE CLEAR", className="eyebrow"),
                        html.H1(["Plan your next move,", html.Br(), html.Em("with more clarity.")]),
                        html.P(
                            "Share a few details to explore your loan outlook. Adjust the numbers as you go; your summary updates in real time.",
                            className="hero-copy",
                        ),
                    ],
                    className="hero",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Section(
                                    [
                                        html.Div(
                                            [
                                                html.Span("01", className="section-index"),
                                                html.Div(
                                                    [
                                                        html.H2("About you", className="section-title"),
                                                        html.P("A little context helps us shape your estimate.", className="section-copy"),
                                                    ]
                                                ),
                                            ],
                                            className="section-heading",
                                        ),
                                        html.Div(
                                            [
                                                field(
                                                    "Gender",
                                                    select(
                                                        [{"label": "Female", "value": 0}, {"label": "Male", "value": 1}],
                                                        "Choose an option",
                                                        "gender-dropdown",
                                                    ),
                                                ),
                                                field(
                                                    "Marital status",
                                                    select(
                                                        [
                                                            {"label": "Single", "value": 0},
                                                            {"label": "Married", "value": 1},
                                                            {"label": "Divorced", "value": 2},
                                                        ],
                                                        "Choose an option",
                                                        "marital-status-dropdown",
                                                    ),
                                                ),
                                                field(
                                                    "Dependents",
                                                    select(
                                                        [
                                                            {"label": "None", "value": 0},
                                                            {"label": "1 dependent", "value": 1},
                                                            {"label": "2 dependents", "value": 2},
                                                            {"label": "3 or more", "value": 3},
                                                        ],
                                                        "Choose a number",
                                                        "dependents",
                                                    ),
                                                ),
                                                field(
                                                    "Education",
                                                    select(
                                                        [
                                                            {"label": "Graduate", "value": 1},
                                                            {"label": "Not a graduate", "value": 0},
                                                        ],
                                                        "Choose an option",
                                                        "education-dropdown",
                                                    ),
                                                ),
                                                field(
                                                    "Self-employed",
                                                    select(
                                                        [{"label": "No", "value": 0}, {"label": "Yes", "value": 1}],
                                                        "Choose an option",
                                                        "self-employed-dropdown",
                                                    ),
                                                ),
                                            ],
                                            className="field-grid profile-grid",
                                        ),
                                    ],
                                    className="form-card",
                                ),
                                html.Section(
                                    [
                                        html.Div(
                                            [
                                                html.Span("02", className="section-index"),
                                                html.Div(
                                                    [
                                                        html.H2("Monthly income", className="section-title"),
                                                        html.P("Move the sliders to match your household income.", className="section-copy"),
                                                    ]
                                                ),
                                            ],
                                            className="section-heading",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Label("Your monthly income", className="field-label", htmlFor="applicant-income-input"),
                                                        html.Span(money(4500), id="applicant-income-value", className="range-value", **{"aria-live": "polite", "aria-atomic": "true"}),
                                                    ],
                                                    className="range-label-row",
                                                ),
                                                range_input("applicant-income-input", 0, 9000, 4500, 100),
                                                html.Div("₹0", className="range-boundary range-min"),
                                                html.Div("₹9,000", className="range-boundary range-max"),
                                            ],
                                            className="range-field",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Label("Co-applicant monthly income", className="field-label", htmlFor="coapplicant-income-input"),
                                                        html.Span(money(2000), id="coapplicant-income-value", className="range-value", **{"aria-live": "polite", "aria-atomic": "true"}),
                                                    ],
                                                    className="range-label-row",
                                                ),
                                                range_input("coapplicant-income-input", 0, 4000, 2000, 100),
                                                html.Div("₹0", className="range-boundary range-min"),
                                                html.Div("₹4,000", className="range-boundary range-max"),
                                            ],
                                            className="range-field",
                                        ),
                                    ],
                                    className="form-card",
                                ),
                                html.Section(
                                    [
                                        html.Div(
                                            [
                                                html.Span("03", className="section-index"),
                                                html.Div(
                                                    [
                                                        html.H2("Loan details", className="section-title"),
                                                        html.P("Set the amount and a few final details.", className="section-copy"),
                                                    ]
                                                ),
                                            ],
                                            className="section-heading",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Label("Loan amount", className="field-label", htmlFor="loan-amount-input"),
                                                                html.Span("In thousands of rupees", className="unit-note"),
                                                            ],
                                                            className="amount-label",
                                                        ),
                                                        html.Span("₹350,000", id="loan-amount-value", className="range-value", **{"aria-live": "polite", "aria-atomic": "true"}),
                                                    ],
                                                    className="range-label-row",
                                                ),
                                                range_input("loan-amount-input", 0, 700, 350, 5),
                                                html.Div("₹0", className="range-boundary range-min"),
                                                html.Div("₹700k", className="range-boundary range-max"),
                                            ],
                                            className="range-field",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Label("Repayment term", className="field-label", htmlFor="loan-term-input"),
                                                                html.Span("Months", className="unit-note"),
                                                            ],
                                                            className="amount-label",
                                                        ),
                                                        html.Span("180 months", id="loan-term-value", className="range-value", **{"aria-live": "polite", "aria-atomic": "true"}),
                                                    ],
                                                    className="range-label-row",
                                                ),
                                                range_input("loan-term-input", 0, 360, 180, 6),
                                                html.Div("0 months", className="range-boundary range-min"),
                                                html.Div("360 months", className="range-boundary range-max"),
                                            ],
                                            className="range-field",
                                        ),
                                        html.Div(
                                            [
                                                field(
                                                    "Credit history",
                                                    select(
                                                        [{"label": "Good", "value": 1.0}, {"label": "Needs attention", "value": 0.0}],
                                                        "Choose an option",
                                                        "credit-history-dropdown",
                                                    ),
                                                ),
                                                field(
                                                    "Property area",
                                                    select(
                                                        [
                                                            {"label": "Urban", "value": 2},
                                                            {"label": "Semi-urban", "value": 1},
                                                            {"label": "Rural", "value": 0},
                                                        ],
                                                        "Choose an option",
                                                        "residential-area-dropdown",
                                                    ),
                                                ),
                                            ],
                                            className="field-grid loan-meta-grid",
                                        ),
                                        html.Div(
                                            [
                                                html.Button(
                                                    ["Explore my outlook", html.Span("→", className="button-arrow")],
                                                    id="predict-button",
                                                    n_clicks=0,
                                                    className="primary-button",
                                                ),
                                                html.P("This estimate is a guide and not a lending decision.", className="button-note"),
                                            ],
                                            className="form-actions",
                                        ),
                                        html.Div(id="prediction-output", className="prediction-output", role="status", **{"aria-live": "polite"}),
                                    ],
                                    className="form-card loan-card",
                                ),
                            ],
                            className="form-column",
                        ),
                        html.Aside(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div("YOUR SNAPSHOT", className="summary-eyebrow"),
                                                html.Div("↗", className="summary-sparkle", **{"aria-hidden": "true"}),
                                            ],
                                            className="summary-topline",
                                        ),
                                        html.H2("Loan summary", className="summary-title"),
                                        html.P("A live view of the numbers you’ve chosen.", className="summary-copy"),
                                        html.Div(
                                            [
                                                html.Span("Requested amount", className="summary-label"),
                                                html.Strong("₹350,000", id="summary-loan-amount", className="summary-main-value"),
                                            ],
                                            className="summary-featured",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Span("Repayment term", className="summary-label"),
                                                        html.Strong("180 months", id="summary-loan-term", className="summary-value"),
                                                    ],
                                                    className="summary-stat",
                                                ),
                                                html.Div(
                                                    [
                                                        html.Span("Household income / month", className="summary-label"),
                                                        html.Strong(money(6500), id="income-total-summary", className="summary-value"),
                                                    ],
                                                    className="summary-stat",
                                                ),
                                                html.Div(
                                                    [
                                                        html.Span("Principal spread / month", className="summary-label"),
                                                        html.Strong("₹1,944", id="summary-principal", className="summary-value"),
                                                        html.Span("Before interest and fees", className="summary-footnote"),
                                                    ],
                                                    className="summary-stat summary-stat-last",
                                                ),
                                            ],
                                            className="summary-stats",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Span("Your income", className="income-legend-item"),
                                                        html.Span("Co-applicant", className="income-legend-item coapplicant-legend"),
                                                    ],
                                                    className="income-legend",
                                                ),
                                                html.Div(
                                                    [
                                                        html.Div(className="income-bar-applicant", id="income-bar-applicant", style={"width": "69.2%"}),
                                                        html.Div(className="income-bar-coapplicant", id="income-bar-coapplicant", style={"width": "30.8%"}),
                                                    ],
                                                    className="income-bar-track",
                                                ),
                                                html.Div(
                                                    [
                                                        html.Span(money(4500), id="summary-applicant-income"),
                                                        html.Span(money(2000), id="summary-coapplicant-income"),
                                                    ],
                                                    className="income-breakdown",
                                                ),
                                            ],
                                            className="income-composition",
                                        ),
                                    ],
                                    className="summary-card",
                                ),
                                html.Div(
                                    [
                                        html.Div("A thoughtful estimate", className="tip-title"),
                                        html.P(
                                            "Your result is based on the details provided and should be treated as a starting point for a lender conversation.",
                                            className="tip-copy",
                                        ),
                                    ],
                                    className="summary-tip",
                                ),
                            ],
                            className="summary-column",
                        ),
                    ],
                    className="workspace-grid",
                ),
            ],
            className="page-shell main-content",
        ),
        html.Footer(
            [html.Span("LOANWISE"), html.Span("Planning starts with a clearer picture.")],
            className="page-footer page-shell",
        ),
    ],
    className="app-page",
)


@app.callback(
    Output("applicant-income-value", "children"),
    Output("coapplicant-income-value", "children"),
    Output("income-total-summary", "children"),
    Output("summary-applicant-income", "children"),
    Output("summary-coapplicant-income", "children"),
    Output("income-bar-applicant", "style"),
    Output("income-bar-coapplicant", "style"),
    Input("applicant-income-input", "value"),
    Input("coapplicant-income-input", "value"),
)
def update_income_summary(applicant_income, coapplicant_income):
    applicant_income = int(applicant_income or 0)
    coapplicant_income = int(coapplicant_income or 0)
    total = applicant_income + coapplicant_income
    applicant_share = (applicant_income / total * 100) if total else 0
    coapplicant_share = 100 - applicant_share if total else 0
    return (
        money(applicant_income),
        money(coapplicant_income),
        money(total),
        money(applicant_income),
        money(coapplicant_income),
        {"width": f"{applicant_share:.1f}%"},
        {"width": f"{coapplicant_share:.1f}%"},
    )


@app.callback(
    Output("loan-amount-value", "children"),
    Output("loan-term-value", "children"),
    Output("summary-loan-amount", "children"),
    Output("summary-loan-term", "children"),
    Output("summary-principal", "children"),
    Input("loan-amount-input", "value"),
    Input("loan-term-input", "value"),
)
def update_loan_summary(loan_amount, loan_term):
    loan_amount = int(loan_amount or 0)
    loan_term = int(loan_term or 0)
    total_loan = loan_amount * 1000
    principal_per_month = round(total_loan / loan_term) if loan_term else 0
    return (
        money(total_loan),
        f"{loan_term} months",
        money(total_loan),
        f"{loan_term} months",
        money(principal_per_month),
    )


@app.callback(
    Output("prediction-output", "children"),
    Input("predict-button", "n_clicks"),
    State("gender-dropdown", "value"),
    State("marital-status-dropdown", "value"),
    State("dependents", "value"),
    State("education-dropdown", "value"),
    State("self-employed-dropdown", "value"),
    State("applicant-income-input", "value"),
    State("coapplicant-income-input", "value"),
    State("loan-amount-input", "value"),
    State("loan-term-input", "value"),
    State("credit-history-dropdown", "value"),
    State("residential-area-dropdown", "value"),
)
def predict_loan_approval(
    n_clicks,
    gender,
    marital_status,
    dependents,
    education,
    self_employed,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history,
    residential_area,
):
    if not n_clicks:
        raise PreventUpdate

    inputs = {
        "gender": gender,
        "marital status": marital_status,
        "dependents": dependents,
        "education": education,
        "self-employment": self_employed,
        "credit history": credit_history,
        "property area": residential_area,
    }
    missing = [name for name, value in inputs.items() if value is None]
    if missing:
        return html.Div(
            [
                html.Strong("A few details are still missing."),
                html.Span(" Choose your " + ", ".join(missing) + " to continue."),
            ],
            className="result-message result-incomplete",
        )

    features = [
        gender,
        marital_status,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        residential_area,
    ]
    prediction = classifier.predict([features])[0]
    approved = prediction == 1
    return html.Div(
        [
            html.Span("✓" if approved else "•", className="result-icon"),
            html.Div(
                [
                    html.Strong("Looks promising" if approved else "More review may be needed", className="result-title"),
                    html.Span(
                        "The estimate indicates loan approval." if approved else "The estimate indicates the application may not be approved.",
                        className="result-copy",
                    ),
                ]
            ),
        ],
        className=f"result-message {'result-approved' if approved else 'result-declined'}",
    )


if __name__ == "__main__":
    app.run_server(debug=True)
