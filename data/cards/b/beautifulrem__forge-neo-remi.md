# beautifulrem/forge-neo-remi

⭐ 713 · Python · AGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/beautifulrem/forge-neo-remi) · 个人维护 · 中文 README

**面向 Anima 等 DiT 模型的本地 AI 图像生成 WebUI**

Forge Neo 的下游分支，构建于 Stable Diffusion WebUI Forge 与 AUTOMATIC1111 之上，用 FastAPI + React 19 SPA 替代 Gradio，提供持久任务队列、SQLite 队列与 REST/WebSocket API。功能覆盖生图、img2img、画廊看板、资产谱系、参数对比、非节点式多阶段流水线与 Recipes，支持 Anima 2B/2.9B/3.8B、Qwen-Image、FLUX、SDXL 等模型家族及 GGUF/FP8 等量化格式。面向 8–24 GB 消费级 GPU 与 Apple Silicon 用户，需 Python 3.13 与 Node.js 构建前端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gradio-free React 19 SPA + FastAPI，含持久任务队列与 REST /sdapi/v1 API
- Anima 2B/2.9B/3.8B 全支持，含 LoRA、ControlNet-LLLite、Control-LoRA/VACE
- 支持 GGUF、FP8、INT8-ConvRot、NVFP4、SVDQuant 等量化与加速路径
- Worker 隔离、多 GPU 池与 Apple Silicon MPS/MLX 支持（worker 模式为预览）

## 适用场景

- 在消费级 GPU 上本地运行 Anima/Qwen-Image/FLUX 等模型生成图像
- 通过 REST API 把图像生成接入自己的工作流
- 用 Recipes 与线性流水线做提示词扩写→生成→精修的多阶段流程
- 用画廊看板与资产谱系管理生成的图片与迭代历史

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: **A zero-node, conflict-safe, studio-grade AI image creation workbench built on Stable Diffusion WebUI Forge Neo — A
> L14: Forge Neo Remi is a downstream distribution of Forge Neo, itself built on Stable Diffusion WebUI Forge and AUTOMATI
> L24: - **Anima-first inference & conflict-safe runtime.** Full 2B / 2.9B / 3.8B support (28/40/52-block layouts + native


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `08ebfb6e2ce1` · [字段定义](../../DATASET.md)*
