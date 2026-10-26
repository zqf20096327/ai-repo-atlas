# mahdidavoodi7/expo-thinking-orbs

⭐ 42 · TypeScript · MIT · 推送 2026-08-16 · [GitHub](https://github.com/mahdidavoodi7/expo-thinking-orbs) · [官网](https://motionary.dev/blog/react-native-ai-loading-animation) · 个人维护

**React Native/Expo 的 AI 思考指示器与语音 Agent 球形动画组件库**

为 React Native 与 Expo 应用提供的 UI 组件库：包含六个点阵球形动画状态（working/searching/solving/listening/composing/shaping）覆盖 AI 思考过程的不同阶段，以及独立的 VoiceOrb 组件映射语音 Agent 的九个生命周期状态并随音频幅度起伏。全部动画通过 Skia 与 Reanimated 在 UI 线程绘制，token 流式输出时保持帧率。库本身不采集音频，仅提供 useVoiceAmplitude 桥接外部音源；需 Reanimated 4（新架构）。是 web 库 thinking-orbs 的 React Native 移植。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六种思考状态动画 + 独立 VoiceOrb 语音 Agent 组件
- Skia + Reanimated 全程 UI 线程绘制，流式输出时保持帧率
- VoiceOrb 状态联合与 LiveKit AgentState 一致，可直接透传
- 支持颜色渐变、音频频段输入、四元数倾斜等驱动参数

## 适用场景

- 为 LLM 聊天应用显示思考/搜索/推理等过程动画
- 语音 Agent 界面中展示会话生命周期与实时音量反馈
- 让指示动画跟随麦克风音量或滚动进度驱动

## 场景标签

 · 领域:移动端 UI 组件库

## 证据(README 行号)

> L11: `expo-thinking-orbs` gives an AI or agent UI something better than a spinner: a
> L224: `<VoiceOrb>` is a wrapper that takes a voice agent's lifecycle state and its

## 星数曲线

```mermaid
xychart-beta
    title "mahdidavoodi7/expo-thinking-orbs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2f21104e2abe` · [字段定义](../../DATASET.md)*
