# runpod-workers/worker-a1111

⭐ 101 · Python · MIT · 推送 2025-11-21 · [GitHub](https://github.com/runpod-workers/worker-a1111) · 组织维护

**在 RunPod Serverless 上运行 A1111 的 Stable Diffusion 推理 worker**

RunPod 官方维护的 serverless worker 项目：以容器形式运行 Automatic1111 Stable Diffusion WebUI，并将其 /sdapi/v1/txt2img 端点暴露为 serverless API；请求的 input 对象可传入该端点的任意有效参数（seed、sampler_name、batch_size、styles 等）。镜像内预装 Deliberate v6 模型，收到 prompt 即可生成图像。面向需要在 RunPod 平台部署无服务器文生图服务的开发者，README 未给出本地部署细节。

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

- 容器化运行 Automatic1111 WebUI 并暴露 txt2img API
- input 可透传 A1111 /sdapi/v1/txt2img 的任意参数
- 预装 Deliberate v6 模型

## 适用场景

- 在 RunPod Serverless 上按需部署 Stable Diffusion 文生图
- 通过 serverless API 批量调用 txt2img 生成图像
- 无需自建前端即可复用 A1111 的参数体系

## 场景标签

 · 领域:图像生成/推理部署

## 证据(README 行号)

> L5: - Runs Automatic1111 Stable Diffusion WebUI and exposes its `txt2img` API endpoint
> L10: The `input` object accepts any valid parameter for the Automatic1111 `/sdapi/v1/txt2img` endpoint. Refer to the Aut

## 星数曲线

```mermaid
xychart-beta
    title "runpod-workers/worker-a1111 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-23 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c0dad7a589aa` · [字段定义](../../DATASET.md)*
