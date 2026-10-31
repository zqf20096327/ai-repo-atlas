# Fu-Jie/mimo-free-api-mcp

⭐ 30 · TypeScript · GPL-3.0 · 推送 2026-04-26 · [GitHub](https://github.com/Fu-Jie/mimo-free-api-mcp) · [官网](https://github.com/Fu-Jie/mimo-free-api-mcp) · 个人维护 · 中文 README

**逆向小米 MiMo 官网构建的 OpenAI 兼容网关与 MCP 插件服务**

基于 MiMo 官网（aistudio.xiaomimimo.com）逆向的代理网关：以 OpenAI 兼容 API 暴露 mimo-v2.5/v2.5-pro 等模型，支持思维链流式输出、图像/视频/音频分析、联网搜索；同时在 8001 端口提供 MCP Server（2025 Streamable HTTP 标准），为 Claude/Cursor 等客户端提供 search 与 vision 两个工具。凭证通过 .env 或 Bearer Header 传入，本地文件经 Docker 挂载 /app/media 访问。README 声明原生 Function Calling 不稳定，不建议在 Agent 中使用；项目仅供学术交流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API 暴露 mimo-v2.5 系列模型，流式含 reasoning_content
- MCP Server 提供 search 与 vision 工具，供 Claude/Cursor 集成
- 视觉分析支持 URL、Base64 与挂载的本地文件三种来源
- 旧版模型 ID（mimo-v2-omni/v2-pro）自动路由至 V2.5 系列

## 适用场景

- 在 OpenAI 兼容客户端中调用 MiMo 模型进行对话或多模态分析
- 为 Claude/Cursor 添加联网搜索与视觉分析 MCP 工具
- 通过思维链后缀获取推理过程输出

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: > 基于小米大模型（MiMo）官方网站（aistudio.xiaomimimo.com）逆向构建的高级 OpenAI 兼容网关 + 原生 MCP 插件集成。现已全量适配 **MiMo V2.5 全模态** 系列，支持 **Think
> L13: 5. **Native MCP Server**: 集成最新 MCP 标准。赋予 Claude / Cursor 等客户端原生的 **联网搜索 (`search`)** 与 **视觉分析 (`vision`)** 能力。

## 星数曲线

```mermaid
xychart-beta
    title "Fu-Jie/mimo-free-api-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-31 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `95635c650439` · [字段定义](../../DATASET.md)*
