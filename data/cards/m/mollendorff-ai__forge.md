# mollendorff-ai/forge

⭐ 10 · Rust · Apache-2.0 · 推送 2026-11-18 · [GitHub](https://github.com/mollendorff-ai/forge) · [官网](https://mollendorff-ai.github.io/forge/) · 组织维护

**面向 FP&A 与 AI agent 的纯文本财务建模引擎**

Rust 编写的财务建模引擎：读取 YAML 格式的模型（输入、公式、表格、情景），用 203 个 Excel 风格函数计算，并提供电子表格插件式的能力（蒙特卡洛、龙卷风图、决策树、实物期权、贝叶斯网络）。同一引擎以命令行、MCP server 和浏览器应用（编译为 WebAssembly 的 Forge Studio）三种形式运行，浏览器端数据留在本地设备、可离线使用。通过 2,160 条与 Gnumeric、R 的对比测试及 CI 中的批量生成用例做校验。目前为 release candidate 且自述为 R&D 原型，export 对部分公式与 scenarios 的 Excel 往返存在已知限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- YAML 纯文本模型，203 个 Excel 风格函数加蒙特卡洛、决策树等扩展分析
- 同一引擎支持命令行、MCP server（供 AI agent 调用）与 WebAssembly 浏览器应用
- 2,160 条公式测试与 Gnumeric/R 对比，CI 中每周生成 27,000 个用例复核
- 浏览器端无服务器计算、无账号、可离线运行，数据留在本地

## 适用场景

- 用纯文本 + git diff 管理财务模型与情景假设
- 让 AI agent 编写模型 YAML，由 Forge 做确定性计算
- 在无 AI 的月末流水线中作为可复现的计算器，输出 JSON/CSV/工作簿
- 在手机或笔记本浏览器中离线拖动输入做 what-if 分析

## 场景标签

`数据分析` `金融量化` · 领域:效率与自动化

## 证据(README 行号)

> L12: Forge reads a financial model written in YAML (inputs, formulas, tables, scenarios) and calculates it with 203 Exce
> L36: 1. **A person alone.** A model is a text file: change an input, `forge calculate`, and `git diff` shows every resul
> L39: 4. **A pipeline with AI.** An agent reads a new report and writes or updates the model, Forge checks and calculates


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `0735664fe214` · [字段定义](../../DATASET.md)*
