# Luna-AI-Infra/ComfyUI-H3-2080Ti-TP

⭐ 3 · Cuda · GPL-3.0 · 推送 2026-11-07 · [GitHub](https://github.com/Luna-AI-Infra/ComfyUI-H3-2080Ti-TP) · 个人维护

**让双卡 2080 Ti 在 ComfyUI 中以张量并行跑 MiniMax H3 视频生成**

一个面向 ComfyUI 的实验性自定义节点包，针对两块经 NVLink 互连的 RTX 2080 Ti 22GB（SM75）实现 H3 transformer 的 TP2 张量并行，包含 INT8 ConvRot 线性层、事件驱动的 GPU 间交换、分组双缓冲权重流送、CPU 权重包缓存，以及带预编译库的 SM75 内核。需已有 Linux ComfyUI 环境与两块支持 P2P 的 CUDA GPU，通过 git clone 安装并下载指定模型变体（约 55 GiB 校验读取）。README 明确限定目标硬件，未验证其他互连方式，多行结果为单次观测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- H3 transformer 的 TP2 张量并行与分组双缓冲权重流送
- SM75 调优内核提供源码、构建脚本与校验和固定的 Linux 预编译库
- 规范 CPU 包缓存支持不同视频长度的重复任务复用
- VAE 可选 FP32/mixed/FP16 TP2 策略与解码器预取

## 适用场景

- 在双 2080 Ti 22GB NVLink 平台上用 ComfyUI 生成 H3 视频
- 在有限显存下通过权重流送与缓存运行大模型视频工作流
- 复现 README 记录的 5s/10s/15s 视频生成实验配置

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: **An RTX 2080 Ti / SM75 acceleration project for ComfyUI, measured on two 22 GB cards connected by NVLink.**
> L26: This experimental custom-node pack builds on Comfy-H3-MultiStream. Its development target is a Supermicro X9DAi wit
> L36: - **TP2 for the H3 transformer:** INT8 ConvRot linear layers, direct event-driven GPU-to-GPU exchange, chunked acti

## 星数曲线

```mermaid
xychart-beta
    title "Luna-AI-Infra/ComfyUI-H3-2080Ti-TP 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `e5cd4405c6b5` · [字段定义](../../DATASET.md)*
