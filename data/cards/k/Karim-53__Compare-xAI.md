# Karim-53/Compare-xAI

⭐ 14 · Jupyter Notebook · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/Karim-53/Compare-xAI) · [官网](https://karim-53.github.io/cxai/) · 个人维护

**XAI 方法统一评测基准：功能测试比较 SHAP、LIME 等**

对特征归因类可解释性方法（SHAP、LIME、MAPLE、Archipelago 等）进行功能单元测试式评测的基准：每条测试编码一条终端用户对解释的期望，以黑盒方式端到端执行，输出可复现的证据化比较。使用 3 个指标（可理解性、可移植性、平均执行时间），全套实验可在无 GPU 的普通计算机 CPU 上约 4 小时跑完，数据与 SQLite 导出随仓库提供，另附在线交互结果页面与 arXiv 论文。面向需要为模型挑选解释方法的数据科学家与科研人员，支持通过继承基类扩展新解释器与新测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 功能单元测试式黑盒评测，每条测试对应一条终端用户期望
- 3 个可比较指标：Comprehensibility、Portability、平均执行时间
- 全量数据与 SQLite 导出随仓库提供，CPU 上约 4 小时可复现
- 约 4 步即可添加新解释器或新测试

## 适用场景

- 为我的模型在 SHAP、LIME 等解释方法之间做选型比较
- 复现论文中的 XAI 评测实验结果
- 按可理解性/可移植性/耗时维度浏览各解释器表现

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L8: `Compare-xAI` benchmarks feature-attribution / feature-importance explainability methods (SHAP, LIME, MAPLE, Archipe
> L16: - 📊 **3 comparable metrics** — Comprehensibility, Portability, and Average execution time (see FAQ).

## 星数曲线

```mermaid
xychart-beta
    title "Karim-53/Compare-xAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `800c152526cc` · [字段定义](../../DATASET.md)*
