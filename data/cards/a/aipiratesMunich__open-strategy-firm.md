# aipiratesMunich/open-strategy-firm

⭐ 4 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/aipiratesMunich/open-strategy-firm) · [官网](https://www.ai-pirates.com/open-strategy) · 组织维护

**给 AI 代理用的战略咨询技能包：从问题界定到董事会演示**

一组遵循开放 Agent Skills 格式的战略咨询技能，包含三个技能（strategy-engagement、strategy-deliverables、partner-review）与六个场景手册（增长、市场进入、扭亏、定价、并购、运营模式）。工作流覆盖问题界定、假设与证伪标准、带来源的数据、Excel 财务模型与 HTML/PPTX 演示文稿，以及模拟合伙人评审的 red-team 审查。运行于 Claude Code、Codex、Cursor、Gemini CLI 等可加载 skills 的代理环境，评估用例与分级结果随仓库发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个技能：问题界定与调研、交付物生成（Excel/幻灯片/备忘录）、合伙人式评审
- 六个场景手册：增长、市场进入、扭亏、定价、M&A、运营模式
- red-team 评审机制：数字不闭合即判 Blocker 并退回
- 评估用例与全部分级运行结果存于 evals/ 目录

## 适用场景

- 让代理对增长停滞等模糊问题给出可检验的首日答案
- 在董事会汇报前让代理审查演示文稿是否成立
- 提交 Excel 财务模型前让代理核验数字来源与一致性

## 场景标签

 · 领域:商业/咨询服务

## 证据(README 行号)

> L33: ||**strategy-engagement**|Turns a vague briefing into a sharp question, a first answer and a plan to test it. Then 
> L52: The skills follow the open Agent Skills format and run in Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, O

## 星数曲线

```mermaid
xychart-beta
    title "aipiratesMunich/open-strategy-firm 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-11-08", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-23 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a6fed3b5a79e` · [字段定义](../../DATASET.md)*
