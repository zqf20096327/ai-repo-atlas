# afterdark-workers/h3-eros-max

⭐ 3 · Python · AGPL-3.0 · 推送 2026-11-07 · [GitHub](https://github.com/afterdark-workers/h3-eros-max) · 个人维护

**RunPod/Modal Serverless worker：图片生成带声音视频**

基于官方 runpod/worker-comfyui 的 RunPod Serverless worker，封装 tenstrip 的 H3 Eros Max beta7（MiniMax H3 融合模型），从单张图片经 8 步生成 5 秒 24fps 带声音的 MP4。模型文件烘焙进镜像（约 45 GB），构建时 SHA-256 校验，冷启动不重新下载。部署流程为 fork 私有仓库、填入 Civitai token、RunPod 建端点；同一 worker 也可通过 modal_app.py 部署到 Modal，接口一致。支持每请求远程 LoRA（默认最多 4 个）与构建时内置 LoRA。受 RunPod 30 分钟构建限制，需 48GB 以上 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图片生成带声音（语音/音效/音乐）的 5 秒 MP4 视频
- 模型烘焙进镜像，冷启动不重下，构建时 SHA-256 校验
- 同一 worker 可部署 RunPod 或 Modal，接口一致
- 支持请求级远程 LoRA 与构建时内置 LoRA

## 适用场景

- 在 RunPod 无服务器 GPU 上按需生成带声音视频
- 通过 Cobalt Pear 网页客户端附加图片生成视频
- 从 Civitai/Hugging Face 链接加载 LoRA 定制生成

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: A ready-to-build RunPod Serverless worker for **H3 Eros Max — beta7** by tenstrip, an adult MiniMax H3 merge that ma
> L41: |**GPU configuration**|tick every box of 48 GB or more, on both tabs **Previous generation** and **Latest generatio
> L75: The same worker also runs on Modal — another serverless GPU service, billed by the second — from `modal_app.py` in 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8652d0063801` · [字段定义](../../DATASET.md)*
