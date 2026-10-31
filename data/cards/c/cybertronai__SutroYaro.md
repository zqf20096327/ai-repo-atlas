# cybertronai/SutroYaro

⭐ 17 · Python · Unlicense · 推送 2026-05-29 · [GitHub](https://github.com/cybertronai/SutroYaro) · [官网](https://cybertronai.github.io/SutroYaro/) · 组织维护

**能源高效 AI 训练研究工作区：编码 agent 实验调度与评测环境**

Sutro Group 的研究工作区仓库，定位为实验室记忆与调度中心：用 DISCOVERIES.md 记录已验证结论，配合任务队列、每周纪要与 Telegram/Google Docs/GitHub 同步。用户以 Claude Code、Gemini CLI、Codex 等编码 agent 打开仓库即可自主运行实验。提供 Gymnasium 兼容的评测环境（3 个挑战、16 种方法、72 分评分标准），以 DMD（数据搬运距离）为能源指标，通过 SHA256 校验与指标隔离保证结果可比较，支持多人经 PR 合并结果。当前前沿问题（sparse parity 等）已迁移至其他仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gymnasium 兼容评测环境：3 挑战、16 方法、72 分评分，DMD 能源指标自动测量
- 多编码 agent（Claude Code/Gemini CLI/Codex/Antigravity）共享挑战、自主循环实验
- harness SHA256 校验、指标文件隔离与断路器等安全机制
- bin/merge-findings 支持多研究者结果合并与积分榜生成

## 适用场景

- 让编码 agent 在统一工作区自主运行并记录机器学习实验
- 评测 AI agent 做能源高效 ML 研究的能力
- 多人研究组同步进展、合并各自实验结果

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L10: SutroYaro is the **lab's memory and dispatcher**: where you go to find out what's been tried, who's working on what
> L80: Gymnasium-compatible environment that tests whether an AI agent can do energy-efficient ML research. The agent pick
> L92: - Adapters: Anthropic tool-use, UK AISI Inspect

## 星数曲线

```mermaid
xychart-beta
    title "cybertronai/SutroYaro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2270668e1fa8` · [字段定义](../../DATASET.md)*
