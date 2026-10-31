# Igualguana/AUTOCAD-ELECTRICAL-MCP

⭐ 19 · Python · AGPL-3.0 · 推送 2026-04-15 · [GitHub](https://github.com/Igualguana/AUTOCAD-ELECTRICAL-MCP) · 个人维护

**用自然语言控制 AutoCAD Electrical 的 MCP 服务器与本地 Web 控制台**

面向 AutoCAD Electrical 2025 用户的 AI 控制平台：将 46 个 AutoCAD 操作（2D/3D 绘图、电气原理图、导线、元件、报表、项目管理）封装为 MCP 工具，供 AI 助手以自然语言调用。提供两种独立模式：Mode A 通过 Claude Code CLI 接入 Claude API，Mode B 为 FastAPI + 原生 JS 的本地 Web 仪表盘，配合 Ollama 离线运行；另支持 OpenAI/Groq/LM Studio 切换。经 pywin32 COM 自动化直连 AutoCAD，要求 Windows 10/11 且 AutoCAD 处于运行状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 46 个 MCP 工具覆盖 2D/3D 绘图、电气符号、导线编号与 BOM 报表
- 双模式：Claude Code CLI（MCP）或本地 Web 仪表盘（Ollama 离线）
- 复合绘图：单条指令触发多步执行计划（3D 螺丝 5 步、电气原理图 31 步）
- 关键词预路由与 34 个工具名别名纠正（修正 AI 幻觉）

## 适用场景

- 用自然语言让 AI 在 AutoCAD Electrical 中绘制电气原理图与 3D 模型
- 在 Claude Code 中以 MCP 工具操作 AutoCAD 生成图纸与 BOM
- 无 API key 时用本地 Ollama 通过 Web 仪表盘离线控制 AutoCAD

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L22: **AUTOCAD-ELECTRICAL-MCP** bridges AI models and AutoCAD Electrical 2025. It exposes **46 AutoCAD operations** as M
> L33: |**Mode B — Web Dashboard**|Browser `localhost:8080`|Ollama (local)|Ollama installed|

## 星数曲线

```mermaid
xychart-beta
    title "Igualguana/AUTOCAD-ELECTRICAL-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1fef0f2f81d9` · [字段定义](../../DATASET.md)*
