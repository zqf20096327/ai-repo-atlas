# QosmoInc/Spot-if-AI

⭐ 29 · TypeScript · MIT · 推送 2026-03-25 · [GitHub](https://github.com/QosmoInc/Spot-if-AI) · 组织维护

**检测 Spotify 歌曲是否为 Suno/Udio 生成的 Chrome 扩展**

Chrome 扩展，在 Spotify Web Player 页面显示歌曲由 Suno/Udio 等 AI 音乐工具生成的置信度（红条=疑似 AI、绿条=疑似人类创作）。检测基于 SONICS 研究的模型，转换为 ONNX 后通过 ONNX runtime 在浏览器本地执行，分析 Spotify 预览音频中间 5 秒片段。面向普通听众与关注 AI 音乐透明度的人群。公开测试已结束、扩展已从 Chrome 商店下架，源代码保留供自行构建；无法检测 Suno v4 等新模型生成的歌曲。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SONICS 模型经 ONNX 转换后在浏览器内本地运行
- 在歌曲/专辑页显示 AI 生成置信度条
- 基于音频中人类创作细节缺失与 AI 特征伪影的检测原理

## 适用场景

- 浏览 Spotify 时想知道某首歌是否由 AI 生成
- 审视 AI 生成音乐在流媒体平台的传播情况
- 在源码基础上扩展或改进 AI 音乐检测功能

## 场景标签

 · 领域:AI 内容检测/音乐

## 证据(README 行号)

> L9: Spot-if-AI is a Chrome extension that analyzes whether songs on Spotify have been generated with Suno or Udio. It wo
> L33: Our detection model is based on the research paper SONICS by Rahman et al. (2025). The detection models are trained

## 星数曲线

```mermaid
xychart-beta
    title "QosmoInc/Spot-if-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bc9a03942d4f` · [字段定义](../../DATASET.md)*
