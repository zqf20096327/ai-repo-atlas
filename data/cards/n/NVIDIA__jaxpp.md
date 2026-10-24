# NVIDIA/jaxpp

⭐ 83 · Python · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/NVIDIA/jaxpp) · 组织维护

**面向 JAX 的 MPMD 流水线并行库，用于大规模 LLM 训练**

NVIDIA 维护的 JAX 扩展库，通过 mark_stage_end(layer) 注解与 @mpmd_jit_with_loop 装饰器，将 JAX 计算自动拆分为多个独立 jit 并分发到不同设备的 SPMD 模块，实现 MPMD 流水线并行，面向大规模 LLM 训练场景。支持多节点部署（需各节点安装，用 jax.distributed.initialize 初始化，也可配合 Ray），提供 MpmdMesh 包装 JAX Mesh。提供开发/测试 Docker 容器，已在 MaxText 若干模型上测试；API 当前不稳定且暂不接受 PR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- mark_stage_end 注解 + @mpmd_jit_with_loop 装饰器实现自动计算拆分
- 多节点并行部署支持，不绑定特定集群启动器（可用 Ray 等）
- 提供基于 CUDA 13 的开发/测试 Docker 容器与多测试套件
- 已在 MaxText 多个模型上测试并集成为其 fork

## 适用场景

- JAX 训练代码中添加流水线并行以训练大模型
- 多节点多 GPU 环境下做 MPMD 并行训练
- 为 Flax 模块（如 BERT 类配置）划分流水线阶段

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: JaxPP is a JAX library enabling Multiple-Program Multiple-Data (MPMD)
> L7: JaxPP automatically splits JAX computations into multiple SPMD modules that
> L195: JaxPP has been tested with several models from MaxText.

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/jaxpp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-24 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ca97f969828b` · [字段定义](../../DATASET.md)*
