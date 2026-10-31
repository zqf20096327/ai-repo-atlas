# ashleykleynhans/runpod-worker-comfyui

⭐ 24 · Python · GPL-3.0 · 推送 2026-05-23 · [GitHub](https://github.com/ashleykleynhans/runpod-worker-comfyui) · 个人维护

**在 RunPod Serverless 上运行 ComfyUI 推理的 worker**

RunPod Serverless worker 源码，通过 ComfyUI API 执行 Stable Diffusion 推理：模型从 RunPod Network Volume 加载，handler.py 处理 API 请求并返回输出。部署流程为在 Network Volume 安装 ComfyUI、构建 Docker 镜像、发布到 RunPod Serverless。API 支持 /run（异步）与 /runsync（同步，超 90 秒转异步查状态）两种端点，可选 Webhook 回调，并定义 IN_QUEUE/IN_PROGRESS/COMPLETED 等状态码。面向需要在 RunPod 上自建图像生成 API 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 ComfyUI API 的 RunPod Serverless 推理 worker
- 模型从 RunPod Network Volume 加载，无需打包进镜像
- 支持 /run 异步与 /runsync 同步端点及可选 Webhook 回调
- 提供本地示例、RunPod 示例与单元测试套件

## 适用场景

- 在 RunPod Serverless 上部署 ComfyUI 图像生成 API
- 按队列异步处理 Stable Diffusion 推理请求
- 通过 Webhook 获取推理任务完成通知

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: This is the source code for a Runpod
> L4: Serverless worker that uses the [ComfyUI API](
> L67: The serverless handler (`handler.py`) is a Python script that handles

## 星数曲线

```mermaid
xychart-beta
    title "ashleykleynhans/runpod-worker-comfyui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2fa14586b502` · [字段定义](../../DATASET.md)*
