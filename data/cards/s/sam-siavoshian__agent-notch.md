# sam-siavoshian/agent-notch

⭐ 22 · Swift · MIT · 推送 2026-09-22 · [GitHub](https://github.com/sam-siavoshian/agent-notch) · [官网](https://agent-notch.vercel.app/) · 个人维护

**驻留 MacBook 刘海区的 macOS 语音 computer-use agent**

用 Swift/SwiftUI 编写的 macOS 菜单栏刘海区应用：长按光标说话，OpenAI Whisper 转写，快速命令由 IntentRouter 本地处理，其余交给 Claude computer-use 循环驱动鼠标与键盘，工具调用在刘海面板实时展示，回复经 OpenAI TTS 或本地 Piper 语音播报。模型提供方可选 Anthropic API 直连或本地 Claude Code 子进程（经捆绑的 MCP stdio 侧车）。要求 M 系列 MacBook（物理刘海）、macOS 14+、Swift 5.10，需通过 XcodeGen/Xcode 自行构建并授予辅助功能、屏幕录制、麦克风三项权限，需 Anthropic/OpenAI API key（部分场景可豁免）。TritonHacks 2026 出品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音输入→Claude computer-use 循环驱动鼠标键盘，工具调用实时显示在刘海面板
- 双提供方：Anthropic API 直连或本地 Claude Code 子进程（AgentNotchMCP stdio 侧车）
- Whisper 转写 + IntentRouter 快速路径（URL/Spotify/提醒事项不走模型）
- OpenAI TTS 或本地 Piper 离线语音合成，含 Dev Tools 与 kill-switch

## 适用场景

- 在 Mac 上用语音指挥 AI 代为操作桌面应用
- 通过屏幕截图让 agent 完成点击、输入等自动化任务
- 无需手动切换窗口即可从刘海区查看 agent 执行状态

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: Long-press the cursor, say what you want, watch Claude do it. Voice in, screenshot in, mouse + keyboard out. The not
> L35: 5. Anything else goes to the Claude computer-use loop. The notch shows each tool call live.

## 星数曲线

```mermaid
xychart-beta
    title "sam-siavoshian/agent-notch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `99579c1bfbed` · [字段定义](../../DATASET.md)*
