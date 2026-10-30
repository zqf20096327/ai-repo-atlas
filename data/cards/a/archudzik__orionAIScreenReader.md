# archudzik/orionAIScreenReader

⭐ 19 · Kotlin · MIT · 推送 2026-06-01 · [GitHub](https://github.com/archudzik/orionAIScreenReader) · 个人维护

**给视障用户的 Android AI 屏幕阅读器，用 Gemini 朗读屏幕内容**

以 Android 无障碍服务形式运行的屏幕阅读器：用户点击悬浮的 Read Screen 按钮后截取当前屏幕快照，发送至 Gemini AI 提取信息，再通过 Android TTS 或可选的 Gemini TTS 朗读出来，支持暂停、恢复、重复播放与触觉反馈。提供简洁描述与朗读可见文本两种模式，可配置语言、语速、语音引擎与私有 Gemini API key，处理后的截图在私有存储中临时保存并删除。面向视障或有视觉障碍的用户，需联网并自行从 Google AI Studio 获取 API key。

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

- 截屏发送 Gemini AI 提取屏幕信息并朗读
- Android TTS 默认 / Gemini 在线 TTS 可选，失败时回退 Android TTS
- 悬浮按钮触发，朗读后提供暂停/恢复/重复控制
- 诊断日志查看/分享，分享时自动脱敏 API key

## 适用场景

- 视障用户听取手机屏幕上的文字或内容摘要
- 应对被弹窗或交互元素遮挡、难以用常规读屏访问的应用内容
- 通过简洁描述模式快速了解屏幕要点

## 场景标签

 · 领域:无障碍/移动应用

## 证据(README 行号)

> L11: - **AI-Powered**: Captures a snapshot of the current screen, sends it to Gemini AI, and reads the result aloud.
> L36: 4. **AI Processing**: The snapshot is sent to Gemini AI, which extracts meaningful information. The floating contro

## 星数曲线

```mermaid
xychart-beta
    title "archudzik/orionAIScreenReader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6bd40431def4` · [字段定义](../../DATASET.md)*
