# FareedKhan-dev/glm-5.2-in-c

⭐ 75 · C · Apache-2.0 · 推送 2026-07-15 · [GitHub](https://github.com/FareedKhan-dev/glm-5.2-in-c) · [官网](https://medium.com/@fareedkhandev/77a3df56e7b4) · 个人维护

**纯 C 推理引擎：让 744B GLM-5.2 在消费级硬件上运行**

用单文件纯 C 引擎（glm.c，约 3900 行，无 BLAS/框架）运行 GLM-5.2 744B MoE 模型：将厂商 FP8 权重离线转为 int4，常驻部分（约 17B 参数/9.9GB@4bit）留在内存，其余 362GB 专家按需用 pread 从磁盘流式读取并经 VRAM/pinned RAM/LRU/页缓存分层缓存。支持无 GPU 的 16GB 内存笔记本运行（实测约 0.37 tokens/s），可选 CUDA 后端与 OpenAI 兼容服务。含基准测试与测量数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件纯 C 引擎编译为约 377KB 二进制，无 BLAS 无框架
- int4 量化 + 专家磁盘流式加载，744B 模型可在 16GB RAM 无 GPU 机器生成
- VRAM/锁定内存/LRU/页缓存/磁盘多级专家分层与投机解码（多 token 头/n-gram/语法）
- OpenAI 兼容服务端，含调度、流式与背压

## 适用场景

- 在个人笔记本/台式机上本地运行超大参数 MoE 模型
- 学习 MoE 流式推理、int4 量化内核与内存分层的实现细节
- 以消费级硬件成本部署 OpenAI 兼容的本地推理服务

## 场景标签

 · 领域:LLM 推理引擎

## 证据(README 行号)

> L7: **GLM 5.2** is a **744 billion parameter** model, about 1.5 terabytes in bfloat16, and the usual way to run somethin
> L21: - **Serve it**: an OpenAI compatible server with a proper scheduler, streaming, and backpressure.

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/glm-5.2-in-c 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 73 --> 76
    line [74, 75, 75]
```

2026-10-18 74 → 2026-10-24 75（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `665dff2cbc26` · [字段定义](../../DATASET.md)*
