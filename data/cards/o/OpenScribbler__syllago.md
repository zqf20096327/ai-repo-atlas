# OpenScribbler/syllago

⭐ 15 · Go · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/OpenScribbler/syllago) · [官网](https://syllago.dev) · 组织维护

**AI 编码工具配置内容的转换、打包与分发管理系统**

面向同时使用多种 AI 编码工具（Claude Code、Cursor、Gemini CLI、Copilot 等 15 种）的开发者与团队：把 rules、skills、agents、hooks、MCP 配置等内容统一到规范中间格式，再自动转换为目标工具的原生格式安装。采用 hub-and-spoke 转换模型，新增 provider 只需两向转换。支持 git 注册表分发、loadout 打包、隐私门禁、基于 Sigstore/Rekor 的 MOAT 签名信任层，以及 Linux 下 bubblewrap 沙箱。Go 编写，提供 CLI 与 TUI。

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

- hub-and-spoke 转换模型：内容统一规范格式后按需转换到各 provider 原生格式
- 支持 15 种 AI 编码工具的 rules/skills/agents/MCP/hooks/commands 管理
- MOAT 信任模型：注册表与内容经 Sigstore keyless 签名、Rekor 透明日志、三级信任门槛
- git 注册表团队分发与隐私门禁（私有注册表内容禁止流向公共注册表）

## 适用场景

- 把 Claude Code 的规则与技能迁移到 Cursor、Gemini CLI 等其他工具使用
- 团队通过 git 注册表统一分发和维护 AI 工具配置
- 以 loadout 为单位打包整套 AI 工具配置并按角色应用
- 在 CI 中用 --json 输出审计 AI 工具内容与信任层级

## 场景标签

 · 领域:开发者工具/AI 工具链管理

## 证据(README 行号)

> L13: AI coding tools like Claude Code, Cursor, Gemini CLI, Copilot, and Amp each store rules, skills, agents, and config
> L83: Syllago uses a **hub-and-spoke conversion model**. When you add content from a provider, syllago converts it into i
> L108: |Tool|Rules|Skills|Agents|MCP|Hooks|Commands|

## 星数曲线

```mermaid
xychart-beta
    title "OpenScribbler/syllago 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `05e314c08e32` · [字段定义](../../DATASET.md)*
