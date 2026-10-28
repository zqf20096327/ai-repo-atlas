# shubhamshnd/Open-Cluely

⭐ 186 · JavaScript · 推送 2026-09-24 · [GitHub](https://github.com/shubhamshnd/Open-Cluely) · [官网](https://github.com/shubhamshnd/Open-Cluely) · 个人维护

**实时 AI 面试助手桌面应用：转录+截屏+Gemini 生成回答**

基于 Electron 的 Windows 桌面应用，面向技术面试与在线会议场景：通过 AssemblyAI 流式转录对主机/麦克风双路音频，截取屏幕截图，调用 Gemini 生成回答；提供 Ask AI（全上下文回答）、Screen AI（截图解读）、Suggest（口语开场建议）、Notes（会议纪要整理）四种操作。支持多 Gemini API key 自动故障切换、每条消息的上下文开关，并内置移动端伴侣界面（端口 7823 的 Web 服务）。限制：需自备 Gemini 与 AssemblyAI API key，依赖原生模块（可能需 C++ 构建工具），README 提示仅在允许录制与 AI 协助的环境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双路音频实时转录（主机/麦克风，可分别开关）
- 四种 AI 操作：Ask AI / Screen AI / Suggest / Notes
- 多 Gemini API key 列表与配额错误自动切换
- 内置移动端伴侣界面（局域网端口 7823，无需装 App）

## 适用场景

- 技术面试中实时获取问题解答与开场应答建议
- 对屏幕上的题目或报错截图让 AI 给出解法
- 会议结束后生成结构化纪要与行动项

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Open-Cluely is an Electron desktop copilot for technical interviews and live meetings. It combines AssemblyAI stream
> L7: Open source alternative for Cluely and Parakeetai. Your Real-Time AI Interview Assistant 😉
> L34: **What it does:** reads the entire context as one unified thread, silently corrects speech-to-text recognition erro

## 星数曲线

```mermaid
xychart-beta
    title "shubhamshnd/Open-Cluely 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25", "2026-10-28"]
    y-axis "stars" 181 --> 187
    line [182, 183, 185, 186]
```

2026-10-18 182 → 2026-10-28 186（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `118e279c2a82` · [字段定义](../../DATASET.md)*
