# Navarre-AI/pythia

⭐ 15 · JavaScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/Navarre-AI/pythia) · [官网](https://navarre.ai/apps/pythia) · 组织维护

**面向 FileMaker 数据库的对话式报表应用：自然语言出报表**

自托管的对话式报表应用：连接任意开启了 OData 的 FileMaker Server 文件，通过 OData 将所选表同步到应用自有卷上的本地 DuckDB 副本（有 UUID 主键与修改时间戳时可增量同步），用户用自然语言提问，AI 编写查询并由本地 SQL 引擎执行，返回数字、图表与可打印报表；已保存报表可无 AI 重复运行并得到相同结果。经一条命令安装脚本部署到用户自己的 Fly.io 账户，需要 Anthropic 或 OpenAI 的 API key。发送给 AI 的仅有表/字段名、问题与每次查询至多 60 行结果，可在设置中开启严格隐私模式。

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

- AI 写查询、本地 SQL 引擎（DuckDB）执行，数字不来自模型
- OData 增量同步 FileMaker 表到本地 DuckDB 副本
- 已保存报表无 AI 重跑，结果可复现
- 一条命令安装并部署到用户自己的 Fly.io 账户

## 适用场景

- 对 FileMaker 数据用自然语言提问并获得数字与图表报表
- 无需搭建布局或关系即可生成业务报表
- 在企业自有云账户中自托管，控制数据发送范围

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Pythia is a conversational reporting app for FileMaker databases. Point it at
> L47:  the model.** The AI writes queries; a local SQL engine runs them. The model

## 星数曲线

```mermaid
xychart-beta
    title "Navarre-AI/pythia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `acefb4284fbe` · [字段定义](../../DATASET.md)*
