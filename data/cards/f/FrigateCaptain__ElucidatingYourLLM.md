# FrigateCaptain/ElucidatingYourLLM

⭐ 14 · MIT · 推送 2026-10-11 · [GitHub](https://github.com/FrigateCaptain/ElucidatingYourLLM) · 个人维护

**给 Cursor/Claude Code/OpenClaw 的 AI 助手规则集，减少幻觉与失控行为**

一套按平台（Cursor、Claude Code、OpenClaw）和语言（英/俄）组织的 AI 助手规则文件仓库，配套逐步的 AI 辅助部署流程（deploy-workflow.md），可让 AI 读取规则、检查与现有配置的冲突后自动部署，也可手动复制文件到项目根目录。默认加载约 4,100–4,350 tokens（约占 200K 上下文的 2%）。规则在 Claude Opus/Sonnet 4.6 起的模型上开发测试，并对 Grok 4.7 的过度字面执行做了放宽修订。另有 18 条进阶规则与付费课程，需通过课程或订阅获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按平台×语言组织的 Principal 规则集，含 AI 辅助自动部署流程
- 默认加载约 4,100–4,350 tokens（200K 上下文的约 2%）
- 规则在 Claude Opus/Sonnet 4.6+ 开发测试，并对 Grok 4.7 做了字面性放宽修订
- 配套结构模板仓库（含 AI 自动部署）可组合使用

## 适用场景

- 给我的 Cursor/Claude Code 助手部署一套基础行为规则
- 通过 AI 自动读取 deploy-workflow 完成规则部署
- 配合结构模板让工作区对人和 AI 都可预期

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: **EN:** A battle-tested **set of main and core rules** for your AI assistants (Cursor, Claude Code, OpenClaw) — read
> L15: A battle-tested **set of main and core rules** for your AI assistants — ready to deploy. Comes with step-by-step AI
> L103: **Option 2 — manual:**

## 星数曲线

```mermaid
xychart-beta
    title "FrigateCaptain/ElucidatingYourLLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b85e74ffcb28` · [字段定义](../../DATASET.md)*
