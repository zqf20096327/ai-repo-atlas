# quguanni/kernel-vuln-data

⭐ 25 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/quguanni/kernel-vuln-data) · 个人维护

**Linux 内核漏洞数据集：12.5 万对 bug 修复对及标注**

从 2005-2025 年 Linux 内核 git 历史中挖掘出的 125,183 对 bug 引入-修复提交数据集，以 CSV 提供，字段包括引入/修复提交 SHA、存活天数、子系统、bug 类型（use-after-free、null-deref 等）、CVE ID、stable 回 port 标记及 diff 统计。附带 cve_miner.py（提取 Fixes: 标签）与 extract_features.py（从 diff 提取 51 个特征用于 ML 训练）两个脚本。数据同步托管于 HuggingFace。面向漏洞研究与机器学习研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 125,183 对 bug-fix pairs，覆盖 2005-2025 年内核历史
- 标注存活时长、子系统、bug 类型、CVE ID 等 14 类字段
- 附 extract_features.py 从 diff 提取 51 个 ML 特征
- HuggingFace 上提供 Data Studio 在线查看

## 适用场景

- 训练 bug 存活时长预测或 bug 引入检测模型
- 按子系统与 bug 类型分析内核漏洞分布规律
- 研究 CVE 与修复提交的关联及 stable 回 port 情况

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **125,183 bug-fix pairs** mined from 20 years of Linux kernel git history (2005-2025).
> L56: - `cve_miner.py` - Extract `Fixes:` tags from kernel git history

## 星数曲线

```mermaid
xychart-beta
    title "quguanni/kernel-vuln-data 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f6397a67030d` · [字段定义](../../DATASET.md)*
