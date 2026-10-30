# use-ash/apex

⭐ 15 · Python · NOASSERTION · 推送 2026-09-17 · [GitHub](https://github.com/use-ash/apex) · 个人维护

**自托管多模型 AI 智能体平台：单文件服务器+记忆与技能系统**

单 Python 文件的自托管 AI 平台，提供多模型聊天（Claude/Codex/Grok/本地模型按会话路由）、持久记忆（MEMORY.md、语义搜索、Whisper 上下文注入）、可扩展技能引擎（SKILL.md 自动发现、三级风险审批）、mTLS/TLS 安全、61 个 REST 端点与管理后台，另有 iOS 原生应用与 War Room 多智能体协作。面向开发者、个人与团队。当前单用户架构；2026 年 9 月 30 日起群组频道、多智能体编排等高级功能需付费许可，服务器与 Web 端保持免费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型路由：Claude/Codex/Grok/Ollama/MLX 按会话切换
- 持久记忆系统：MEMORY.md + 语义搜索 + Whisper 上下文注入
- SKILL.md 技能引擎，三级风险审批与 /improve 自改进
- mTLS 证书认证、TLS、原子写入与凭据隔离

## 适用场景

- 在自己服务器上托管多模型 AI 后端，数据不出本地
- 跨会话记忆的项目/知识管理对话
- 通过 SKILL.md 扩展智能体能力并用面板管理
- 团队场景下的 AI 基础设施与凭据审计

## 场景标签

`模型网关` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Self-hosted AI platform with multi-model chat, persistent memory, and an extensible skills engine. One Python file
> L20: - Multi-model routing — Claude, Grok, Codex, Ollama
> L52: Claude for deep coding. Grok for live web research. Local models for free, private inference. Each conversation tar

## 星数曲线

```mermaid
xychart-beta
    title "use-ash/apex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `394fc49a2ff0` · [字段定义](../../DATASET.md)*
