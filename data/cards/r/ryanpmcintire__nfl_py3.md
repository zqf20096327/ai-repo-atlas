# ryanpmcintire/nfl_py3

⭐ 16 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/ryanpmcintire/nfl_py3) · 个人维护

**预测 NFL 让分盘（ATS）胜负的可复现机器学习研究管线**

面向 NFL 让分预测的 Python 研究与预测管线：读取 nflverse 维护数据集（而非爬取 HTML），所有特征仅使用开球前可得信息，通过嵌套时间顺序 walk-forward 测试评估模型（Ridge 回归、市场残差特征），输出每周预测卡与校准概率。要求 Python 3.12，使用 uv 管理依赖，通过 nfl-ats CLI 执行 ingest、回测、预测与发布流程；数据与模型产物不入 Git，README 标注模块由命令自动再生成，禁止手工编辑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全部特征严格由开球前可得信息构建
- 嵌套时间顺序 walk-forward 评估，模型只能用预测周之前的比赛训练
- 一次命令完成 ingest、特征构建、回测、预测与卡片发布的每周流水线
- 发布前经独立的 fail-closed prediction_safety 契约校验

## 适用场景

- 每周生成 NFL 让分盘的强制选择预测卡
- 对体育市场预测模型做时间顺序回测研究
- 为竞猜池（pool）提供按置信度排序的全场选择

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: NFL ATS is a reproducible research and prediction pipeline for estimating which
> L7: and evaluates model choices with nested chronological walk-forward tests.

## 星数曲线

```mermaid
xychart-beta
    title "ryanpmcintire/nfl_py3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `083ded73d12e` · [字段定义](../../DATASET.md)*
