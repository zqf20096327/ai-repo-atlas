# ReaperProtocol/Reaper

⭐ 23 · TypeScript · 推送 2026-09-04 · [GitHub](https://github.com/ReaperProtocol/Reaper) · [官网](https://reaperedge.com/) · 组织维护

**Robinhood 加密抛售后反弹机会扫描与评分工具**

TypeScript 编写的加密市场结构扫描器，基于 Claude Agent SDK 构建。从 Robinhood 加密行情快照中识别经历急跌后正在反弹的资产，按反弹参与度、报价价差、可见深度与距低点时间四项输入评分，经五道确定性闸门后输出 HUNT/WATCH/SKIP/EXPIRED 决策及理由。模型仅在数据检查通过后解释 setup，不覆盖闸门判定。提供风险控制项与 dry mode 观察模式，以 git clone + npm 方式本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四维评分：反弹参与度、价差、深度、距低点时间
- 五道确定性决策闸门，被拒候选保留理由
- HUNT/WATCH/SKIP/EXPIRED 四级输出并附分数
- dry mode 默认观察模式，未配置执行则不下单

## 适用场景

- 急跌后筛选括约可控、深度足够的反弹候选
- 避免把首次反弹当作趋势恢复的证据
- 以统一评分面板比较多个加密资产的恢复质量

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L12: Built with Claude Agent SDK
> L87: The loop stays deterministic around its gates. The model explains the setup after the data checks pass; it does not

## 星数曲线

```mermaid
xychart-beta
    title "ReaperProtocol/Reaper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `91a0d9c2bb46` · [字段定义](../../DATASET.md)*
