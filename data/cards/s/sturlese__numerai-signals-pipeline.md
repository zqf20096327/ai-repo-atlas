# sturlese/numerai-signals-pipeline

⭐ 26 · Python · 推送 2026-07-09 · [GitHub](https://github.com/sturlese/numerai-signals-pipeline) · 个人维护

**量化竞赛管道：从 Yahoo 数据造特征、训练 XGBoost 并提交 Numerai**

面向 Numerai Signals 竞赛的端到端 Python 流水线：从 Yahoo Finance 下载价量数据，用声明式特征/滞后引擎构建技术分析特征（指标→去噪→滞后→按 era 归一化），连接 Numerai 官方目标与股票池，训练 XGBoost 模型并生成合法的 (0,1) 信号提交文件。配置由不可变 dataclass 管理，纯逻辑与 IO 层分离，附 93 项离线测试。实盘运行需 Numerai 凭据、下载数 GB parquet 数据集并默认使用 GPU 训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式特征/滞后引擎：IndicatorSpec 统一定义指标、滞后与归一化
- 端到端覆盖：Yahoo 下载→特征→XGBoost 训练→排名归一化提交
- 纯逻辑与 IO 分离，93 项离线测试约 99% 覆盖率
- Bloomberg↔Yahoo ticker 映射含社区镜像与内置回退

## 适用场景

- 参加 Numerai Signals 竞赛并自动化提交信号
- 基于 Yahoo Finance 数据构建技术分析特征与训练模型
- 复用特征引擎为自有量化研究生成数据集

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L12: The pipeline downloads price/volume data from Yahoo Finance, builds a large set of custom
> L14: Numerai's official targets, trains an XGBoost model and produces a valid tournament

## 星数曲线

```mermaid
xychart-beta
    title "sturlese/numerai-signals-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `676481281f9d` · [字段定义](../../DATASET.md)*
