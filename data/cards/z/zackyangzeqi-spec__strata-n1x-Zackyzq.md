# zackyangzeqi-spec/strata-n1x-Zackyzq

⭐ 3 · CSS · MIT · 推送 2026-10-31 · [GitHub](https://github.com/zackyangzeqi-spec/strata-n1x-Zackyzq) · [官网](https://zackyangzeqi-spec.github.io/strata-n1x-Zackyzq/) · 个人维护 · 中文 README

**在 N1X 128GB Windows ARM64 笔记本本地运行 DeepSeek 1017 的推理与桌面工具**

基于 Niko1221/Strata 的社区适配项目，面向 NVIDIA RTX Spark N1X 128GB 统一内存、Windows ARM64 笔记本，把本地模型加载、卸载、运行监控和本机 API 整理为桌面工作流。运行 DeepSeek-V4.1-Flash-1017 的 ISTA-DASLab GSQ-RCO GGUF 第三方量化版本，提供原生 CUDA 推理引擎与 OpenAI 兼容本地 API，可接入 DeepSeek Harness 作为客户端。当前为实验性预览：结果来自维护者单台设备，安装包未签名且不含模型权重与 NVIDIA 驱动，完整干净源码构建未获独立验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Windows ARM64 原生 CUDA 推理引擎，无需 LM Studio 或 WSL 推理桥
- 桌面端模型加载、卸载与运行监控
- 本机 OpenAI 兼容 API，可接入 DeepSeek Harness（DSH）
- 公开实测记录含提示词缓存复用与较慢对照结果

## 适用场景

- 在 N1X 128GB 笔记本上私有化运行 DeepSeek 1017 量化模型
- 给 DeepSeek Harness 配置本地推理后端
- 查阅分量化、分场景的本地推理速度与缓存记录

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: **Strata N1X** is a free community adaptation of Strata, maintained by **Zack_yzq** for **NVIDIA RTX Spark N1X lapt
> L32: |Run DeepSeek 1017 on N1X Windows|A native Windows ARM64 CUDA **inference engine**; the control layer still include
> L34: |Use DeepSeek Harness as the client|A local OpenAI-compatible API; DSH manages its conversations and tools|

## 星数曲线

```mermaid
xychart-beta
    title "zackyangzeqi-spec/strata-n1x-Zackyzq 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `5fa6f9c0d0d7` · [字段定义](../../DATASET.md)*
