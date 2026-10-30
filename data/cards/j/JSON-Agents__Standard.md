# JSON-Agents/Standard

⭐ 20 · Python · Apache-2.0 · 推送 2025-11-12 · [GitHub](https://github.com/JSON-Agents/Standard) · [官网](https://JSONAgents.org) · 个人维护

**描述 AI agent 的通用 JSON 规范：可移植的 agent 清单格式**

基于 RFC 8259 与 JSON Schema 2020-12 的开放规范，定义 Portable Agent Manifest（PAM）用于描述 agent 的能力、工具、运行时与治理。采用 core/exec/gov/graph 四个模块化 profile，包含 ajson:// URI 方案、策略表达式语言、7 类标准能力 schema 与多 agent 图编排定义，并提供到 LangChain、OpenAI、AutoGen、MCP 等框架的双向映射。Python 验证器已发布（47/47 测试通过），JS/Go 验证器与转换工具尚未提供。规范处于 v1.0.0 草案状态，可能发生破坏性变更，未获标准组织正式采纳。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Portable Agent Manifest 单文件描述 agent 能力/工具/运行时/治理
- core/exec/gov/graph 四 profile 模块化组合
- ajson:// URI 方案与策略表达式语言的形式化定义
- 与 LangChain/OpenAI/AutoGen/MCP 的双向转换映射

## 适用场景

- 在不同 agent 框架间迁移和转换 agent 定义
- 构建可发现的 agent 注册表或市场
- 企业场景下为 agent 附加策略与审计治理
- CI/CD 流水线中做 schema 校验

## 场景标签

 · 领域:AI agent 规范/互操作

## 证据(README 行号)

> L26: **JSON Agents** defines an open, JSON-native specification for describing AI agents, their capabilities, tools, run
> L31: - **Framework-agnostic**: Works with LangChain, OpenAI, AutoGen, MCP, and more
> L133: JSON Agents provides bidirectional conversion with major frameworks:

## 星数曲线

```mermaid
xychart-beta
    title "JSON-Agents/Standard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `eac14831355b` · [字段定义](../../DATASET.md)*
