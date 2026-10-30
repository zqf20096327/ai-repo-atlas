# oomol-lab/wanta

⭐ 82 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/oomol-lab/wanta) · [官网](https://wanta.ai) · 组织维护 · 中文 README

**开源桌面 Agent 宿主：承载自带模型/Agent 与 1400+ 应用连接**

由 OOMOL 开发的 Electron 桌面应用，作为通用桌面 Agent 宿主：内置 Agent 使用 Wanta 托管模型或用户自带的 OpenAI 兼容 API key，运行时固定为 OpenCode（opencode-ai@1.18.30 以 loopback sidecar 方式启动）；也可接入 Claude Code、Codex、Grok 等外部 Agent，保留其本地账户与原生模型。通过 OpenConnector 生态连接 1,400+ 应用、10,000+ 预置 Action，OAuth 凭据不进入 Agent。提供本地文件/shell/浏览器/知识访问、权限审批流程、Artifacts 面板与团队工作区。可 fork 定制并分发自有品牌桌面 Agent；自托管 OpenConnector 的应用内配置为规划中功能。

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

- 内置 Agent 固定使用 OpenCode 运行时（loopback serve sidecar + SDK 驱动）
- BYOA 适配层接入 Claude Code/Codex/Grok，保留各自本地账户与模型配额
- 经 OpenConnector 连接 1,400+ 应用、10,000+ 预置 Action，凭据不进入 Agent 上下文
- 本地 BYOK 模式无需账户即可运行；支持 fork 定制分发

## 适用场景

- 用自带 API key 在本地运行一个通用工作 Agent
- 让 Agent 在同一工作区中结合本地工具与经授权的 SaaS 操作
- 团队共享连接与技能，按命名权限规则限制成员可用的 Action
- fork 桌面基础框架，打包成自己产品的领域 Agent

## 场景标签

`工作流自动化` `编码 Agent` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L9: Run the built-in Agent with Wanta-hosted models or your own OpenAI-compatible API key. Or bring
> L171: Wanta uses OpenCode as the pinned runtime for the built-in Agent and supports external Agents through
> L177: The application starts the pinned `opencode-ai@1.18.30` binary as a loopback-only `opencode serve`

## 星数曲线

```mermaid
xychart-beta
    title "oomol-lab/wanta 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-30 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `066094d8f823` · [字段定义](../../DATASET.md)*
