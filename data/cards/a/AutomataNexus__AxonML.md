# AutomataNexus/AxonML

⭐ 33 · Rust · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/AutomataNexus/AxonML) · [官网](https://automatanexus.com) · 组织维护

**纯 Rust 编写的 PyTorch 等价深度学习框架（22+ crates）**

以纯 Rust 实现的机器学习框架，覆盖张量运算与惰性计算、反向自动微分、nn 模块（CNN/RNN/Transformer）、优化器与训练健康监控、数据加载、视觉/音频/NLP 组件、分布式训练（DDP/FSDP/流水线/张量并行）、量化（INT4-INT8、BitNet 1.58-bit）、ONNX 导入导出、CLI/TUI/Web 控制台与 API 服务器。后端支持 CUDA、wgpu WebGPU 与 no_std 嵌入式核心，含 LLM 微调（LoRA、Qwen3/LLaMA）与 GGUF 导出。面向需要在 Rust 生态中训练和部署模型的开发者，以 cargo workspace 多 crate 形式分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反向模式自动微分 + 惰性张量计算与运行时核融合
- CUDA/wgpu 双 GPU 后端，NVFP4 路径支持 Blackwell
- 分布式训练：DDP、FSDP（ZeRO-2/3）、流水线与张量并行
- 量化覆盖 INT4-INT8 与 BitNet I2_S 1.58-bit 三值
- ONNX 导入导出（40+ 算子，opset 17）与 GGUF 导出

## 适用场景

- 在 Rust 项目中训练与部署神经网络，不依赖 Python 栈
- 对 LLM 做 LoRA 微调并导出量化（Q8_0/Q4）模型
- 多 GPU 分布式训练与模型分片部署
- 在嵌入式（no_std）与边缘设备上运行推理

## 场景标签

`模型训练` `微调` `模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5:  A complete, PyTorch-equivalent machine learning framework written in pure Rust.
> L16: Axonml (named after axons - the nerve fibers that transmit signals between neurons) is an ambitious open-source pro
> L20: AxonML provides comprehensive PyTorch-equivalent functionality across 24 crates with **1,700+ tests** (1,773 test f

## 星数曲线

```mermaid
xychart-beta
    title "AutomataNexus/AxonML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `93ebc5781ca8` · [字段定义](../../DATASET.md)*
