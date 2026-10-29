# 2722039978-source/Noosphere

⭐ 52 · Go · MIT · 推送 2026-10-27 · [GitHub](https://github.com/2722039978-source/Noosphere) · 个人维护 · 中文 README

**面向个人用户的本地 AI 桌面工作台：对话、代码检索、记忆与运维 Agent**

Windows 优先的本地优先桌面应用：前端 React/TypeScript/Vite，桌面壳 Tauri 2，Go 后端统一管理多 Provider LLM 网关（OpenAI/DeepSeek/Claude/Gemini/Ollama，支持流式 SSE、重试与 Token 统计）、Nebula 记忆引擎（LSM-Tree + HNSW 向量索引 + BM25 + RRF 混合检索）、DevOps 运维 Agent 和 Python CodeLens 代码索引（Tree-sitter AST）。提供项目内只读 Agent 搜索与诊断，文件修改等操作需用户逐项审批并留恢复记录。仓库仅提供源码，首次使用需本地完整构建（Node/Go/Rust/Python 等多工具链），生成 release/Noosphere.exe 便携程序或 NSIS 安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Provider LLM 网关：OpenAI/DeepSeek/Claude/Gemini/Ollama，流式 SSE、重试、Token 统计
- Nebula 记忆引擎：LSM-Tree + HNSW 向量索引 + BM25 + RRF 混合检索
- 只读 Agent 项目内搜索诊断，文件修改/测试/服务操作需逐项审批并留恢复记录
- CodeLens 用 Tree-sitter 做多语言代码 AST 索引

## 适用场景

- 在本地统一工作区进行 AI 对话、代码检索与记忆检索
- 让只读 Agent 在项目范围内检查系统状态并保留证据
- 在审批控制下让 AI 提议文件修改、测试与服务启停

## 场景标签

`RAG` `AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: 本地 AI 桌面工作台，Windows 优先。前端使用 React、TypeScript 和 Vite，桌面壳使用 Tauri 2，Go 后端统一管理 AI Gateway、Nebula、DevOps 和 Python CodeLe
> L52: |AI Gateway|Go|多 Provider LLM 网关（OpenAI / DeepSeek / Claude / Gemini / Ollama），流式 SSE、重试、Token 统计、调用日志|
> L53: |Nebula|Go|记忆引擎：LSM-Tree + HNSW 向量索引 + BM25 + RRF 混合检索|

## 星数曲线

```mermaid
xychart-beta
    title "2722039978-source/Noosphere 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-29"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-19 52 → 2026-10-29 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `533d418f48eb` · [字段定义](../../DATASET.md)*
