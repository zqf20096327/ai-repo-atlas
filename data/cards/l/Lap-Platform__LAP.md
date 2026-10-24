# Lap-Platform/LAP

⭐ 346 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/Lap-Platform/LAP) · [官网](https://lap.sh/) · 组织维护

**把 API 规范编译为压缩的 Agent 原生格式的 CLI 平台**

Lean API Platform 提供 lapsh 命令行工具与注册表：将 OpenAPI、GraphQL、AsyncAPI、Protobuf、Postman、Smithy 六种格式的 API 规范编译为自称最多缩小 10 倍的 .lap 精简格式，保留端点、参数与类型约束；并可将 .lap 转回 OpenAPI。注册表收录 1500+ 预编译规范，支持以 agent skill 形式安装到 Claude Code、Cursor、Codex、OpenClaw，也提供 LangChain 加载器与 Python/TypeScript SDK。面向需要让 LLM agent 正确调用 API 的开发者。基准测试数据（0.399→0.860 准确率、35% 降本）为项目自述，未见同行评审。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种输入格式编译为 .lap，格式自动检测
- 注册表含 1500+ 预编译规范，lapsh search/get/install 管理
- lapsh convert 可从 .lap 转回 OpenAPI
- 生成 agent skill 并安装到 Claude Code/Cursor/Codex/OpenClaw

## 适用场景

- 为我的 coding agent 提供准确 API 规范以减少调用幻觉
- 压缩大型 OpenAPI 规范以降低 agent 的 token 成本
- 检测 API 规范的破坏性变更（lapsh diff）

## 场景标签

 · 领域:AI agent 工具链/API 规范

## 证据(README 行号)

> L5: **Agent-Native API specs. Verified, compressed, ready to install.**
> L50: Install the LAP skill so your agent can search, compile, and manage APIs automatically:
> L147: |**Compiler**|Any spec → `.lap`|`lapsh compile api.yaml`|

## 星数曲线

```mermaid
xychart-beta
    title "Lap-Platform/LAP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 345 --> 347
    line [346, 346]
```

2026-10-18 346 → 2026-10-24 346（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `02a8b6eccd73` · [字段定义](../../DATASET.md)*
