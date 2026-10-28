# workofart/harness-training

⭐ 23 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/workofart/harness-training) · [官网](https://www.henrypan.com/blog/2026-07-18-harness-training/) · 个人维护

**冻结 LLM、训练其外层 harness 的 PyTorch 风格训练框架**

面向 agent 开发者的训练框架：保持 LLM 权重冻结，对模型外层的 harness（提示词、上下文管理、工具、修复循环）做迭代优化。每轮由 Estimator（默认 claude CLI，可换 codex）提出一个 diff，在任务面板（Terminal-Bench、SWE-bench）上按 StrictPareto 准则与基线比较，通过则 git fast-forward 晋升，否则拒绝。要求确定性推理（串行解码）、Docker 环境，通过 OpenAI 兼容端点接入任意模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 风格 API（epochs/backward/step）驱动 harness 迭代
- 候选 diff 经任务面板测量与 StrictPareto 准则决定晋升或拒绝
- 内置 Terminal-Bench 与 SWE-bench 环境，可扩展基准与模型 provider
- 可限定候选可编辑的补丁面，只训练 prompt 表面等局部

## 适用场景

- 在不改模型权重的前提下优化 agent 的提示词与上下文管理
- 对 agent harness 做 A/B 测试并自动晋升优胜版本
- 将 harness 适配到新模型时重新基线与训练

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A PyTorch-style harness trainer**. The LLM model stays frozen, the harness around it is being trained, including t
> L30: **Requirements:** Python 3.13, Docker with `linux/amd64` container support and the Compose plugin, the `claude` CLI
> L38: Use either Ollama or llama.cpp or anything you like to expose the model through an OpenAI-compatible endpoint. Foll

## 星数曲线

```mermaid
xychart-beta
    title "workofart/harness-training 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-28 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3d1e96029b2d` · [字段定义](../../DATASET.md)*
