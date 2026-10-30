# withcatai/catai

⭐ 498 · TypeScript · MIT · 推送 2025-11-16 · [GitHub](https://github.com/withcatai/catai) · [官网](https://withcatai.github.io/catai/) · 组织维护

**本地运行 GGUF 模型的 Node.js AI 助手，带聊天界面与 API**

基于 node-llama-cpp 在本地运行 GGUF 模型的桌面/服务器工具：通过 npm 全局安装，CLI 下载模型后启动服务，提供网页聊天界面（实时流式输出、模型下载管理）与 HTTP API，并暴露 Node.js 开发 API（createChat、LlamaJsonSchemaGrammar 等）供集成。跨 Windows/Linux/macOS，数据默认存于 ~/catai。灵感来自 Node-Llama-Cpp 与 Llama.cpp。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 安装任意 GGUF 模型并一键启动本地服务
- 网页聊天界面与实时文本流式输出
- HTTP Web API 与 Node.js 开发 API（含 JSON Schema 语法约束）
- 支持 Windows/Linux/macOS 多平台

## 适用场景

- 在本机跑 GGUF 模型并通过网页聊天界面对话
- Node.js 应用通过 API 调用本地 LLM
- 统一管理本地模型下载与推理服务

## 场景标签

`AI 助手` `聊天机器人` `推理引擎` · 领域:对话与助手

## 证据(README 行号)

> L11: Run GGUF models on your computer with a chat ui.
> L25: catai install qwen3-4b-q4_k_m
> L26: catai up

## 星数曲线

```mermaid
xychart-beta
    title "withcatai/catai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 497 --> 499
    line [498, 498]
```

2026-10-18 498 → 2026-10-30 498（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `36e05703ba9a` · [字段定义](../../DATASET.md)*
