# ashleykleynhans/runpod-worker-a1111

⭐ 16 · Python · GPL-3.0 · 推送 2026-02-16 · [GitHub](https://github.com/ashleykleynhans/runpod-worker-a1111) · 个人维护

**在 RunPod Serverless 上封装 A1111 Stable Diffusion API 的工作器**

提供 RunPod Serverless worker 源码，调用 Automatic1111 Stable Diffusion Web UI 的 API 执行文生图、图生图等推理，内置 ControlNet、ReActor、ADetailer 扩展。模型从 RunPod Network Volume 加载，经 /run 与 /runsync 端点异步或同步处理请求，支持可选 Webhook 回调。部署需先在 Network Volume 安装 A1111 Web UI，再构建 Docker 镜像。注意 A1111 1.9.0 API 不向后兼容，需旧格式者应使用本 worker 的 2.5.0 版本与 A1111 1.8.0。

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

- 通过 /run、/runsync 端点暴露 A1111 API，支持 IN_QUEUE 等 6 种状态
- 内置 ControlNet、ReActor、ADetailer 扩展
- 覆盖文生图/图生图/Interrogate/模型切换等 A1111 API 及文件下载、Huggingface 同步辅助 API
- serverless handler（rp_handler.py）基于 runpod Python 库处理请求

## 适用场景

- 把 Stable Diffusion 图像生成部署为 RunPod Serverless API 端点
- 按需弹性运行文生图/图生图推理任务
- 通过 Webhook 获取生成任务完成回调

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: This is the source code for a RunPod
> L4: Serverless worker that uses the [Automatic1111 Stable Diffusion API](

## 星数曲线

```mermaid
xychart-beta
    title "ashleykleynhans/runpod-worker-a1111 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3fa82cd02760` · [字段定义](../../DATASET.md)*
