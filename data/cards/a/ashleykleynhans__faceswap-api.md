# ashleykleynhans/faceswap-api

⭐ 33 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/ashleykleynhans/faceswap-api) · 个人维护

**给开发者的 GPU 加速人脸替换 API 服务（14 模型+CodeFormer）**

基于 FastAPI 的人脸替换 API 服务，提供 14 种换脸 ONNX 模型（inswapper、simswap、ghost 等）、CodeFormer 人脸修复与 RealESRGAN 背景放大。内置异步任务队列，每次串行处理一个请求以控制显存占用；支持人脸性别/年龄筛选与身份混合权重配置，Swagger 文档自动生成于 /docs。安装需 git clone 后 pip 装依赖，先克隆 CodeFormer 仓库再运行下载脚本获取约 5.3 GB 权重。README 声明仅供教育与研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 种换脸模型可选（inswapper/simswap/ghost/hyperswap 等）
- VRAM 安全的串行异步任务队列，支持同步/异步两种模式
- CodeFormer 人脸修复 + RealESRGAN 背景放大，默认开启
- 提供 Docker 构建与多平台安装说明（Linux/Mac/Windows/Runpod）

## 适用场景

- 为应用集成人脸替换能力，通过 REST API 提交与轮询任务
- 批量处理图片的人脸替换与画质修复
- 在 GPU Pod（如 Runpod）上部署换脸服务

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: GPU-accelerated face swapping API with 14 face swap models,
> L18: - **14 face swap models**: inswapper, simswap, ghost, hififace, hyperswap, blendswap, uniface, alphaface
> L155: |`POST`|`/faceswap`|Submit async face swap (returns 202 with job ID)|

## 星数曲线

```mermaid
xychart-beta
    title "ashleykleynhans/faceswap-api 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-28"]
    y-axis "stars" 30 --> 34
    line [31, 32, 33, 33]
```

2026-10-18 31 → 2026-10-28 33（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1fad9646c993` · [字段定义](../../DATASET.md)*
