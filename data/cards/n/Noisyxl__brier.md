# Noisyxl/brier

⭐ 116 · HTML · MIT · 推送 2026-09-20 · [GitHub](https://github.com/Noisyxl/brier) · [官网](brier.watch) · 个人维护

**面向 LLM 的预测记账本：事前密封概率、事后按评分规则判分**

四阶段工具：Gate 校验问题（含日期、数据源、可判定测试），Panel 以概率作答并即时哈希链密封，Resolver 盲读数据源结算结果，Scorer 用 Brier 评分与 Murphy 分解评分。内置 hedgehog/fox/parrot/drunk 四种基准预测者，配置 API key 后用户模型可与它们同板评判；账本头哈希锚定到 Robinhood Chain（Arbitrum L2，链 4663）区块以证明时间，工具本身不持有私钥、只读 RPC。以 npm/npx 提供，含可在浏览器运行的演示与无需 API key 的演示命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预测概率作答瞬间哈希链密封，篡改可定位到具体行
- Resolver 与 Scorer 互不可见，防止结算与评分环节作弊
- Brier 评分、校准分箱、Murphy 分解（含剩余项）与 always-yes 基准
- 账本头哈希锚定 Robinhood Chain 区块时间戳，工具不持有私钥（RPC 仅只读方法）

## 适用场景

- 我想验证某个 LLM 给出的概率预测是否事后被改动
- 把自有模型与基准预测者放在同一评分板下比较校准能力
- 为问题设定数据源与判定规则，自动结算并按 Brier 分数评分

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L32: A panel answers with a probability. That answer is hash-chained the second it is given, so it cannot be
> L61: |accuracy, which rewards a forecaster for only ever saying 1% and 99%|proper scoring rules. Your best score comes f
> L165: Put an API key in `.env` and your models sit on the same board as these four, judged the same way.

## 星数曲线

```mermaid
xychart-beta
    title "Noisyxl/brier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-24 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0cf86fa8d87a` · [字段定义](../../DATASET.md)*
