# microsoft/vscode-data-analysis-for-copilot

⭐ 56 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/microsoft/vscode-data-analysis-for-copilot) · 组织维护

**让 Copilot 代理执行 Python 完成数据分析的 VS Code 扩展**

VS Code 扩展，为 GitHub Copilot 的 @data 代理提供代码执行工具：通过 Pyodide 在浏览器侧执行 Python，LLM 可请求运行代码并获取结果，出错时可自动重试。面向数据科学用户，支持 CSV 文件分析、统计度量与预测模型、可视化生成，编辑器/资源管理器右键集成分析入口，分析所用代码可导出为 Jupyter Notebook 或 Python 文件。README 可见范围内未给出安装命令或硬件要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供工具让 LLM 经 Pyodide 执行 Python 并返回结果
- 错误或失败时可智能重试以获得更合适的执行结果
- 支持 CSV 分析、可视化生成与追问
- 分析代码可导出为 Jupyter Notebook 或 Python 文件

## 适用场景

- 在 VS Code 里让 Copilot 分析我的 CSV 文件
- 通过追问生成图表等可视化
- 把 AI 分析用的代码导出成 Notebook 复用

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Data Analysis for Copilot empowers people in data science field. From cleaning up user's .csv file to performing hig

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/vscode-data-analysis-for-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-26 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bb1e1f87ce7a` · [字段定义](../../DATASET.md)*
