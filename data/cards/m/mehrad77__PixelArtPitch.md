# mehrad77/PixelArtPitch

⭐ 4 · TypeScript · 推送 2026-11-09 · [GitHub](https://github.com/mehrad77/PixelArtPitch) · 个人维护

**多智能体协作生成分辨率320×180像素风短片的工作室**

本地运行的工作室：用户输入一条消息（如应用 30 秒 pitch、发布预告、demo day 开场），Pip 编排一支 AI 智能体团队（Writer、Director、Pixel Artists、Animator、Sound Designer、Editor、Reviewer 等）在 320×180 画布上分工完成脚本、动画与声音，仅在关键节点请用户挑选。字节精确渲染引擎保证同文档输出一致帧与音频，模型调用前预留预算上限，工具经 MCP（stdio 与 Streamable HTTP）对外提供。需 Node ≥ 24.21、pnpm 与 ffmpeg；代码尚未选定许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多智能体团队分工生成像素风短片，用户在关键节点做挑选
- 字节精确引擎：同一文档每次渲染相同帧与 WAV
- 预算硬上限：每次模型调用预留最坏情况开销，超限前征询用户
- 工具注册表通过 MCP 服务，其他 agent 可驱动项目或加入团队

## 适用场景

- 为应用制作 30 秒 pitch 短片
- 生成产品发布预告或 demo day 开场视频
- 本地私有环境下用多模型编排视频制作流程

## 场景标签

`多智能体` `视频生成` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Short pixel-art pitch videos, made by a crew of AI agents while you watch, steer and pick.**
> L15: You tell Pip what you're making: a 30-second pitch for your app, a launch teaser, a demo-day opener. Pip runs a cre
> L26: - **Everything is a tool.** Pip, the crew and the studio share one tool registry, and the same tools are served ove

## 星数曲线

```mermaid
xychart-beta
    title "mehrad77/PixelArtPitch 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-14", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `4725c184cf44` · [字段定义](../../DATASET.md)*
