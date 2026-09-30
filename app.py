"""Construction Command Center Streamlit dashboard."""

from __future__ import annotations

import pandas as pd
import streamlit as st


RECORDS = [
    {
        "Category": "Site Operations",
        "Workstream": "Terminal A",
        "Status": "On track",
        "Open items": 3,
    },
    {
        "Category": "Site Operations",
        "Workstream": "Runway excavation",
        "Status": "Delayed",
        "Open items": 7,
    },
    {
        "Category": "Safety",
        "Workstream": "Scaffolding inspection",
        "Status": "Needs attention",
        "Open items": 4,
    },
    {
        "Category": "Safety",
        "Workstream": "PPE compliance",
        "Status": "On track",
        "Open items": 2,
    },
    {
        "Category": "Risk",
        "Workstream": "Terminal B water leakage",
        "Status": "Needs attention",
        "Open items": 5,
    },
    {
        "Category": "Construction Experts",
        "Workstream": "Structural concrete review",
        "Status": "On track",
        "Open items": 1,
    },
]


def load_records() -> pd.DataFrame:
    """Return the dashboard records as a dataframe."""
    return pd.DataFrame(RECORDS)


def filter_records(records: pd.DataFrame, category: str) -> pd.DataFrame:
    """Filter records by category, keeping all records for the default view."""
    if category == "All categories":
        return records
    return records[records["Category"] == category]


def main() -> None:
    """Render the Construction Command Center dashboard."""
    st.set_page_config(
        page_title="Construction Command Center",
        page_icon="🏗️",
        layout="wide",
    )
    st.title("Construction Command Center")
    st.caption("A focused view of current construction operations and risks.")

    records = load_records()
    categories = ["All categories", *sorted(records["Category"].unique())]
    selected_category = st.sidebar.selectbox("Category", categories)
    st.sidebar.caption("Use the selector to focus the dashboard.")

    filtered_records = filter_records(records, selected_category)
    if filtered_records.empty:
        st.info(
            f"No records match the “{selected_category}” category. "
            "Try selecting another category."
        )
        return

    st.subheader(f"{selected_category} overview")
    st.dataframe(filtered_records, use_container_width=True, hide_index=True)

    chart_data = (
        filtered_records.groupby("Workstream", as_index=True)["Open items"]
        .sum()
        .sort_values(ascending=False)
    )
    st.subheader("Open items by workstream")
    st.bar_chart(chart_data)


if __name__ == "__main__":
    main()
