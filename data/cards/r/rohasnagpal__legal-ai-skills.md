# rohasnagpal/legal-ai-skills

⭐ 217 · JavaScript · MIT · 推送 2026-11-24 · [GitHub](https://github.com/rohasnagpal/legal-ai-skills) · 个人维护

**为律师/当事人在 Claude Code 搭建 AI 律所团队的技能包**

以 Claude Code/Codex 插件形式安装的法律技能集：模拟 1 名管理合伙人、4 名辖区法律顾问（印度/美/英/新加坡）、17 名专长律师的分工流程，内置 244 项法律技能、20 条工作流、14 个官方法律研究来源连接器，以及本地离线的期限/利息计算器与美英联合国制裁名单筛查工具。安装通过 plugin marketplace 命令完成，Node.js 18+ 仅为捆绑工具所需，法律技能本身可不依赖；输出需合格法律专业人士复核。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多角色分工：管理合伙人分派专长律师并由辖区顾问核验当地法律
- 244 项法律技能与 20 条工作流（尽调、诉讼准备、合同审查等）
- 对接 CourtListener、GovInfo、legislation.gov.uk、SEC EDGAR 等官方来源
- 制裁名单与法律计算器在本地机器运行，名单数据不上传

## 适用场景

- 把合同、邮件、截图放入文件夹，让 AI 律师团队评估是否起诉
- 按 RERA、离婚、M&A 尽调等 20 条工作流推进具体法律事务
- 本地筛查客户/对手方是否命中美英联合国制裁名单

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L14: - **1 Managing Partner:** Receives matters, assigns specialist lawyers, coordinates work and reviews final outputs.
> L20: - **244 Legal Skills:** Reusable capabilities such as contract review, legal research, due diligence, evidence anal
> L109: - **Claude Code:** run `claude plugin marketplace add rohasnagpal/legal-ai-skills`, then `claude plugin install le

## 星数曲线

```mermaid
xychart-beta
    title "rohasnagpal/legal-ai-skills 星数(近 20 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 186 --> 219
    line [188, 190, 192, 193, 194, 195, 197, 190, 201, 205, 206, 207, 208, 211, 212, 213, 214, 215, 216, 217]
```

2026-10-24 188 → 2026-11-26 217（+29）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `a1179e9bfbc0` · [字段定义](../../DATASET.md)*
