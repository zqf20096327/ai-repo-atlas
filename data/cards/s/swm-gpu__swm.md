# swm-gpu/swm

⭐ 26 · Python · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/swm-gpu/swm) · [官网](https://swmgpu.com) · 组织维护

**跨 10 家云 GPU 供应商统一搜索、开通与管理的 CLI**

面向使用云端 GPU 的开发者与 MLOps 人员的命令行工具：跨 RunPod、Vast.ai、Lambda Labs、AWS/GCP/Azure 等 10 家供应商搜索实时 GPU 价格与可用性、创建/停止实例；通过 S3 兼容存储（B2/S3/GCS）实现 /workspace 目录跨云同步，支持增量与后台自动同步。另提供框架安装（vLLM、Open WebUI、ComfyUI 等）、HuggingFace/Civitai 模型拉取与统一模型存储、闲置自动关机、成本追踪与预算告警。所有操作经 SSH 完成，不在实例上驻留代理。需 macOS/Linux、SSH 客户端与至少一家 GPU 供应商账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 10 家供应商的 GPU 搜索、开通、停止/恢复与计费 API 支持
- 基于 S3 兼容存储的三级工作区同步（watcher/增量/tar 打包）
- 一键安装 vLLM、Open WebUI、ComfyUI 等框架并自动配好模型路径
- 生命周期守卫（闲置检测自动同步并关机）与成本追踪、预算告警

## 适用场景

- 比较各家云 GPU 价格并快速开通 H200 等实例跑训练或推理
- 在多个云供应商之间保持 /workspace 工作目录同步
- 防止闲置 GPU 实例产生高额过夜账单
- 让 AI agent（Cursor、Claude Code 等）通过 SKILL.md 代管 GPU

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7:  One CLI to rule all GPU clouds.
> L97: swm setup install vllm runpod:<id>       # vLLM inference server

## 星数曲线

```mermaid
xychart-beta
    title "swm-gpu/swm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a97ced79ccf3` · [字段定义](../../DATASET.md)*
