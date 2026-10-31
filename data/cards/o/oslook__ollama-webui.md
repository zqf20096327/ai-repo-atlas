# oslook/ollama-webui

⭐ 43 · TypeScript · MIT · 推送 2026-07-17 · [GitHub](https://github.com/oslook/ollama-webui) · [官网](https://ollama.oslook.com) · 个人维护

**Ollama 本地模型的网页聊天界面，数据不出本机**

面向 Ollama 用户的 Web 前端：浏览器直接与本地 Ollama 服务通信，提供流式对话、多会话管理、对话历史、Markdown/代码高亮、模型列举与切换、服务器 URL 配置、聊天记录 JSON 导入导出；支持 DeepSeek R1 等推理模型的思考过程折叠显示与开关。提供 Docker/Docker Compose 部署（可附带 Ollama 服务）与基于 bun 的开发流程。公网部署需配置 Ollama 跨域，HTTPS 页面无法访问 http 的 Ollama 地址。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式响应与多会话管理、历史记录
- 推理模型（如 DeepSeek R1）思考过程折叠显示与开关
- 聊天记录 JSON 导入导出与设置持久化
- Docker Compose 一键部署，可附带 Ollama 服务

## 适用场景

- 在浏览器里和本地 Ollama 模型聊天，数据留在本机
- 查看 DeepSeek R1 等推理模型的思考过程
- 导出/导入聊天记录做备份

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L1: # Ollama Web UI
> L31: - Ollama installed and running on your machine
> L89: The browser talks to Ollama directly, so when this app is hosted on a public

## 星数曲线

```mermaid
xychart-beta
    title "oslook/ollama-webui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `05168b522b75` · [字段定义](../../DATASET.md)*
