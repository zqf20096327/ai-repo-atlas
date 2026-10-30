# rookiestar28/ComfyUI-Doctor

⭐ 77 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/rookiestar28/ComfyUI-Doctor) · 个人维护

**ComfyUI 实时诊断调试助手：捕获错误并给出修复建议**

面向 ComfyUI 的实时诊断与调试辅助自定义节点：自动捕获启动与运行时的终端错误，提取节点级上下文，按优先级给出 50+ 修复模式的本地建议，并可选接入 LLM 聊天工作流做深度排查。支持 Ollama/LM Studio 及内置提供商等白名单化 LLM 目的地，凭据加密存储并限制出站目的地；另提供 JSON 模式管理与热重载、遥测统计、OpenAPI 契约与安全审计 SOP。面向 ComfyUI 用户与自定义节点开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动拦截终端输出并提取节点级错误上下文，给出优先级修复建议
- 50+ 修复模式，支持基于 JSON 的模式管理与热重载
- 可选 LLM 聊天排查，出站目的地限白名单（Ollama/LM Studio/运营者列出的 base URL）
- 凭据加密存储，Authorization/X-API-Key 无条件脱敏

## 适用场景

- ComfyUI 报错时快速定位问题节点并获取修复建议
- 通过内置聊天与 LLM 对接做深度排障
- 审计与统计历史错误（按节点类型统计失败次数）

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: ComfyUI-Doctor is a real-time diagnostics and debugging assistant for ComfyUI. It captures runtime errors, identifie
> L15: - Sent LLM requests only to approved destinations: the built-in providers, local Ollama/LM Studio, and exact base U

## 星数曲线

```mermaid
xychart-beta
    title "rookiestar28/ComfyUI-Doctor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 75 --> 78
    line [76, 77, 77]
```

2026-10-18 76 → 2026-10-30 77（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0d7dec24bd01` · [字段定义](../../DATASET.md)*
