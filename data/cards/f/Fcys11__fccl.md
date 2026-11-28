# Fcys11/fccl

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/Fcys11/fccl) · 个人维护 · 中文 README

**让单机混插的 AMD+NVIDIA GPU 张量并行跑同一个模型**

纯 Python 实现的跨进程集合通信层，通过 PCIe 和主机共享内存（/dev/shm）在厂商混合的 GPU 之间完成 all_reduce、bcast、all_to_all 等集合操作，不依赖 NVLink、RDMA 或编译工具链。支持 NVIDIA（CUDA）、AMD（ROCm/HIP）、Intel（Level Zero）三条已实现后端，并提供移植文档扩展到其他 PCIe 加速卡。核心约 2.5k 行 Python，仅依赖 torch 和 numpy，pip install 即可安装。适用对象是已持有显卡的用户；同厂商 P2P 可用时 README 建议仍用 NCCL/RCCL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨厂商张量并行：AMD + NVIDIA + Intel 卡可协同运行一个模型
- 纯 Python（约 2.5k 行），pip install 安装，无需编译、内核模块或 root
- 支持不均匀切分（按算力/显存比例分配注意力头）与 PD 分离部署
- 提供移植文档，可接入自定义 PCIe 加速卡

## 适用场景

- 手头已有不同品牌的显卡，想让它们共同跑一个 LLM 或视频生成模型
- 买不到同型号第二张卡时，用任意品牌卡扩展算力
- 跨厂商 prefill/decode 分离推理部署

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: Run one model across an AMD card and an NVIDIA card in the same box — **tensor parallel** over
> L35: |a compiler toolchain, kernel modules, root|`pip install`, pure Python|
> L79: **Is**: a pure-Python cross-process collective layer. Two processes, one GPU each, stage their

## 星数曲线

```mermaid
xychart-beta
    title "Fcys11/fccl 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f3bc52a51cf8` · [字段定义](../../DATASET.md)*
