# rodcasnog/binary-discrete-diffusion

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/rodcasnog/binary-discrete-diffusion) · [官网](https://arxiv.org/abs/2610.28543) · 个人维护

**二值离散扩散论文代码：逻辑/规划与文本任务训练采样**

论文《Binary Discrete Diffusion: Candidate-Set Diffusion for Logic and Planning Tasks》的配套代码库，基于 JAX/uv/Hydra。支持训练 masked、uniform、binary symmetric、binary absorbing 四种噪声核，配备 cavity head、自适应时间采样器与置信度引导的 Psi-sampler；任务覆盖 Sudoku、Boxoban、图着色、Text8、TinyStories、OpenWebText。提供数据准备脚本、训练配置、采样/求解率/NELBO 评估入口，并发布论文预训练模型于 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种噪声核（masked/uniform/binary symmetric/binary absorbing）统一训练
- 置信度引导的 Psi-sampler 与自适应时间采样器
- 论文全部预训练模型可通过 hf download 获取
- solve rate 与 NELBO/bits-per-character 评估入口

## 适用场景

- 复现论文中离散扩散在逻辑/规划任务上的实验
- 在文本语料上训练并评估离散扩散语言模型
- 下载预训练 checkpoint 直接运行采样与评估

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Code for Binary Discrete Diffusion: Candidate-Set Diffusion for Logic and Planning Tasks. The noisy state of binary 
> L29: `text8`, `tinystories`, `owt`; kernels `masked`, `uniform`, `binary_symmetric`, `binary_absorbing`):

## 星数曲线

```mermaid
xychart-beta
    title "rodcasnog/binary-discrete-diffusion 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-15 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `feefeb168e0b` · [字段定义](../../DATASET.md)*
