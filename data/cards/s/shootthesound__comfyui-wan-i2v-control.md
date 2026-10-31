# shootthesound/comfyui-wan-i2v-control

⭐ 26 · Python · 推送 2026-06-07 · [GitHub](https://github.com/shootthesound/comfyui-wan-i2v-control) · 个人维护

**ComfyUI 节点包：WAN 图生视频的初始帧区域遮罩控制**

面向 ComfyUI 用户的节点包，作用于 WAN Image-to-Video 工作流：拦截 conditioning 并生成遮罩，控制初始帧中哪些区域参与 I2V 变换（如仅变脸而保留背景）。内置基于 MediaPipe 的人物检测，可对面部、头发、身体、衣物、背景及面部局部（眼睛/嘴唇等）生成遮罩，支持多人场景中按左右区域锁定单人，也支持外接自定义遮罩与深度图。附带 Drop First Frames 工具节点用于丢弃开头异常帧。通过 git clone 到 custom_nodes 目录安装，需 pip 安装 mediapipe，含示例工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 MediaPipe 的人物/面部检测遮罩（脸/发/身体/衣物/背景及面部局部）
- 多人场景下按 ignore_area/ignore_percent 锁定单人
- 外接自定义遮罩与 depth_map 距离遮罩输入
- 附带 Drop First Frames 工具节点丢弃 I2V 开头异常帧

## 适用场景

- 图生视频时只改变角色面部或发型、保留场景背景
- 多人画面中仅变换指定一人
- 用上一段视频末帧续接生成并刷新角色面部

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L11: This node pack intercepts the conditioning in WAN I2V and uses masking to control which parts of your **initial fra
> L40: 1. Add **WAN I2V Conditioning Mask Pro** node to your workflow

## 星数曲线

```mermaid
xychart-beta
    title "shootthesound/comfyui-wan-i2v-control 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `672e7689846c` · [字段定义](../../DATASET.md)*
