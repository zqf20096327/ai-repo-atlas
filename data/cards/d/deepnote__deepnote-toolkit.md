# deepnote/deepnote-toolkit

⭐ 27 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/deepnote/deepnote-toolkit) · [官网](https://pypi.org/project/deepnote-toolkit/) · 组织维护

**驱动 Deepnote 环境的 Python 工具包：SQL、图表与 notebook 运行时**

Deepnote 官方维护的 Python 工具包，支撑 Deepnote Cloud 与开源版：启动并管理 Jupyter、Streamlit 与 LSP 服务器，提供 SQL 执行（免配数据库连接器与 SDK）、基于 Vega 的图表块（另支持 Altair/Plotly）、Deepnote 组件库（DataFrame 渲染、交互输入）、预装库的 Python 内核、Git 集成及带 per-viewer 认证的自定义 Streamlit 界面。通过 pip 安装，CLI 本地运行，服务器组件需加 [server] extras；无认证 Jupyter 仅限本地开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免数据库连接器/SDK 的 SQL 编写与执行
- Vega 图表块，另支持 Altair 与 Plotly
- 启动管理 Jupyter、Streamlit、LSP 服务器
- 预装精选库的 Python 内核与 Git/SSH 集成

## 适用场景

- 在本地搭建 Deepnote 风格的 notebook 数据分析环境
- 在 notebook 中直接写 SQL 查询数据仓库与数据库
- 基于 Streamlit 构建并运行带认证的交互应用

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L10: Deepnote Toolkit powers Deepnote Cloud and Deepnote Open Source.
> L11: It starts and manages Jupyter, Streamlit, and LSP servers, and provides runtime integrations for fast and reliable 

## 星数曲线

```mermaid
xychart-beta
    title "deepnote/deepnote-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `99844ff79e1d` · [字段定义](../../DATASET.md)*
