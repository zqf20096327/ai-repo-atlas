# mrwogu/promptscript

⭐ 379 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/mrwogu/promptscript) · [官网](https://getpromptscript.dev/) · 个人维护

**面向企业的 Prompt-as-Code 编译器：一份 AI 规则编译给 50 个工具**

开源编译器，用 .prs 源文件统一定义 AI 编码助手的指令、规范、技能、Agent、MCP 服务器、hooks 与策略，经 promptscript.yaml 配置目标后编译为 Claude Code、GitHub Copilot、Cursor 等 50 个工具各自的原生文件（如 CLAUDE.md、.cursor/rules）。机制包括继承与组合（@inherit/@use/@extend/@override）、lockfile 锁定远程依赖、离线 vendor 模式、模型别名映射与内置安全扫描（检测提示注入面）。支持 npm 全局安装或 Docker 运行，提供浏览器 Playground。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一源编译出 50 个 AI 编码工具的原生配置文件
- @inherit/@use/@extend/@override 分层组合与 lockfile 可复现构建
- 模型别名跨目标映射，不支持的目标给出警告而非写入
- prs validate 内置安全扫描，检查指令与导入技能的注入面

## 适用场景

- 团队同时使用多个 AI 编码工具时统一维护规则文件
- 平台团队通过继承与 Git registry 向数百个仓库下发标准
- 在 CI 中校验与审计 AI 指令变更

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L27: PromptScript is an open-source compiler for AI coding agent rules. `.prs` sources
> L31: `.github/copilot-instructions.md` for GitHub Copilot, `.cursor/rules` for Cursor, and 47 more

## 星数曲线

```mermaid
xychart-beta
    title "mrwogu/promptscript 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 386 --> 388
    line [387, 387]
```

2026-10-18 387 → 2026-10-21 387（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `310026609651` · [字段定义](../../DATASET.md)*
