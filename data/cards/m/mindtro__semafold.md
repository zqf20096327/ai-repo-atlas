# mindtro/semafold

⭐ 19 · Python · Apache-2.0 · 推送 2026-09-13 · [GitHub](https://github.com/mindtro/semafold) · [官网](https://mindtro.com) · 个人维护

**面向 AI 基础设施的向量/张量压缩工具库，含 KV-cache**

基于 TurboQuant 编解码器的向量压缩 Python 库，压缩 embedding、检索表示与 cache 形状的 K/V 张量，给出实测字节数、压缩比与验证证据。核心为纯 NumPy 实现，默认无需 GPU；安装 PyTorch（CUDA/MPS）或 MLX（Metal）后可自动零配置 GPU 加速。基准显示 embedding 3-bit 压缩达 10.52x。当前 TurboQuant 位于深层导入面而非稳定根 API，后续方向是运行时/后端集成而非核心压缩数学。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TurboQuant 编解码器压缩 embedding 与 KV 张量（示例 10.52x）
- 纯 NumPy 核心，默认无需 GPU；可选 PyTorch CUDA/MPS 或 MLX Metal 加速
- 类型化 encode/decode 契约与实测字节、失真、验证证据
- 附带基准脚本与合成验证运行器

## 适用场景

- 降低向量数据库与检索管道的存储占用
- 压缩自定义推理栈中的 KV cache 张量
- 压缩 AI 编排器的长期向量记忆

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L10: Semafold is a vector-first compression toolkit for AI workloads that compresses embeddings, retrieval representatio
> L61: - cache-shaped K/V tensor compression in custom inference stacks

## 星数曲线

```mermaid
xychart-beta
    title "mindtro/semafold 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-27 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ec805022c72e` · [字段定义](../../DATASET.md)*
