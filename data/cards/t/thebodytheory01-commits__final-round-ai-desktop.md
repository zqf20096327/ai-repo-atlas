# thebodytheory01-commits/final-round-ai-desktop

⭐ 18 · HTML · MIT · 推送 2026-11-27 · [GitHub](https://github.com/thebodytheory01-commits/final-round-ai-desktop) · 个人维护

**给求职者提供视频面试实时辅导、语音转录与答案建议的桌面应用**

面向求职者与职场人士的 Windows/macOS 桌面应用，在视频通话过程中捕获系统音频与麦克风输入，用内嵌 Whisper 引擎在本地做实时语音转录（约亚秒级延迟），检测问题类型（行为类/技术类/案例类）后调用可配置的语言模型生成结构化要点式回答。核心机制包括：通过窗口显示亲和性 API 注册的不可截取悬浮层（共享屏幕时不被捕获）、全局热键控制、STAR 框架模板、会话历史与复盘报告，转录本本地加密存储。后端模型可切换，支持自托管端点实现完全离线转录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Whisper 引擎实时语音转录，原始音频不出设备
- 经 display affinity API 注册的防截取悬浮层，屏幕共享时不出现
- 模型无关后端，可在设置面板切换多个语言模型提供方
- STAR 框架模板与基于简历/职位描述的会话画像融合生成

## 适用场景

- 视频面试时在悬浮面板中查看实时转录与要点式回答建议
- 面试结束后导出完整转录并生成复盘报告
- 完全离线场景下用本地转录搭配自托管模型端点使用

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: Final Round AI Desktop is a performance-oriented desktop application that delivers real-time interview coaching, liv
> L39: Each audio segment is transcribed on-device by an embedded Whisper inference engine. Transcription runs locally, so
> L47: The finalized transcript is passed to the response engine together with the active session profile. The engine dete


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `464708e6063d` · [字段定义](../../DATASET.md)*
