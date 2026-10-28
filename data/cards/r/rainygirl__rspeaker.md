# rainygirl/rspeaker

⭐ 27 · Python · MIT · 推送 2026-02-10 · [GitHub](https://github.com/rainygirl/rspeaker) · [官网](https://rainygirl.github.io/2026/02/rspeaker) · 个人维护

**macOS 韩语语音助手：语音识别命令并用 TTS 朗读新闻摘要**

macOS 上的语音识别助手应用，基于 Python 调用 Apple SFSpeechRecognizer 框架识别韩语语音命令，通过唤醒词“여보게”激活。支持的功能包括：调用 Google Gemini API 摘要 Google 新闻主要报道并配合首尔天气信息朗读、报时和报日期、退出程序。语音输出使用 Microsoft Edge TTS 的韩语语音（ko-KR-SunHiNeural）。要求 macOS 10.15 以上、Python 3.13 以上，用 uv 管理依赖，通过 make 命令安装与运行；新闻摘要功能需要用户自备 Gemini API 密钥。

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

- 基于 SFSpeechRecognizer 的韩语语音命令识别（唤醒词激活）
- Gemini AI 摘要 Google 新闻并配合天气信息朗读
- Microsoft Edge TTS 韩语语音输出（ko-KR-SunHiNeural）
- 报时/报日期/退出等语音命令

## 适用场景

- 用韩语语音命令在 macOS 上获取新闻摘要与天气
- 语音询问当前时间与日期并朗读结果
- 免手动操作通过语音获取信息播报

## 场景标签

`语音 Agent` `语音识别` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3: 이 프로젝트는 macOS에서 동작하는 음성 인식 비서 애플리케이션입니다. Python을 사용하여 `SFSpeechRecognizer` 프레임워크와 연동하여 음성을 인식하고, 사용자의 명령어에 따라 다양한 작업
> L8: - **뉴스 제공**: "오늘 뉴스"라고 말하면 Google 뉴스의 주요 기사를 Gemini AI로 요약하고, 서울의 현재 날씨 정보와 함께 음성으로 읽어줍니다.
> L10: - **자연스러운 음성 출력**: Microsoft Edge TTS를 사용하여 자연스러운 한국어 음성(ko-KR-SunHiNeural)으로 정보를 전달합니다.

## 星数曲线

```mermaid
xychart-beta
    title "rainygirl/rspeaker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6e901248365b` · [字段定义](../../DATASET.md)*
