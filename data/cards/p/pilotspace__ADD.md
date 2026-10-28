# pilotspace/ADD

⭐ 19 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/pilotspace/ADD) · [官网](https://www.npmjs.com/package/@pilotspace/add) · 组织维护

**给 AI 编码代理的技能文件：让每次改动留下规则、假设与可复核证据**

ADD 是一个安装到项目中的单个 skill 文件（无引擎、无 CLI），面向使用 Claude Code、Codex、Cursor、Copilot、Gemini 等 AI 编码代理的开发者。工作流为'一个任务、三个节拍、一个文件'：Direction 阶段写下规则、假设与失败的检查并以 freeze 提交封存；Build 阶段使检查变绿而不动封存文件；Verify 阶段产出 PASS/RISK-ACCEPTED/HARD-STOP 判定并提交。状态存于磁盘而非对话，通过 npm、pip 或 Claude Code 插件安装。README 给出基于 300 个 SWE-bench Lite 问题的自测数据，并说明成本约为原代理的 1.8 倍。

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

- 每个变更在 .add/tasks/<slug>.md 留下规则、假设与检查
- 检查在构建前以 freeze 提交封存，验证产出可重跑的判定
- 对规格沉默处采取最小权限解释并记录 ASSUMPTION
- 大多数小改动走 Quick 通道：一个红→绿测试、一次提交、无任务文件

## 适用场景

- 我在多里程碑、多协作者的项目中让 AI 编码决策留档可审
- 我希望每次 AI 修复都附带测试且验证后才算完成
- 我想让下一个会话或队友直接读到改动的意图而非反推代码

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L41: our benchmark. What it does not leave behind is the *why*. ADD 4.0 is one skill file, with no
> L120: ADD works with the agent you already use (Claude Code, Codex, Cursor, Copilot, Gemini) and installs
> L170: **One task · three beats · one file.** Every change worth a contract is one task file at

## 星数曲线

```mermaid
xychart-beta
    title "pilotspace/ADD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `38a8d75f14ea` · [字段定义](../../DATASET.md)*
