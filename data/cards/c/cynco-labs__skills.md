# cynco-labs/skills

⭐ 15 · Python · NOASSERTION · 推送 2026-03-24 · [GitHub](https://github.com/cynco-labs/skills) · 组织维护

**面向 Claude Code 的马来西亚会计技能：银行流水生成财务报表与税务计算**

一个 Claude Code 技能包（SKILL.md 结构化提示词 + 参考文件 + 脚本）：把银行对账单等客户文档交给 Claude，按 8 阶段流程生成本着权责发生制的财务报表、工作底稿与税务计算，遵循 MPERS/MFRS/ITA 1967，支持独资、合伙、sdn bhd、berhad、NGO 五类主体。分层加载结构使 agent 按需读取内容；处理在本地进行，OCR 例外。需 Python 3.10+ 及若干库，npx 或 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 阶段固定流程：从客户资料到财务报表与税务计算
- 覆盖 5 类法律主体与对应准则（S21A/MPERS/MFRS/Societies Act）和税表
- 银行对账单为唯一硬性输入，支持全量/部分/仅银行流水三档处理
- 本地处理数据，无遥测，MIT 许可

## 适用场景

- 我在马来西亚的会计师事务所用它跑客户账目全流程
- 我作为创始人用自己的 sdn bhd 银行流水生成工作底稿和报表
- 簿记员或会计学生用它辅助记账但保留人工复核

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: a claude code skill for malaysian accounting — drop in your bank statements, get back accrual-basis financial statem
> L134: a claude code skill — a structured prompt + reference files that teaches claude how to do a full malaysian account
> L100: point claude at a folder with bank statements and say:

## 星数曲线

```mermaid
xychart-beta
    title "cynco-labs/skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `03a25664d8ac` · [字段定义](../../DATASET.md)*
