# microsoft/social-reasoning-bench

⭐ 20 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/microsoft/social-reasoning-bench) · [官网](https://microsoft.github.io/social-reasoning-bench/) · 组织维护

**评测 LLM agent 社交推理能力的基准**

微软发布的评测基准，在多方对话环境中测试 LLM agent 的社交推理能力。以源码仓库形式提供，需 Python 3.11+ 与 uv，通过 git clone 与 uv sync 安装运行。评测时假设被测模型以 OpenAI 兼容端点提供服务，示例使用 Gemini 作为对话对手方，复现官方结果需配置 GEMINI_API_KEY。README 提供安装与用法说明，详细文档另见 Installation、Experiments 与 LLMs 页面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多方对话环境中评测 LLM agent 的社交推理能力
- 支持评测以 OpenAI 兼容端点提供的自有模型
- 复现官方结果使用 Gemini 作为对手方

## 适用场景

- 评测自有 LLM 的社交推理表现
- 复现基准的官方实验结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: Evaluate the social reasoning capabilities of LLM agents in multi-party environments.
> L23: Evaluate the social reasoning ability of your own LLM. For example's sake, we'll assume your LLM is served as `my-m

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/social-reasoning-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c520b41610d8` · [字段定义](../../DATASET.md)*
