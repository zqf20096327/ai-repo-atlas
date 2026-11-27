# JustJoyful/ffwd

⭐ 3 · Python · GPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/JustJoyful/ffwd) · [官网](https://ffwd.pages.dev/) · 个人维护

**面向非开发者的 0.6B 本地模型：将自然语言视频剪辑需求转为经校验的 FFmpeg 操作**

本仓库是 ffwd 的模型侧：基于 Qwen3-0.6B 微调（SFT 加多轮 GRPO）的端侧 agent，将日常视频小任务（剪切、合并、转码、抽帧、压体积等 12 类）转成 FFmpeg 命令。协议规定模型每轮只输出一个 JSON 动作，运行器（harness）用白名单校验参数列表并检查输出是否符合 spec，模型看不到真实路径。同一 GGUF 文件供浏览器（wllama/WebGPU）与原生 CLI 运行。README 明确标注为 early preview：评测仅基于生成任务，真实用户表述的准确率未测量，且已有明确失败案例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 模型每轮输出一个 JSON 动作（spec/ask_user/unsupported/run/finish），由确定性代码校验
- FFmpeg 参数白名单校验器：51 选项/14 编码器/31 滤镜，不执行 shell 字符串
- 同一 GGUF 供浏览器与 CLI 两种路径运行，900 个生成任务上给出带置信区间的评测数字
- 提供训练（SFT+GRPO）、任务生成、评测与原生 CLI

## 适用场景

- 在本地完成剪切、合并、转 720p、压缩到指定体积等偶发视频小任务
- 让 iPhone 视频转为能在 PowerPoint 播放的格式
- 不联网上传的前提下抽取视频帧或提取音频

## 场景标签

`图像视频处理` `微调` `强化学习` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: **A 0.6B-parameter FFmpeg agent that turns a plain-language video chore into a checked FFmpeg command, small enough 
> L16: Many people hit a video chore (trim a clip, fix a file that will not play in a slide deck, pull frames out of a vid
> L22: **What a 0.6B on-device agent is for.** The model has one narrow job, so a small model can do it; running it on the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `ee5af298e4a0` · [字段定义](../../DATASET.md)*
