# tim-mccrimmon/structured-context-spec

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/tim-mccrimmon/structured-context-spec) · [官网](https://structuredcontext.dev) · 个人维护

**AI 系统结构化上下文的开放规范：创建、校验、版本化**

社区驱动的开放规范（SCS），把 AI 所遵循的上下文（禁令、带 id 的指令、事实）组织为 YAML 结构化上下文文档（SCD），经校验后由指定批准人版本化，`scs compile` 生成确定性运行时工件，可渲染为 CLAUDE.md、AGENTS.md、系统提示或网关策略并溯源到版本。分 Domain 与 Project 两层，提供三种行业本体（sdlc/cdmo/mca）。SCS 不做提示工程、RAG 或运行时投递；运行时只消费其产物。工具 0.6.0 经 pip 从 GitHub 安装，PyPI 上的 scs-tools 是旧版 0.1.0，README 明确告知不要使用。

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

- YAML SCD 三类内容：prohibitions / directives / facts
- 带命名批准人的版本化 bundle 与确定性编译工件
- Domain/Project 两层结构与 sdlc/cdmo/mca 三种行业本体
- 引用标准仅以条目形式出现（如 std:iso-13485:2016#7.3.9）

## 适用场景

- 统一管理分散在指令文件与提示中的团队 AI 规则并防止漂移
- 为受监管组织留存 AI 上下文的审批记录（谁批准、何时、哪个版本）
- 把同一份已批准上下文渲染为不同运行时所需的 CLAUDE.md/系统提示等格式

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: SCS is an open specification for the context an AI works within: the rules it follows, the
> L53: approver. `scs compile` turns it into one compact, deterministic artifact that names its
> L106: - Not a prompt engineering framework

## 星数曲线

```mermaid
xychart-beta
    title "tim-mccrimmon/structured-context-spec 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a54c85e34e9a` · [字段定义](../../DATASET.md)*
