# Ginfofinance/BovDBrepository

⭐ 10 · Python · NOASSERTION · 推送 2026-08-25 · [GitHub](https://github.com/Ginfofinance/BovDBrepository) · [官网](https://doi.org/10.7910/DVN/TMB4IG) · 组织维护

**为 ML 研究者提供巴西 B3 全市场股票行情开放数据集**

BovDB 是覆盖巴西 B3 交易所全部上市股票（ON/PN/UNT/BDR）的历史行情开放数据集与 Python 工具包，含 1995 至今的日线 OHLCV 与 5 分钟盘中数据（price5），并通过 factor 字段处理拆股与增发等公司行为。数据以单文件 SQLite 存储，配套 bovdb 只读 Python SDK 与示例脚本。v2 为哈佛 Dataverse 正式发布版（有 DOI），v3 在开发中；许可证为 CC BY-NC 4.0，禁止商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 B3 全部股票的日线 OHLCV（1995–至今）与 5 分钟盘中数据
- SQLite 单文件存储，bovdb SDK 默认只读模式连接
- 含拆股/并股/增发调整的 factor 字段
- 提供 K 线图、统计图与极值检测示例脚本

## 适用场景

- 为股价时序预测模型准备基准训练数据
- 做巴西股市的计量经济学研究
- 研究量化交易策略时回测历史行情

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L20: **BovDB** is an open-access, relational dataset and Python toolkit of historical stock quotes and high-frequency in
> L33: |**BovDB v1.0**|`BovdbV1/`|1995 – 2020|Daily|All B3 equities, daily OHLCV, adjustment factors. Formats: CSV, JSON, 
> L34: |**BovDB v2.0**|`BovdbV2/` — Harvard Dataverse|1995 – 2024|Daily + Intraday|Daily historical quotes + 5-min intrada

## 星数曲线

```mermaid
xychart-beta
    title "Ginfofinance/BovDBrepository 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `5b80e6747ec6` · [字段定义](../../DATASET.md)*
