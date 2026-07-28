import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

class DashboardCharts:

    # --------------------------------------------------
    # Bar Chart (Redesigned for Premium Light Corporate)
    # --------------------------------------------------
    @staticmethod
    def bar_chart(df, x, y, title, color=None):
        fig = px.bar(
            df,
            x=x,
            y=y,
            color=color,
            text=y,
            title=title,
            color_discrete_sequence=["#0F172A", "#475569", "#64748B", "#94A3B8"]
        )
        
        fig.update_traces(
            texttemplate='%{text:,.0f}' if df[y].dtype in ['int64', 'float64'] else '%{text}',
            textposition='outside',
            marker_line_width=0,
            hovertemplate="<b>%{x}</b><br>%{y:,.2f}<extra></extra>"
        )
        
        fig.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            template="plotly_white",
            title=dict(
                text=title,
                font=dict(size=14, color="#0F172A", family="sans serif", weight="bold")
            ),
            margin=dict(t=50, b=30, l=40, r=20),
            yaxis=dict(showgrid=True, gridcolor="#F1F5F9", zeroline=False),
            xaxis=dict(showgrid=False)
        )
        
        # Menggunakan parameter config untuk memaksa browser menggambar ulang canvas tanpa merusak data
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --------------------------------------------------
    # Horizontal Bar Chart (Redesigned for Premium Light Corporate)
    # --------------------------------------------------
    @staticmethod
    def horizontal_bar_chart(df, x, y, title, color=None):
        fig = px.bar(
            df,
            x=x,
            y=y,
            orientation="h",
            color=color,
            text=x,
            title=title,
            color_discrete_sequence=["#0F172A", "#10B981", "#475569", "#64748B"]
        )
        
        fig.update_traces(
            texttemplate='%{text:,.3f}' if df[x].max() <= 1 else '%{text:,.0f}',
            textposition='outside',
            marker_line_width=0,
            hovertemplate="<b>%{y}</b><br>%{x:,.3f}<extra></extra>"
        )
        
        fig.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            template="plotly_white",
            title=dict(
                text=title,
                font=dict(size=14, color="#0F172A", family="sans serif", weight="bold")
            ),
            margin=dict(t=50, b=30, l=100, r=40),
            xaxis=dict(showgrid=True, gridcolor="#F1F5F9", zeroline=False),
            yaxis=dict(showgrid=False, categoryorder="total ascending")
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --------------------------------------------------
    # Line Chart (Redesigned for Premium Light Corporate)
    # --------------------------------------------------
    @staticmethod
    def line_chart(df, x, y, title, color=None):
        fig = px.line(
            df,
            x=x,
            y=y,
            color=color,
            markers=True,
            title=title,
            color_discrete_sequence=["#0F172A", "#10B981", "#3B82F6", "#6366F1"]
        )
        
        fig.update_traces(
            line=dict(width=3),
            marker=dict(size=8, symbol="circle", line=dict(width=1.5, color="#FFFFFF")),
            hovertemplate="<b>%{x}</b><br>%{y:,.2f}<extra></extra>"
        )
        
        fig.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            template="plotly_white",
            title=dict(
                text=title,
                font=dict(size=14, color="#0F172A", family="sans serif", weight="bold")
            ),
            margin=dict(t=50, b=30, l=40, r=20),
            xaxis=dict(showgrid=False, linecolor="#E2E8F0"),
            yaxis=dict(showgrid=True, gridcolor="#F1F5F9", zeroline=False),
            legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --------------------------------------------------
    # Scatter Chart (Redesigned for Premium Light Corporate)
    # --------------------------------------------------
    @staticmethod
    def scatter_chart(df, x, y, title, color=None, size=None):
        fig = px.scatter(
            df,
            x=x,
            y=y,
            color=color,
            size=size,
            title=title,
            color_discrete_sequence=["#0F172A", "#10B981", "#3B82F6", "#6366F1"]
        )
        
        fig.update_traces(
            marker=dict(line=dict(width=1, color="#FFFFFF")),
            hovertemplate="<b>%{hovertext}</b><br>X: %{x:,.2f}<br>Y: %{y:,.2f}<extra></extra>"
        )
        
        fig.update_layout(
            template="plotly_white",
            title=dict(
                text=title,
                font=dict(size=14, color="#0F172A", family="sans serif", weight="bold")
            ),
            margin=dict(t=50, b=40, l=50, r=20),
            xaxis=dict(showgrid=True, gridcolor="#F1F5F9", linecolor="#E2E8F0"),
            yaxis=dict(showgrid=True, gridcolor="#F1F5F9", linecolor="#E2E8F0"),
            legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --------------------------------------------------
    # Pie Chart (Redesigned for Premium Light Corporate)
    # --------------------------------------------------
    @staticmethod
    def pie_chart(df, values, names, title):
        fig = px.pie(
            df,
            values=values,
            names=names,
            title=title,
            color_discrete_sequence=["#0F172A", "#10B981", "#475569", "#64748B", "#94A3B8", "#CBD5E1"]
        )
        
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hole=0.4,
            marker=dict(line=dict(color='#FFFFFF', width=2))
        )
        
        fig.update_layout(
            template="plotly_white",
            title=dict(
                text=title,
                font=dict(size=14, color="#0F172A", family="sans serif", weight="bold")
            ),
            margin=dict(t=50, b=20, l=20, r=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --------------------------------------------------
    # Heatmap (Redesigned for Premium Light Corporate)
    # --------------------------------------------------
    @staticmethod
    def heatmap(df, title):
        custom_colorscale = [
            [0.0, '#F8FAFC'],
            [0.3, '#CBD5E1'],
            [0.7, '#10B981'],
            [1.0, '#0F172A']
        ]
        
        fig = go.Figure(
            data=go.Heatmap(
                z=df.values,
                x=df.columns,
                y=df.index,
                colorscale=custom_colorscale,
                showscale=True,
                hovertemplate="Country: <b>%{y}</b><br>Dimension: <b>%{x}</b><br>Score: %{z:,.3f}<extra></extra>"
            )
        )
        
        fig.update_layout(
            title=dict(
                text=title,
                font=dict(size=14, color="#0F172A", family="sans serif", weight="bold")
            ),
            template="plotly_white",
            margin=dict(t=50, b=40, l=100, r=20),
            xaxis=dict(side="top")
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --------------------------------------------------
    # Radar Chart (Redesigned for Premium Light Corporate)
    # --------------------------------------------------
    @staticmethod
    def radar_chart(df, category, value, title):
        fig = go.Figure()
        
        radar_colors = ["rgba(15, 23, 42, 0.6)", "rgba(16, 185, 129, 0.6)", "rgba(59, 130, 246, 0.6)", "rgba(99, 102, 241, 0.6)", "rgba(234, 179, 8, 0.6)"]
        line_colors = ["#0F172A", "#10B981", "#3B82F6", "#6366F1", "#EAB308"]
        
        for idx, column in enumerate(df.columns[1:]):
            color_idx = idx % len(radar_colors)
            fig.add_trace(
                go.Scatterpolar(
                    r=df[column],
                    theta=df[category],
                    fill="toself",
                    name=column,
                    fillcolor=radar_colors[color_idx],
                    line=dict(color=line_colors[color_idx], width=2),
                    hovertemplate=f"Country: <b>{column}</b><br>Dimension: %{{theta}}<br>Score: %{{r:,.3f}}<extra></extra>"
                )
            )
            
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    gridcolor="#E2E8F0",
                    linecolor="#E2E8F0",
                    tickfont=dict(size=9, color="#64748B")
                ),
                angularaxis=dict(
                    gridcolor="#E2E8F0",
                    linecolor="#E2E8F0",
                    tickfont=dict(size=10, color="#0F172A", weight="bold")
                ),
                bgcolor="#FFFFFF"
            ),
            title=dict(
                text=title,
                font=dict(size=14, color="#0F172A", family="sans serif", weight="bold")
            ),
            template="plotly_white",
            margin=dict(t=60, b=30, l=40, r=40),
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5)
        )

        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})