# Anil-matcha/ai-clipping-comfyui

⭐ 31 · Python · MIT · 推送 2026-07-21 · [GitHub](https://github.com/Anil-matcha/ai-clipping-comfyui) · 组织维护

**ComfyUI 节点包：调 muapi.ai 把长视频切成热门短视频**

面向 ComfyUI 用户的 AI 视频剪辑节点包：通过单次 muapi.ai API 调用，将长视频/播客/访谈在服务端完成 Whisper 转录、传播力排名、去重与人脸追踪竖屏裁切，返回带病毒分数（0-100）、钩子句与推荐理由的短视频片段；输出 JSON 可接入下游节点链。提供 4 个节点（API Key、剪辑、选片、保存视频），支持 9:16/1:1/4:5 比例与仅返回坐标模式。限制：需 muapi.ai API key，按量计费，无本地模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 服务端一站式流水线：Whisper 转录 + 传播力排名 + 去重 + 人脸追踪竖屏裁切
- 每个片段返回病毒分数（0-100）、钩子句与推荐理由的 JSON
- coordinates-only 模式可仅返回时间段，用自有 ffmpeg/VHS 管线渲染
- 提供 4 个 ComfyUI 节点与示例工作流（单片段/扇出多片段）

## 适用场景

- 在 ComfyUI 工作流中把播客/访谈自动切成 TikTok/Shorts/Reels 短视频
- 按传播力分数挑选并保存排名最高的多个片段
- 将剪辑节点接入已有的放大、字幕、口型同步等下游节点链

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L4: > Turn long-form videos, podcasts, interviews, lectures, and livestreams into ranked viral-ready short clips for **Y
> L52: |✂️ AI Clipping|Long video → ranked vertical short clips (full pipeline)|

## 星数曲线

```mermaid
xychart-beta
    title "Anil-matcha/ai-clipping-comfyui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-26 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c53b304f979e` · [字段定义](../../DATASET.md)*
