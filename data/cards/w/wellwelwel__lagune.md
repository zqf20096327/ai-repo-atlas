# wellwelwel/lagune

⭐ 173 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/wellwelwel/lagune) · [官网](https://lagune.ai) · 个人维护

**让 AI agent 对任意语言项目做安全加固与审计的命令工具集**

运行于 Node.js 之上的安全工作流工具：通过 npx 安装后，在项目中以斜杠命令驱动 AI agent 执行五步 Blue Team 流程——设立安全章程（charter）、读取代码并映射风险（detect）、生成防御计划（plan）、逐项应用修复（harden）、验证修复（verify）；另有 /lagune 命令在开发过程中随时强化安全，以及从文章/漏洞利用学习新安全子技能的 specialize 命令。声明支持 78 种 agent、任意编程语言，无需 API key；提供本地私有 dashboard（实时刷新、浏览器内管理），要求系统装有 Node.js LTS 和至少一种受支持的 agent。

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

- 五步 Blue Team 流程命令：charter/detect/plan/harden/verify
- 声明支持 78 种 agent 与任意编程语言，无需 API key
- 本地私有 dashboard，可在浏览器内安装、更新与管理
- specialize 命令可从文章或漏洞利用学习新的安全子技能

## 适用场景

- 开发过程中让 AI agent 持续执行项目安全加固
- 对已有代码库做风险映射并生成可执行的防御计划
- 把检测到的发现转成可运行的负责任披露证明

## 场景标签

`网络安全` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: **Lagune** helps your AI agent make a project more secure. You point it at your code, and the agent figures out what
> L81: Once **Lagune** is set up in your project, your **AI** agent unlocks a set of slash commands:
> L98: |#|Command|What it does for you|

## 星数曲线

```mermaid
xychart-beta
    title "wellwelwel/lagune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 172 --> 174
    line [173, 173]
```

2026-10-18 173 → 2026-10-29 173（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c5614b2de59b` · [字段定义](../../DATASET.md)*
