# yuhp/opencode-models-discovery

⭐ 190 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/yuhp/opencode-models-discovery) · 个人维护

**OpenCode 插件：从 OpenAI 兼容端点动态发现并注入模型配置**

面向 OpenCode（v2 稳定、v1 兼容）的通用模型发现插件：读取任意 OpenAI 兼容 provider 的 /v1/models 端点，将发现的模型自动合并进 OpenCode 配置；支持 provider 级开关、端点覆盖、regex/字段过滤，可选从 models.dev、vLLM、LM Studio 等 8 种元数据格式补充上下文限制与能力元数据。凭据经 OpenCode 原生 /connect 流程解析，不落盘到配置或日志。提供 TUI 命令、agent 工具、XDG/host 存储两级缓存（默认关闭，TTL 24 小时）。

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

- 从任意 OpenAI 兼容 provider 端点动态发现模型并注入 OpenCode 配置
- regex id 过滤与 raw 字段 equals/match 过滤，excludeBy 优先
- 8 种元数据格式（models.dev/vllm/lmstudio/openrouter 等）可选补充能力元数据
- 凭据经 /connect 原生解析，不写入配置、缓存或日志

## 适用场景

- 本地或网关后端模型较多时免去手工逐个配置模型
- 对 provider 暴露的模型按 id 或字段做筛选后接入
- 为仅返回最小 /models 响应的服务补充上下文与能力元数据

## 场景标签

 · 领域:AI 编码工具/LLM 接入

## 证据(README 行号)

> L10: > A universal OpenCode plugin for dynamic model discovery across any OpenAI-compatible provider.
> L17: - Discovers models dynamically from provider model endpoints
> L18: - Injects discovered models into OpenCode provider config automatically

## 星数曲线

```mermaid
xychart-beta
    title "yuhp/opencode-models-discovery 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 184 --> 191
    line [185, 187, 189, 190]
```

2026-10-18 185 → 2026-10-23 190（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `60844fc0a5dd` · [字段定义](../../DATASET.md)*
