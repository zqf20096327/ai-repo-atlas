# tensorcircuit/tensorcircuit-ng

⭐ 92 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/tensorcircuit/tensorcircuit-ng) · [官网](https://tensorcircuit-ng.readthedocs.io/en/latest/platform/index.html) · 组织维护 · 中文 README

**给量子研究者的张量网络量子电路模拟与AI工作流框架**

基于张量网络引擎的开源量子软件框架，是 TensorCircuit 的技术后继版本。构建于 Jax、TensorFlow、PyTorch 之上，支持自动微分、JIT 编译、GPU 加速、向量化并行与多机多卡分布式训练，可模拟理想、噪声、Clifford、qudit、MPS 近似、模拟及费米子等八类电路，并支持 QPU 硬件接入与 CPU/GPU/QPU 混合部署。面向科研用户，提供 200+ 示例脚本与 40+ 教程，内置面向 AI 编码代理的 AGENTS.md 规则与多个 agentic skills。以纯 Python 包形式经 pip 安装。

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

- 张量网络引擎支持八类电路模拟（理想/噪声/Clifford/qudit/MPS/模拟/对称/费米子）
- 基于 Jax/TensorFlow/PyTorch，支持自动微分、JIT、GPU 加速与分布式模拟
- 内置 AGENTS.md 与 8 个 agentic skills，支持 AI 编码代理的量子研究工作流
- 支持 QPU 硬件接入、CPU/GPU/QPU 混合部署与多种量子误差缓解方法

## 适用场景

- 运行变分量子算法与量子-经典混合范式的数值实验
- 用 AI 编码代理把研究问题转化为可执行验证的量子实验代码
- 多 GPU/多主机上做大规模量子电路模拟

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L31: TensorCircuit-NG is the next-generation open-source high-performance quantum software framework and an AI-native qu
> L33: TensorCircuit-NG is built upon tensornetwork engines, supporting for automatic differentiation, just-in-time compil
> L35: TensorCircuit-NG is built on top of modern machine learning frameworks: Jax, TensorFlow, and PyTorch. It is specifi
> L249:  - Fully **AI-native ecosystem** with built-in agentic skills and standardized development rules for AI assistants

## 星数曲线

```mermaid
xychart-beta
    title "tensorcircuit/tensorcircuit-ng 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-27 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b93f9a28f520` · [字段定义](../../DATASET.md)*
