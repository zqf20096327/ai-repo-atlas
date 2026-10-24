# NVIDIA-Merlin/HugeCTR

⭐ 1,072 · C++ · Apache-2.0 · 推送 2026-08-03 · [GitHub](https://github.com/NVIDIA-Merlin/HugeCTR) · 组织维护

**GPU 加速的推荐系统深度学习训练与推理框架**

NVIDIA 维护的 GPU 加速推荐系统框架，面向 CTR 估计等大规模深度学习模型的训练与推理，支持模型并行、多节点训练、混合精度以及超大 embedding 部署，提供高层 Python 接口、ONNX 转换器与 Sparse Operation Kit，并提供合成数据生成工具。从 25.03 版本起仅提供 Dockerfile 源码，用户需自行构建镜像后运行容器，配合 NCCL 进行多卡/多节点通信。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 高层抽象 Python 接口，支持模型并行与多节点训练
- 混合精度训练与超大 embedding 部署支持
- HugeCTR 到 ONNX 的模型转换器与 Sparse Operation Kit
- 内置合成数据生成工具（Parquet 格式）

## 适用场景

- 在多 GPU/多节点环境训练大规模 CTR 推荐模型
- 部署含超大 embedding 的推荐模型并导出 ONNX
- 生成 Parquet 合成数据快速验证训练流程

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L8: HugeCTR is a GPU-accelerated recommender framework designed for training and inference of large deep learning models
> L11: * **Fast**: HugeCTR performs outstandingly in recommendation benchmarks including MLPerf.

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-Merlin/HugeCTR 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 1071 --> 1074
    line [1073, 1072, 1072]
```

2026-10-18 1,073 → 2026-10-24 1,072（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1bdeb0a4afca` · [字段定义](../../DATASET.md)*
