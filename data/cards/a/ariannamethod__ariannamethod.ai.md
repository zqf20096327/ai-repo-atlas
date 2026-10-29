# ariannamethod/ariannamethod.ai

⭐ 20 · C · LGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/ariannamethod/ariannamethod.ai) · [官网](http://x.com/@olegataeff) · 个人维护

**纯 C 实现的机器学习语言：定义、训练并运行自研 transformer**

AML（Arianna Method Language）是一门以两个 C 文件为核心的机器学习编程语言，提供数组/矩阵运算、反向模式自动微分、异步与因果注意力等原语，每条命令映射到具体 C 操作；不依赖 Python 与 PyTorch，BLAS 与 CUDA 为可选后端。内含参考架构 Janus（三路注意力 + 场记忆，176M 参数）及训练结果、Go 推理引擎封装（加载 GGUF 模型）、550 项基准测试与 make 构建安装工具链。语言层提供 PROPHECY/DESTINY 等生成时 logit 调控命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心为两个 C 文件，零外部依赖（libc/libm/libpthread）即可构建训练
- Janus 架构：Content + RRPRAM + Echo 三路注意力，176M 参数模型 val bpb 0.866
- Go 推理引擎封装 GGUF 模型加载与生成（可选链接）
- 推理期 logit 调控命令（PROPHECY/DESTINY/VELOCITY/LoRA 注入等）

## 适用场景

- 在无 Python/PyTorch 环境下用 C 训练和运行 transformer
- 把核心 C 库直接编译进自己的项目做嵌入
- 通过 AML 命令在推理时调控生成行为

## 场景标签

`模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: A complete machine learning language. AML defines, trains, and runs transformers with integrated field physics — ar
> L13: Two core files, with 550 baseline runtime tests and dedicated compiler, module, and text suites. A transformer arch

## 星数曲线

```mermaid
xychart-beta
    title "ariannamethod/ariannamethod.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `df756d119300` · [字段定义](../../DATASET.md)*
