# Thomaszhou22/prompt-optimizer-skill

⭐ 19 · NOASSERTION · 推送 2026-05-19 · [GitHub](https://github.com/Thomaszhou22/prompt-optimizer-skill) · 个人维护 · 中文 README

**跨平台提示词优化技能包：模板匹配+宿主 AI 优化提示词**

以 SKILL.md 技能文件形式分发的提示词优化工具，采用双引擎：3,344 条模板库匹配（整理自 7 个开源仓库、14 类）与宿主 AI 元提示优化（零额外 API 成本）。兼容 OpenClaw、Claude Code、Cursor、Gemini CLI、Cline、ChatGPT Custom GPT、Aider 等平台，各平台按文件系统能力分级降级。支持 14 类模板按需加载、5 维质量评分、迭代优化与中英双语输出。安装方式为复制文件到项目并引用，各平台存在状态持久化等差异限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双引擎：3,344 条模板库 + 宿主 AI 元提示优化，零 API 成本
- 7 个平台兼容矩阵，按平台能力自动降级（如 ChatGPT 仅 LLM 模式）
- 14 类模板按需加载（默认 Coding 类 1,672 条）
- 5 维度前后质量评分与多轮迭代优化

## 适用场景

- 在 Claude Code/Cursor 等编码助手中优化我的提示词
- 通过 Custom GPT 用 LLM 模式优化提示词
- 按需加载特定类别模板库节省 token

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **Dual-Engine Prompt Optimization Skill** — Template matching (3,344 library) + LLM meta-prompting (host AI as opt
> L110: |Platform|Files to Use|How to Install|
> L266: - **Model-Agnostic** — Works with all host AI platforms

## 星数曲线

```mermaid
xychart-beta
    title "Thomaszhou22/prompt-optimizer-skill 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30", "2026-10-31"]
    y-axis "stars" 15 --> 20
    line [16, 17, 19, 19]
```

2026-10-18 16 → 2026-10-31 19（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d3b23a3aff74` · [字段定义](../../DATASET.md)*
