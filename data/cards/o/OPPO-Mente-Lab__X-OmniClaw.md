# OPPO-Mente-Lab/X-OmniClaw

⭐ 266 · Kotlin · Apache-2.0 · 推送 2026-05-22 · [GitHub](https://github.com/OPPO-Mente-Lab/X-OmniClaw) · [官网](https://eggplant95.github.io/X-OmniClaw-Page/) · 组织维护 · 中文 README

**在 Android 手机上本地运行的多模态设备 Agent，感知-记忆-执行一体**

部署在物理 Android 设备上的边缘侧多模态 Agent 应用：聚合屏幕 UI 状态、摄像头视觉与语音输入构建统一感知栈，以 LLM/VLM 推理后通过原子触控操作执行跨 App 任务，形成 观察→推理→执行 与 感知→规划→执行→验证 的闭环。提供工作记忆与长期个人记忆、10 个内置技能（淘宝搜索、相册问答、定时自动化等）、可复用 deeplink 技能与多会话并行。模型侧通过内置 provider（OpenRouter/Anthropic/OpenAI/Moonshot/MiniMax/Ollama 等）填 API Key 接入，STT 与 VLM 可分别配置。以 APK 形式安装，需 Android 8.0+，授予无障碍、截屏、相机等七项权限；也可用 JDK 17+ 与 Android SDK 从源码构建。附 arXiv 技术报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 屏幕 UI、摄像头视觉、语音三域统一感知栈
- 观察→推理→执行设备端闭环，含预算与循环检测
- 工作记忆 + 本地多模态长期记忆的个性化交互
- 10 个内置技能，支持录制一次生成可复用 deeplink 技能

## 适用场景

- 用语音或文字让手机跨 App 完成搜索、比价、总结等任务
- 把常用导航路径录制为一句话直达的技能
- 按周期定时自动打开应用执行任务（息屏也可）
- 基于相册记忆做主题照片搜索与一键视频

## 场景标签

`GUI 自动化` `多模态` · 领域:效率与自动化

## 证据(README 行号)

> L11: **X-OmniClaw** is an edge-native **Multimodal Android Agent** that integrates multimodal perception, memory, and ac
> L42: To ensure task completion in complex mobile GUI environments, X-OmniClaw organizes every interface interaction as a
> L70:  Perception Multi-modal Input ASR, screenshot/recording frames, accessibility tree → unified context.

## 星数曲线

```mermaid
xychart-beta
    title "OPPO-Mente-Lab/X-OmniClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 265 --> 267
    line [266, 266]
```

2026-10-18 266 → 2026-10-23 266（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `80392273f06c` · [字段定义](../../DATASET.md)*
