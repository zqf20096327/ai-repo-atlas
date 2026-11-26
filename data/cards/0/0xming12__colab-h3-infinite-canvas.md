# 0xming12/colab-h3-infinite-canvas

⭐ 3 · Jupyter Notebook · MIT · 推送 2026-11-14 · [GitHub](https://github.com/0xming12/colab-h3-infinite-canvas) · 个人维护 · 中文 README

**普通电脑用户借助 Colab 云端 GPU + 无限画布生成 AI 视频**

将 Google Colab、ComfyUI、MiniMax H3 与 Infinite Canvas 整合的视频生成工作流：在 Colab A100 上运行 H3 模型，通过官方 Colab CLI SSH 隧道将 8188 端口转发到本地画布，用户在可视化界面导入图片、配置工作流并生成视频。提供 4/8 步 Turbo LoRA、Qwen-Image-2.1 文生图接视频的工作流，以及环境恢复脚本与 Google Drive 权重持久化。README 注明画布端到端生成尚无独立核验记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Colab A100 运行 MiniMax H3，SSH 隧道连接本地 Infinite Canvas
- 5 秒/10 秒视频生成工作流，支持 4 步与 8 步 Turbo LoRA
- Qwen-Image-2.1 INT8 文生图/图生图接首尾帧视频
- restore_colab.py 从 Drive 恢复模型并启动 ComfyUI

## 适用场景

- 没有高端显卡时在云端生成 AI 视频
- 在无限画布中可视化组织素材与生成任务
- 用文生图先出图再接入首尾帧生成视频

## 场景标签

`视频生成` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: 这是一个开源的 AI 视频生成解决方案，将 **Google Colab、ComfyUI、MiniMax H3 和 Infinite Canvas（无限画布）** 整合成一套完整的创作工作流。
> L7: 无需在本地部署大型视频模型，也无需购买昂贵的高性能显卡。通过 Google Colab 提供的云端 GPU 运行 MiniMax H3，再利用安全的 SSH 隧道连接本地无限画布，即可在可视化界面中完成图片导入、工作流配置、视频生成
> L39: 在 Colab A100 的 ComfyUI 运行真实 MiniMax H3，通过官方 Colab CLI SSH 将只监听云端本机的 8188 端口转发到 Mac，再由 Infinite Canvas 的 ComfyUI 渠道提


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a1a11a04eaa9` · [字段定义](../../DATASET.md)*
