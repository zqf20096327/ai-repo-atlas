# abhijit-ubale/Tableau_Workbook_Generator

⭐ 31 · Python · MIT · 推送 2026-02-17 · [GitHub](https://github.com/abhijit-ubale/Tableau_Workbook_Generator) · 个人维护

**上传数据自动生成 Tableau 工作簿的 AI 网页应用**

基于 Streamlit 的网页应用：用户上传 CSV/Excel/JSON/Parquet 数据并指定业务目标与受众，应用经 Azure OpenAI 与 meta-prompting 分析数据结构、推荐 KPI 与图表类型，生成含计算字段（表计算、LOD 表达式）的 Tableau 工作簿（.twb/.twbx），兼容 Tableau Desktop/Server。工作流由 Langgraph 编排，带检查点恢复与错误处理。运行需配置 Azure OpenAI 凭证（.env），文件上限 100MB、建议 100 万行以内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 分析数据并自动生成完整 .twb/.twbx 工作簿
- 支持表计算与 LOD（FIXED/INCLUDE/EXCLUDE）表达式
- Langgraph 工作流编排，带检查点恢复
- 支持 CSV/Excel/JSON/Parquet 四种数据源

## 适用场景

- 我没有 Tableau 开发经验，想让 AI 根据业务目标直接产出可用仪表盘
- 给管理层快速生成 KPI 与趋势分析的执行摘要型仪表盘
- 批量探索数据并自动获得图表类型与可视化建议

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Transform your data into compelling Tableau dashboards with the power of AI. This production-grade application uses 
> L10: - **📊 Automatic Dashboard Generation**: Creates complete Tableau workbooks (.twb/.twbx)
> L193: - Creates complete Tableau workbook

## 星数曲线

```mermaid
xychart-beta
    title "abhijit-ubale/Tableau_Workbook_Generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `193a5f5d4e41` · [字段定义](../../DATASET.md)*
