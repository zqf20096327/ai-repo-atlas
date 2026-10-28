# roampal-ai/roampal-core

⭐ 54 · Python · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/roampal-ai/roampal-core) · [官网](https://roampal.ai) · 个人维护

**为 AI 编程助手提供基于结果评分的持久记忆 MCP 服务器**

面向 Claude Code 与 OpenCode 用户的持久记忆服务：在用户输入前自动注入相关历史上下文（Claude Code 用 hooks，OpenCode 用插件），对话结束后对建议进行结果评分，好建议晋升、坏建议降级。记忆分为 working/history/patterns/memory_bank/books 五个集合，各有生命周期；存储基于 ChromaDB，检索用 TagCascade（标签优先+交叉编码器重排）。Roampal 本体在 CPU 上运行，评分可选用本地模型（Ollama/LM Studio）或 Zen 免费模型（需显式选择）。通过 pip 安装，`roampal init` 自动检测并配置已装工具，支持多项目独立记忆 profile。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于结果评分的记忆晋升/降级循环（好建议晋升、坏建议降级）
- 自动上下文注入：Claude Code hooks / OpenCode 插件两种机制
- 五个记忆集合（working/history/patterns/memory_bank/books）分生命周期管理
- 支持按项目/客户端隔离的命名记忆 profile

## 适用场景

- 让 AI 编程助手跨会话记住我的偏好与已验证的解决方案
- 在多个项目间隔离不同的记忆库
- 用本地小模型（如 Ollama）做对话评分，数据不出本机

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Outcome-Based Persistent Memory MCP Server
> L14:  Two commands. Your AI coding assistant gets outcome-based memory.
> L49: ||Claude Code|OpenCode|

## 星数曲线

```mermaid
xychart-beta
    title "roampal-ai/roampal-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-28 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ae15a218b561` · [字段定义](../../DATASET.md)*
