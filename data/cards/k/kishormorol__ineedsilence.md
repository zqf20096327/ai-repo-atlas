# kishormorol/ineedsilence

⭐ 8 · Python · MIT · 推送 2026-11-10 · [GitHub](https://github.com/kishormorol/ineedsilence) · 个人维护

**让三个 AI 评审多轮互审文档直至全部通过的 Claude Code 技能**

以 Claude Code 技能形式分发的多模型同行评审脚本：将论文分别交给三个评审模型独立阅读，各返回带位置与原文引用的问题清单；由 Claude Code 合并去重、核对文本并修复，再进入交叉质询与签核轮次，仅当全部评委绿灯且无遗留项时输出 SILENCE。面板可自定义为 2-5 个评委，支持 OpenAI 兼容 API、本地模型或任意命令行 agent。仅标准库实现，Python 3.9+，无 pip 依赖；文档全文会发送给各供应商，消耗大量配额，且不核查文献与引用真实性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三轮评审机制：独立阅读、匿名交叉质询、全绿签核，签核后改动即作废
- 评委面板可配置：内置 CLI、OpenAI 兼容端点、本地模型、自定义命令行 agent
- 配额耗尽自动换替补评委并在最终结论中点名
- 留存完整运行产物（issues.json 等）供核查，并维护本地 LESSONS.md 学习记录

## 适用场景

- 论文投稿前让多个模型评审并互相质询我的 LaTeX 手稿
- 用 --kind skill 模式审查写给 AI agent 的指令文档
- 接入本地 Ollama 模型做不外发文档的私有评审

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L9: `ineedsilence` is a skill for Claude Code. It hands your draft to
> L11: model, four judges, five), merges what they find, fixes it, and then makes the three of
> L47: **Round 1: everyone reads alone.** No judge sees another's notes. Each returns up to 25 issues,

## 星数曲线

```mermaid
xychart-beta
    title "kishormorol/ineedsilence 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-13", "2026-11-25"]
    y-axis "stars" 6 --> 9
    line [7, 8, 8]
```

2026-11-10 7 → 2026-11-25 8（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `f60a140cc69c` · [字段定义](../../DATASET.md)*
