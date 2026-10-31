# arunishrajput/Gemini-Voice-Assistant

⭐ 24 · Python · 推送 2026-08-15 · [GitHub](https://github.com/arunishrajput/Gemini-Voice-Assistant) · 个人维护

**终端唤醒词语音助手：调用 Gemini API 对话并语音播报**

基于 Python 的终端语音助手：通过麦克风监听唤醒词（默认 gemini）激活，用 speech_recognition 转录语音，经 google-genai SDK 调用 Gemini API 生成回复，再用 pyttsx3 以语音播报。界面为 Rich 构建的实时终端 UI，显示状态与对话记录。需自备 Gemini API key（存于 .env），提供免麦克风与 API key 的 --demo 演示模式。运行需 Python 3.9+ 与 PortAudio 系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 唤醒词激活与退出词暂停的状态机流程
- Rich 实时终端 UI（状态、对话日志、页脚）
- --demo 模式无需麦克风与 API key 预览界面
- API key 通过 .env/环境变量/命令行参数三途配置

## 适用场景

- 在终端用语音与 Gemini 对话并获得语音回复
- 无麦克风环境下预览语音助手界面
- 通过命令行参数自定义唤醒词、模型与语速

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L4: transcribes what you say, chats with Google's Gemini API, and speaks the
> L122:  `speech_recognition`, send it to Gemini via the `google-genai` SDK, and

## 星数曲线

```mermaid
xychart-beta
    title "arunishrajput/Gemini-Voice-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `84a1e73e45e0` · [字段定义](../../DATASET.md)*
