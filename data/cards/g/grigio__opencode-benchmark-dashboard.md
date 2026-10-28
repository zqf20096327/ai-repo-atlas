# grigio/opencode-benchmark-dashboard

⭐ 46 · TypeScript · 推送 2026-06-05 · [GitHub](https://github.com/grigio/opencode-benchmark-dashboard) · 个人维护

**测试 opencode 与多种 LLM 模型的基准系统：测延迟与准确率**

针对 opencode CLI 的基准测试系统：在多种已配置的 LLM 模型上运行真实场景任务，测量速度（延迟、tok/s）与正确率（accuracy），生成基准报告。README 强调最优速度/准确率权衡取决于具体用例与硬件，需在真实场景中实测。运行依赖 Bun 运行时、已安装并在 PATH 中的 opencode CLI，以及预先在 ~/.config/opencode/opencode.json 配置好的模型。以源码形式提供，通过 bun install 安装依赖后运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 测量多模型的延迟与准确率
- 考虑推理、tok/s 与不同量化方案的影响
- 生成基准测试报告

## 适用场景

- 为自己的硬件挑选速度与准确率合适的本地 LLM
- 对比不同量化方案在真实编码场景的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Benchmark system for testing opencode with various LLM models, measuring speed (latency) and correctness (accuracy).
> L22: - Bun runtime

## 星数曲线

```mermaid
xychart-beta
    title "grigio/opencode-benchmark-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `51df91b50be1` · [字段定义](../../DATASET.md)*
