# replicate/cog-comfyui

⭐ 769 · Python · MIT · 推送 2025-11-03 · [GitHub](https://github.com/replicate/cog-comfyui) · [官网](https://replicate.com/fofr/any-comfyui-workflow) · 组织维护

**在 Replicate 上运行 ComfyUI 工作流的 Cog 模板仓库**

Replicate 官方维护的 ComfyUI 封装仓库：预置主流模型权重与自定义节点，用户导出 ComfyUI 工作流的 API JSON，通过 cog predict 或 Replicate API 在云端运行，支持 URL、单文件与 zip/tar 上传输入，可从 CivitAI/HuggingFace 加载 LoRA。README 详述三种专属实例方式（私有部署、用 Cog 部署 fork、train 标签自建模型），并提供本地开发流程（克隆子模块、安装自定义节点、在 Cog 容器内启动 Web UI），需要 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预置主流模型权重与自定义节点清单
- 通过 API JSON 在 Replicate 云端运行 ComfyUI 工作流
- 支持 URL/单文件/zip/tar 三种输入上传方式
- 可从 CivitAI/HuggingFace 以 URL 直接加载 LoRA

## 适用场景

- 把现有 ComfyUI 工作流通过 API 集成到自己的应用
- 在 Replicate 上部署专属 ComfyUI 实例以固定版本、加速推理
- 以此仓库为模板创建自定义 ComfyUI 模型（自选节点与权重）

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Run ComfyUI workflows on Replicate:
> L158: You can use this repository as a template to create your own model. This gives you complete control over the Comfy

## 星数曲线

```mermaid
xychart-beta
    title "replicate/cog-comfyui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 768 --> 770
    line [769, 769]
```

2026-10-18 769 → 2026-10-25 769（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `150058204ad6` · [字段定义](../../DATASET.md)*
