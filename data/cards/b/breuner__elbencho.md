# breuner/elbencho

⭐ 304 · C++ · GPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/breuner/elbencho) · 个人维护

**面向文件/对象/块存储的分布式基准测试工具**

用 C++17 从零编写的统一存储基准测试工具，覆盖文件系统、对象存储（S3）与块设备的延迟、吞吐与 IOPS 测试，支持多节点分布式服务模式、N-to-M 网络测试、数据完整性校验与实时统计。GPU 侧通过 CUDA 与 GPUDirect Storage 测试存储访问性能，供运行深度学习等 GPU 负载的场景使用。可通过源码编译、Releases 预编译包或 Docker Hub 获取，提供 Slurm、Kubernetes 示例及 CSV/JSON 结果与图表工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件/对象/块三类存储的统一延迟、吞吐、IOPS 基准测试
- 通过 Nvidia CUDA 或 GPUDirect Storage 测试 GPU 存储访问性能
- 分布式服务模式支持本地与共享存储的多客户端测试
- 内置网络基准模式，支持 TCP、InfiniBand/RoCE、libfabric 等 N-to-M 通信

## 适用场景

- 在部署深度学习训练前测试 GPU 直连存储的读写性能
- 对分布式文件系统或多节点存储集群做吞吐与 IOPS 压测
- 测试 S3 对象存储服务的性能表现
- 对 NVMe 存储或块设备做延迟与吞吐基准

## 场景标签

 · 领域:系统工具/存储性能测试

## 证据(README 行号)

> L5: **A distributed storage benchmark for files, objects & blocks with support for GPUs**
> L16: * GPU storage access performance testing through Nvidia CUDA or GPUDirect Storage (GDS)
> L96: If GPU data transfer performance is critical for you, e.g. because you are running DeepLearning applications, you w

## 星数曲线

```mermaid
xychart-beta
    title "breuner/elbencho 星数(近 9 点)"
    x-axis ["2026-10-24", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-18", "2026-11-21", "2026-11-25", "2026-11-26"]
    y-axis "stars" 298 --> 305
    line [299, 300, 299, 300, 301, 302, 303, 304, 304]
```

2026-10-24 299 → 2026-11-26 304（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `3cf7aa82efeb` · [字段定义](../../DATASET.md)*
