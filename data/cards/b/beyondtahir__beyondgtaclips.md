# beyondtahir/beyondgtaclips

⭐ 49 · Python · NOASSERTION · 推送 2026-11-19 · [GitHub](https://github.com/beyondtahir/beyondgtaclips) · 个人维护

**让 Claude/ChatGPT 自动把 GTA 6 直播切成 9:16 短视频**

一个以 Claude/ChatGPT 技能形式安装的本地剪辑工具：按用户指令搜索 YouTube 上最高观看量的直播，下载片段、用语音识别定位高能时刻、自动裁剪为 1080×1920 竖屏、生成 hook 文本与逐字字幕，并输出带 caption/hashtag 的 POSTING.md。全部剪辑与渲染在本机完成，无需 API key；时刻挑选与 hook 撰写依赖用户已有的 Claude 或 ChatGPT，无 AI 时按音量热点挑选。支持五种样式、按链接剪辑 Twitch/Kick、更换其他游戏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 识别尖叫声/笑声/聊天峰值等信号挑选高能片段
- 回看画面帧核验 hook 与内容匹配，不匹配则改写
- 五种 9:16 样式（Hook card/Stack/Bubble/Cinematic/Breaking news）
- 完全本地运行：语音识别、编辑、渲染均在本机

## 适用场景

- 把长直播自动剪成可投稿的竖屏短片
- 为剪辑分成活动批量产出带文案的视频
- 给任意游戏直播制作 shorts/reels

## 场景标签

`AI 写作` `语音识别` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L124: 1. **You say** *"Make GTA 6 clips"* to Claude or ChatGPT.
> L213: Yes. Everything runs on your own computer: speech recognition, editing and rendering.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `2da08426f8f6` · [字段定义](../../DATASET.md)*
