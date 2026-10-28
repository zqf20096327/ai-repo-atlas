# ashleykleynhans/runpod-worker-inswapper

⭐ 29 · Python · GPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/ashleykleynhans/runpod-worker-inswapper) · 个人维护

**RunPod Serverless 换脸推理 worker：14 种模型可选**

部署在 RunPod Serverless 上的 GPU 换脸 worker 源码，基于 FaceFusion 换脸模型与 InsightFace 人脸检测，支持 inswapper、simswap、ghost、hyperswap 等 14 种模型及参数化的人脸选择器（性别/年龄/排序）与脸部遮罩控制，并可用 CodeFormer 做修复。以 Docker 镜像构建后接入 RunPod 端点，通过 /run 或 /runsync API 提交 base64 图像请求，examples/ 目录提供各模型可运行的 Python 脚本。面向需要在无服务器 GPU 环境部署换脸 API 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 14 种换脸模型（含 inswapper_128 默认与 simswap_unofficial_512 高质量选项）
- 人脸选择器支持数量/性别/年龄范围/排序过滤
- 通过 /run 与 /runsync 端点异步或同步调用，附状态码说明
- 每个模型带 examples/ 可运行示例脚本

## 适用场景

- 在 RunPod Serverless 上部署换脸 API 端点
- 按质量/速度权衡选择不同换脸模型批量处理图像
- 在多人照片中按性别或年龄筛选目标人脸进行替换

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: This is the source code for a RunPod
> L4: Serverless worker for face swapping using
> L17: The worker uses the `inswapper_128.onnx` model by [InsightFace](
> L22: The worker supports 14 different face swap models with varying quality/speed trade-offs.

## 星数曲线

```mermaid
xychart-beta
    title "ashleykleynhans/runpod-worker-inswapper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8ac04770fa05` · [字段定义](../../DATASET.md)*
