# AntonioTF5/soul-spec

⭐ 15 · JavaScript · MIT · 推送 2026-04-21 · [GitHub](https://github.com/AntonioTF5/soul-spec) · 组织维护

**AI agent 持久身份的开放文件格式规范与校验工具**

定义 .soul.md 开放文件格式，用 YAML frontmatter 描述 AI agent 的身份（名称、版本、性格、价值观等），可选 Markdown 正文补充，任何可读 YAML 的工具均可解析，可在平台间移植。仓库提供规范（SPEC.md）、JSON schema、11 个示例 soul 文件与 CLI 工具（校验/评分/生成），另有 Claude Desktop 用的 MCP 服务器。参考实现为 Agenturo 平台，可将 soul 文件部署为在线 agent。MIT 许可，接受贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML frontmatter + Markdown 正文的平台中立身份格式
- soul-md-cli 提供校验、评分与生成功能
- 11 个可直接使用的示例 soul 文件
- 提供 Claude Desktop 的 MCP 服务器工具

## 适用场景

- 为 AI agent 定义可版本化、可跨平台移植的身份描述
- 在部署或迁移 agent 时保持一致的持久身份
- 验证 soul 文件是否符合规范

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **SOUL.md is an open file format for giving AI agents persistent identity.**
> L39: The format was created by Anton Agafonov at Agenturo — a platform where every agent is defined by a SOUL.md file an
> L108: |`soul-md-cli`|CLI validator, scorer, and generator — `npx soul-md-cli validate my-agent.soul.md`|

## 星数曲线

```mermaid
xychart-beta
    title "AntonioTF5/soul-spec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9d1b1198e9ac` · [字段定义](../../DATASET.md)*
