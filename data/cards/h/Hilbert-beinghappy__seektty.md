# Hilbert-beinghappy/seektty

⭐ 195 · TypeScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/Hilbert-beinghappy/seektty) · 个人维护 · 中文 README

**DeepSeek Harness 的 Claude Code 风格终端工作区界面**

SeekTTY 是 DeepSeek Harness（dsh）的终端前端插件：通过 dsh plugin 安装后，以单一终端工作区暴露 Harness 的 Agent、Session、模型、权限、Settings、Profile、插件与持久化服务，运行时状态仍由 Harness 持有。能力覆盖流式 Markdown 对话、会话管理、Agent 预设切换、图片附件、/plan、/goal、子代理树浏览、插件中心与 MCP 管理、VS Code 主题导入与中英文切换。可选 Clarify 插件提供引导式需求澄清工作流，配合 Harness 原生 /plan 生成实现方案。要求 Node.js 22.19+，测试配对 dsh 0.2.0-rc.2，经 pnpm/npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从运行中的 Harness 动态发现模型、Provider、Agent 预设、Skills 与 MCP，无需硬编码
- 会话创建/恢复/分叉/归档、队列化提示与多类交互应答
- 可选 Clarify 引导式需求澄清，产出可审阅 Draft 后交由 /plan
- VS Code 主题导入、透明终端适配与中英文实时切换

## 适用场景

- 在终端中以 Claude Code 风格界面使用 DeepSeek 编码代理
- 通过引导式澄清把模糊需求整理成可执行的实现计划
- 在统一终端里管理 Profiles、插件、Skills 与 MCP 配置

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L29: Run `deepseek` from a project directory to use the native Agent, Session, model, permission, Settings, Profile, plu
> L31: Models, Providers, Agent Presets, permissions, commands, tools, Settings, Skills, MCP servers, and marketplace sour

## 星数曲线

```mermaid
xychart-beta
    title "Hilbert-beinghappy/seektty 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 194 --> 197
    line [196, 195, 195]
```

2026-10-18 196 → 2026-10-27 195（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `215f9b9a7a8a` · [字段定义](../../DATASET.md)*
