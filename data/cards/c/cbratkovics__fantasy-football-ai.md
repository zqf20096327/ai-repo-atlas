# cbratkovics/fantasy-football-ai

⭐ 16 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/cbratkovics/fantasy-football-ai) · [官网](https://fantasy-football-ai.vercel.app) · 个人维护

**面向NFL梦幻橄榄球玩家的每周得分预测与决策工具**

基于 nflverse 数据的每周 NFL 梦幻橄榄球得分预测流水线：按 QB/RB/WR/TE 位置训练随机森林模型（XGBoost 为挑战者），使用 65 个严格滞后的 as-of 特征并做泄漏测试，在 2024 冻结测试季与 2025 样本外赛季上对照因果基线评估；GMM 生成选秀分层。GitHub Actions 每周二拉数、跑数据契约与 PSI 漂移检测后自动决定发布/保持/晋升。提供 FastAPI（Hugging Face Docker Space）与 Next.js 前端，含 Decision Lab 决策记录回放功能。明确声明全流程无 LLM 参与。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按位置训练随机森林模型，65 个严格滞后特征并有泄漏测试
- 每周 GitHub Actions 作业：数据契约→PSI 漂移→评分→影子评估→发布/保持/晋升
- 评估结果以带输入哈希与提交号的 JSON 工件为准，API 原样提供
- dbt Core + dbt-duckdb/MotherDuck 构建奖章层数据仓库（26 模型、97 测试）

## 适用场景

- 每周获取 NFL 球员梦幻得分预测做首发/替补决策
- 在 Decision Lab 中对比候选球员并导出可回放校验的决策凭证
- 参考其时间序列验证与工件化评估方法做 MLOps 实践

## 场景标签

`MLOps` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L34: Weekly NFL fantasy-point projections for QB / RB / WR / TE, built so that **every number can be
> L45:  One as-of feature module (65 lagged features) · RandomForest champion, XGBoost challenger, per position · residual

## 星数曲线

```mermaid
xychart-beta
    title "cbratkovics/fantasy-football-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ca272b490c46` · [字段定义](../../DATASET.md)*
