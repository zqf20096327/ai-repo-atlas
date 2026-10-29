# vikd1000/investment-council

⭐ 82 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/vikd1000/investment-council) · 个人维护

**让 21 位传奇投资人风格 AI 辩论你的选股名单的 Claude Code 工具**

基于 Claude Code 运行的股票研究工具：输入股票代码与投资金额，Python 脚本先从 Yahoo Finance 拉取真实财务数据并计算，随后 21 位名投资人风格的分析 agent 各自打分给出买卖判断，再汇总共识分数、风险与最终报告（Markdown + 交互式 dashboard）。全程分六步执行、每步落盘可人工检查修改；数学计算与 AI 推理分离并由 validate.py 校验。支持美/加税务账户的卖出顺序建议，明确声明不构成投资建议、不执行交易。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 21 个基于真实投资风格评分规则的投资人 agent
- Python 脚本抓取 Yahoo Finance 真实数据，AI 只做推理不编数字
- 六步流程每步输出可读可改的文本文件
- 识别美国与加拿大税务账户类型（401k/IRA/TFSA/RRSP 等）的卖出顺序建议

## 适用场景

- 我想看多位风格不同的投资人视角对同一只股票的分歧与共识
- 持仓组合想获得一份带共识热力图的第二意见研究报告
- 在学习投资时观察不同投资风格如何解读同一组财务数据

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L9: Investment Council is a tool that helps you research stocks. You give it a list of stock tickers (like `AAPL` for Ap
> L93: - **21 real investor styles, not just names.** Each investor has their own scoring rules, based on how they actuall
> L94: - **Math and opinions are kept separate.** A plain Python script does all the number crunching. The AI only adds th

## 星数曲线

```mermaid
xychart-beta
    title "vikd1000/investment-council 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-29"]
    y-axis "stars" 78 --> 83
    line [79, 80, 82, 82]
```

2026-10-18 79 → 2026-10-29 82（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b2185533d7ff` · [字段定义](../../DATASET.md)*
