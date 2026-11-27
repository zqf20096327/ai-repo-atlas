# wonseokjung/connect-ai-video-motion

⭐ 5 · JavaScript · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/wonseokjung/connect-ai-video-motion) · 个人维护

**给编码 Agent 的视频动效技能包：在人像视频上叠加动态图形**

通过 npx 安装到 Claude Code/Codex/Antigravity 等编码 Agent 的技能包，让 Agent 对用户视频执行分析、规划、校验、渲染流程，叠加 80 种动效图形。底层以 plan.json 每行调用 Remotion 包、HyperFrames 块、Lottie 文件与自定义组件；默认通过面部/身体/手部检测（15 次/秒）避让人脸放置图形。运行需 Node.js 18+，面部检测在 macOS 用 Vision，Windows/Linux 自动换用 MediaPipe。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 80 种动效图形，每种对应一行 plan.json
- 融合 Remotion、HyperFrames、Lottie、GSAP 的统一调用层
- 默认避让人脸/身体/手部（每秒 15 次检测）的放置机制
- npx install-skill 一条命令接入编码 Agent

## 适用场景

- 给口播带货或知识类视频添加动态图形
- 让编码 Agent 按自然语言指令完成视频动效剪辑
- 在无人出镜的画面区域叠加标注、图表与转场

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Open source by CONNECT AI LAB · AI education for everyone.** An AI content employee for commerce and knowledge con
> L9: One line. It gives your coding agent (Claude Code, Codex, Antigravity) the skill:
> L123: You need Node.js 18 or newer. No Python. The ffmpeg inside Remotion is used.

## 星数曲线

```mermaid
xychart-beta
    title "wonseokjung/connect-ai-video-motion 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-26 5 → 2026-11-27 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4652cb91c3f1` · [字段定义](../../DATASET.md)*
