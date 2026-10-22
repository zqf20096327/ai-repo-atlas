# breuner/elbencho

⭐ 299 · C++ · GPL-3.0 · 推送 2026-10-12 · [GitHub](https://github.com/breuner/elbencho) · 个人维护

**分布式存储基准测试工具：测文件/对象/块存储性能**

用 C++17 从零编写的统一存储基准工具，覆盖文件系统、对象存储（S3）与块设备的延迟、吞吐与 IOPS 测试；支持分布式服务模式测试本地与共享存储、Nvidia CUDA 与 GPUDirect Storage 的 GPU 存取性能测试、实时统计、CSV/JSON 输出与图表工具、数据完整性校验。面向存储系统与 HPC/深度学习基础设施的运维和评估人员。提供源码编译（make deb/rpm）方式，Releases 与 Docker Hub 提供预编译 Linux/Windows 版本；S3 支持默认关闭需手动开启，macOS 需通过 homebrew 安装依赖编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件/对象/块存储统一的延迟、吞吐与 IOPS 基准
- 分布式服务模式测试本地与共享存储
- 通过 CUDA 与 GPUDirect Storage (GDS) 进行 GPU 存取性能测试
- 实时统计、CSV/JSON 输出与 elbencho-chart 图表工具

## 适用场景

- 评估 NVMe 或机械盘存储在多线程负载下的吞吐与 IOPS
- 多节点分布式测试共享文件系统或 S3 对象存储性能
- 深度学习场景下测量 GPU 直连存储的数据传输性能

## 场景标签

 · 领域:存储/性能测试

## 证据(README 行号)

> L5: **A distributed storage benchmark for files, objects & blocks with support for GPUs**
> L7: elbencho was inspired by traditional storage benchmark tools like fio, mdtest and ior, but was written from scratch 
> L16: * GPU storage access performance testing through Nvidia CUDA or GPUDirect Storage (GDS)
> L96: If GPU data transfer performance is critical for you, e.g. because you are running DeepLearning applications, you w

## 星数曲线

```mermaid
xychart-beta
    title "breuner/elbencho 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 298 --> 300
    line [299, 299]
```

2026-10-18 299 → 2026-10-22 299（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `be775e11bdcb` · [字段定义](../../DATASET.md)*
