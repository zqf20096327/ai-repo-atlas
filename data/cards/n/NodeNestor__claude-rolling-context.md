# NodeNestor/claude-rolling-context

⭐ 33 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/NodeNestor/claude-rolling-context) · 个人维护

**Claude Code 滚动上下文压缩代理，避免长会话撞上下文墙**

以本地 MITM 代理形式工作的 Claude Code 插件：通过设置 HTTPS_PROXY 截获发往 Anthropic API 的会话流量，当上下文超过 100K token 触发值时在后台异步压缩旧消息（结构化摘要：目标/时间线/当前状态/关键细节），近期消息保持原文，完整 JSONL 转录保留。默认复用会话自身请求形状生成摘要以利用 prompt cache，也可配置独立的 Anthropic 或 OpenAI 兼容端点（Ollama、vLLM 等）做压缩。纯 Python 标准库实现，需 Python 3.7+。

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

- MITM 代理按内容哈希透明替换已压缩消息，完全无状态
- 仅压缩旧消息，近期上下文逐字保留，摘要滚动合并
- 100K 触发、后台异步压缩，不阻塞会话
- 压缩请求可走任意 Anthropic/OpenAI 兼容端点（Ollama/vLLM/OpenRouter 等）

## 适用场景

- 长会话编码时自动控制上下文长度避免撞墙
- 降低长会话逐轮重复计费的输入成本
- 在第三方 Anthropic 格式端点上保持压缩可用（带回退）

## 场景标签

 · 领域:LLM 基础设施/上下文管理

## 证据(README 行号)

> L7: A transparent proxy that gives Claude Code **rolling context compression** — old messages get automatically summariz
> L54: Claude Code  ──HTTPS_PROXY──►  Rolling Context MITM (:5590)  ──►  core (:5588)  ──►  Anthropic API

## 星数曲线

```mermaid
xychart-beta
    title "NodeNestor/claude-rolling-context 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `cdfd4b06e77d` · [字段定义](../../DATASET.md)*
