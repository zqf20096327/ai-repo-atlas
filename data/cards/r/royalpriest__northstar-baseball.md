# royalpriest/northstar-baseball

⭐ 23 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/royalpriest/northstar-baseball) · [官网](https://northstar-baseball.vercel.app) · 个人维护

**为棒球爱好者提供 2025 MLB 打者数据分析诊断**

将 2025 赛季 MLB Statcast 投球数据处理为打者三维度诊断（选球、接触、破坏力），通过 FastAPI 服务与 Next.js 网页应用提供检索，另设多伦多蓝鸟与加拿大出生球员专页。数据处理含 742,080 笔投球重建为 190,987 个打席；得分概率模型按时序切分训练，并如实报告模型未超过简单基线的阴性结果。API 可从 CSV 回退或 PostgreSQL 读取，源数据需经 pybaseball 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 742,080 笔 Statcast 投球数据处理为 190,987 个打席诊断
- 选球/接触/破坏力三维度打者画像与 2-4 人对比视图
- 时序切分训练的概率模型，实验与命令全部公开可复现
- 支持 CSV 回退与 PostgreSQL 后端两种 API 数据源

## 适用场景

- 查询 2025 赛季任意 MLB 打者的数据诊断画像
- 并排比较两到四名打者的表现指标
- 复现实验流程或基于 Statcast 数据开展研究

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: NorthStar is a baseball analytics project that turns a full season of MLB Statcast pitch data into
> L4: context-aware hitter diagnostics (Selection, Contact and Damage) and serves them through a FastAPI service
> L17: - Scoring-probability models were trained only on information available before each plate appearance, on a


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `ce8d53cab767` · [字段定义](../../DATASET.md)*
