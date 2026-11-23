# furkancavlak/claude-shorts-editor

⭐ 3 · Python · MIT · 推送 2026-11-19 · [GitHub](https://github.com/furkancavlak/claude-shorts-editor) · 个人维护

**让个人 Claude Code 代理从原始录像剪辑竖版 Short 的本地剪辑引擎**

本地运行的竖版视频剪辑引擎：用户用自己的 Claude 订阅与 Claude Code 代理，在聊天中说明需求，代理经转写、选时刻、以代码形式撰写剪辑、技术检查五阶段完成剪辑，由本机 ffmpeg、HyperFrames 与本地 Whisper 渲染输出。视频文件不出本机，但代理读取的帧与转写文本会发送到 Anthropic 会话。每条视频约 25–30 分钟；已在两台 Windows 机器上测试，Mac/Linux 未测试；代理只看帧与测量，不处理声音与动态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五阶段代理剪辑流程：转写、选时刻、代码化剪辑、技术检查、产出
- 本地 Whisper 转写与 ffmpeg/HyperFrames 本机渲染，视频文件不出本机
- 风格笔记本记录用户反馈作为后续剪辑提示
- 只读监控页面展示任务进度、成品视频与风格笔记本（127.0.0.1 本地访问）

## 适用场景

- 把自己的游戏录像剪成竖版 Short
- 从获授权的直播录像中截取多条竖版片段
- 用带旁白的单条信息或列表类 Short 制作视频

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: **Short Motoru is an editor, not a video generator.** You bring the raw footage (your own game recording, or a strea
> L22: Short motoru video üreten bir yapay zekâ değil, bir kurgucudur: sen ham görüntüyü verirsin (kendi oyun kaydın, kull
> L40: 1. **Motor:** her video için bir iş klasörü ve bir izleme sayfası (ilerleme, çıkan videolar, tarz defteri). Uzun ka

## 星数曲线

```mermaid
xychart-beta
    title "furkancavlak/claude-shorts-editor 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `4f36835138be` · [字段定义](../../DATASET.md)*
