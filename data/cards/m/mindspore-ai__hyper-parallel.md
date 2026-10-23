# mindspore-ai/hyper-parallel

⭐ 103 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/mindspore-ai/hyper-parallel) · 组织维护 · 中文 README

**面向昇腾超节点的分布式并行训练框架，服务大模型训练**

HyperParallel 是面向昇腾（Ascend）超节点的分布式并行加速能力框架，覆盖从集群分布式并行（SPMD/MPMD）到芯片内多核并行，支持 CPU DRAM 与 NPU HBM 池化管理、拓扑感知调度、FP8 混合精度训练。面向训练用户提供以 YAML 配置 Hugging Face 模型的训练入口（当前支持 Qwen3-30B-A3B）；面向模型作者提供 HyperParallel Core 底层 API（DeviceMesh/DTensor、FSDP/HSDP、TP/CP/EP/PP、MoE 切分、分布式检查点、确定性训练）。并行等系统优化通过声明式接口从模型代码中分离注入，并支持直接读取 Hugging Face 权重与复用 Transformers 实现。采用 Apache 2.0 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖集群 SPMD/MPMD 与芯片内多核 MPMD 的并行范式，支持昇腾超节点资源池化与 FP8 混合精度
- 声明式接口将并行/重计算/Offload 等系统优化从模型代码分离注入，兼容 Hugging Face 模型与权重
- FSDP/HSDP、TP、CP、EP、PP 等并行策略组合与 MoE 专家切分
- 全流程确定性训练与 bitwise 对齐验证、分布式检查点与异步保存

## 适用场景

- 在昇腾超节点集群上训练 Qwen3 等 Hugging Face 大语言/多模态模型
- 模型作者用 HyperParallel Core API 构建分布式模型并组合并行策略
- 需要可复现训练结果与确定性调试的大规模训练任务

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L19: HyperParallel 面向昇腾超节点提供分布式并行加速能力。针对资源池化、对等架构、分层网络拓扑和 FP8 低精度格式等特点，框架覆盖从集群分布式并行到芯片内多核并行，并支持 CPU DRAM 与 NPU HBM 池化管理、
> L23: - **模型与系统优化解耦**：HyperParallel 将并行、重计算和 Offload 等系统优化从模型代码中分离，并通过声明式接口注入模型；并行范式覆盖集群 SPMD、集群 MPMD 和芯片内多核 MPMD，面向大语言模型
> L47: > HyperParallel Core 面向模型作者和框架开发者，提供从分布式模型构建到训练执行与状态管理的底层能力。

## 星数曲线

```mermaid
xychart-beta
    title "mindspore-ai/hyper-parallel 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 78 --> 105
    line [80, 101, 103]
```

2026-10-18 80 → 2026-10-23 103（+23）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `50196728f203` · [字段定义](../../DATASET.md)*
