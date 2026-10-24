# vavo/lora-pilot

⭐ 89 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/vavo/lora-pilot) · [官网](https://www.lorapilot.com) · 个人维护

**一体化 Docker 镜像：LoRA 训练到图像/视频生成的浏览器工作区**

将数据集准备、模型管理、LoRA 训练、推理与媒体浏览打包进单个 Docker 容器的 Stable Diffusion 工作区。内置 Kohya SS、AI Toolkit、Diffusion Pipe 三套训练栈与 ComfyUI、InvokeAI 推理栈，支持 51 个训练模型组（图像/视频/音频），由 supervisord 编排，全部数据持久化在 /workspace。提供 ControlPilot 控制面板、TagPilot 数据标注、TrainPilot 引导训练与 MediaPilot 成品浏览。可部署到 RunPod 模板或本地 Docker Compose，面向自有 GPU 或云 GPU 用户；文档提示该镜像面向受信任环境，内部控制面不应暴露公网。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单容器集成 Kohya SS / AI Toolkit / Diffusion Pipe 三套训练栈与 ComfyUI / InvokeAI 推理栈
- 支持 51 个训练模型组，覆盖图像、视频与音频生成
- models pull 命令与 Web 界面内置模型下载
- 所有模型/数据集/输出/配置持久化在 /workspace

## 适用场景

- 在自有 GPU 或 RunPod 上从数据集一路完成 LoRA 训练与出图
- 在同一工作区内切换多套训练与推理环境，避免环境配置冲突
- 通过浏览器管理训练队列、日志与生成成品的浏览整理

## 场景标签

`微调` `图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: > End-to-end Stable Diffusion workspace in one container, with one persistent `/workspace`.
> L17: - **Three proven LoRA trainer stacks** in one place: Kohya SS, AI Toolkit, and Diffusion Pipe (plus TrainPilot for 
> L18: - **51 training model groups** without juggling five half-compatible environments.

## 星数曲线

```mermaid
xychart-beta
    title "vavo/lora-pilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-24 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d42ebd7160d6` · [字段定义](../../DATASET.md)*
