# baker27727/ds4-8gb-cpu

⭐ 40 · C · MIT · 推送 2026-08-18 · [GitHub](https://github.com/baker27727/ds4-8gb-cpu) · 个人维护

**在 8GB RAM 无 GPU 的 Linux 上跑 78.62 GiB DeepSeek V4 Flash 的研究性推理 fork**

antirez/ds4（DwarfStar）的研究分支，验证在 7.7 GiB 物理内存、纯 CPU 的 Linux 笔记本上，通过 mmap 持久化的 NVMe 按需分页执行 78.62 GiB 的 DeepSeek V4 Flash GGUF。新增 AProjQ4 CPU 支持与可选需求分页路径（DS4_CPU_NO_PREFETCH=1），需 make cpu 从源码编译。仓库附证据登记、基准数据与明确的声明边界，自述为 v0.1 Research Preview，明确不声明生产级推理速度或持续生成吞吐，V18 运行时研究仍在进行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 78.62 GiB GGUF 在 7.7 GiB RAM、纯 CPU 环境下经 NVMe 需求分页执行并公开复现数据
- 新增 AProjQ4 CPU 支持与 DS4_CPU_NO_PREFETCH 需求分页开关
- 附证据登记册、基准数据与明确的不声明边界
- 上游 DwarfStar 引擎另支持 Metal/CUDA/ROCm 后端与 GLM 5.2

## 适用场景

- 在内存远小于模型体积的机器上验证 CPU-only 大模型执行可行性
- 研究 Linux VM 按需分页、缺页与专家权重 I/O 行为
- 复现受控的冷启动首 token 诊断实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **Run a 78.62 GiB DeepSeek V4 Flash GGUF on a Linux laptop with 7.7 GiB of physical RAM and no GPU, using mmap-backe
> L61: The public v0.1 claim is intentionally narrow: CPU-only execution of an AProjQ4 DeepSeek V4 Flash GGUF on a memory-

## 星数曲线

```mermaid
xychart-beta
    title "baker27727/ds4-8gb-cpu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f901941bd59d` · [字段定义](../../DATASET.md)*
