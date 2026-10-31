# BlockRunAI/franklin-canvas

⭐ 17 · TypeScript · NOASSERTION · 推送 2026-09-05 · [GitHub](https://github.com/BlockRunAI/franklin-canvas) · 组织维护

**节点式 AI 媒体工作室：无限画布生成图像/视频/音乐**

开源的节点画布式 AI 媒体生成应用：在无限画布上放置 Text/Image/Video/Music 等节点，串联成工作流生成图像（7 模型）、视频（5 模型）、音乐（1 模型）；Media Agent 为工具调用循环，可从一句话生成分镜、逐镜头生成并剪辑短片。支持单提示词最多 5 个视频模型并行生成并拼接对比，内置 848 条提示词库与时间轴播放列表。计费按次：BlockRun 账户 API key 或本地 Solana/Base 钱包 USDC（x402）。React 前端 + Node 后端，需 Node 18+，git clone 后 npm 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个图像模型、5 个视频模型、1 个音乐模型按节点混用
- Media Agent 工具调用循环：生成、串联、编辑、放大、拼接并视觉自检
- 单提示词最多 5 个视频模型并行生成并拼接（网格/顺序、横屏/9:16）
- 两种按次计费：BlockRun API key 或 x402 钱包 USDC（Solana/Base）

## 适用场景

- 在无限画布上串联图像→视频→拼接的工作流生成内容
- 用一句话让 AI Agent 生成并剪辑整部短片
- 同一提示词并行对比多个视频模型的效果
- 为 TikTok 等平台生成 9:16 竖屏视频

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: A node-based AI media studio — generate images, video and music on an
> L21: An infinite canvas for **image, video and music**, with side-by-side **model comparison**,
> L45: - **🤖 Media Agent.** Describe what you want — *"a cinematic fox clip in a snowy forest,

## 星数曲线

```mermaid
xychart-beta
    title "BlockRunAI/franklin-canvas 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27", "2026-10-31"]
    y-axis "stars" 12 --> 18
    line [13, 15, 16, 17]
```

2026-10-18 13 → 2026-10-31 17（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ffdeca5f3217` · [字段定义](../../DATASET.md)*
