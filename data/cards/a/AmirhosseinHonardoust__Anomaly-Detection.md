# AmirhosseinHonardoust/Anomaly-Detection

⭐ 26 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/AmirhosseinHonardoust/Anomaly-Detection) · 个人维护

**合成交易数据异常检测演示项目：四检测器投票集成**

基于 scikit-learn 的教学/作品集项目：生成带已知异常模式的合成交易数据（杂货爆发、极端电子消费、负数/零金额），用 Isolation Forest、LOF、逐客户滚动 Z-score 和逐品类日成交量爆发检测器组成 2-of-4 投票集成，输出异常 CSV、严重度排名与两张图表，并用独立脚本对照真值计算 precision/recall/F1。README 明确声明这是教育演示，非生产级反欺诈系统，不适用于真实金融数据；批处理 CLI，无实时/流式检测。

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

- 四检测器（Isolation Forest/LOF/滚动 Z-score/品类爆发）2-of-4 投票集成
- 合成数据生成器注入三类已知异常，种子可复现
- 独立评估脚本输出 precision/recall/F1，README 附实测低值结果与调参表
- 滚动基线仅用先前数据，避免当前行泄漏进自身统计

## 适用场景

- 学习多模型异常检测集成与评估的完整工作流
- 作品集展示数据科学项目工程实践（测试/CI/文档）
- 了解滚动基线泄漏、特征缩放等建模陷阱

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L10: A transaction-anomaly detection project that combines **Isolation Forest**, **Local Outlier Factor (LOF)**, a **per
> L12: > **Important:** This project runs on **synthetic transaction data** and is an **educational demo**, not a producti

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Anomaly-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5e5bae2400fe` · [字段定义](../../DATASET.md)*
