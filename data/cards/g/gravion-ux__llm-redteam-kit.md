# gravion-ux/llm-redteam-kit

⭐ 4 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/gravion-ux/llm-redteam-kit) · 个人维护

**面向开发者的 LLM 红队评测工具：注入/越狱探针与 CI 回归门禁**

一个授权用途的 LLM 红队评测工具包：内置 24 条覆盖 4 类攻击（提示注入、越狱、系统提示提取、数据外泄）的探针集，按 OWASP LLM Top 10 (2025) 映射，向任意 OpenAI 兼容聊天端点发送探针，用基于正则与拒绝检测的启发式判定器打分，输出每案结论、分类通过率与攻击成功率，并可通过阈值和基线对比在 CI 中阻断回归。零运行时依赖，提供离线 mock 模式。MIT 许可，从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 条探针映射 OWASP LLM Top 10，覆盖 4 类攻击
- 零运行时依赖，仅 Python 标准库
- 离线 mock 模式无需网络与 API key
- CI 回归门禁：阈值与基线对比，退出码区分结果

## 适用场景

- 模型或系统提示变更后在 CI 中回归测试安全性
- 对自有应用编写针对其系统提示与工具的自定义探针包
- 离线 mock 模式下先熟悉流程再接入真实模型

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **An authorized LLM red-teaming evaluation toolkit.** Run a curated pack of
> L9: transparent heuristic detectors, and gate your CI pipeline on the result.
> L47: |Regression gate|`--threshold` (minimum pass rate) and `--baseline` (previous report) — exit code `2` on regression

## 星数曲线

```mermaid
xychart-beta
    title "gravion-ux/llm-redteam-kit 星数(近 3 点)"
    x-axis ["2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-22 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `88f781e5c5d6` · [字段定义](../../DATASET.md)*
