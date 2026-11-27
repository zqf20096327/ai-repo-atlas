# ankurCES/Lapis-Zero

⭐ 6 · Kotlin · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/ankurCES/Lapis-Zero) · 个人维护

**给 CardputerZero 手持机的 agentic 固件：看屏操作你的电脑**

为 M5Stack CardputerZero（CM0，512 MB）定制的固件，将其变成手持 AI 控制器：用户输入自然语言任务，Python agent 服务截图→询问模型下一步→经 VNC/SSH 在用户自己的电脑上执行，循环至任务完成。Rust 程序直接绘制 framebuffer 界面（无 X11/Wayland），配 Android Kotlin 伴侣应用显示步骤与远程屏幕，流量走 Tailscale。三种授权策略（strict/balanced/autonomous）与 kill switch 控制风险。目前仅一名作者在一台设备上使用过，Android 应用为 debug 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 截图→决策→执行的 agent 循环，每步在手持机与手机上实时可见
- 支持 Anthropic 及任意 OpenAI 兼容 provider，含 OpenRouter/DeepSeek 等一键预设
- 可将聊天交给主机上已有的 agent CLI（Claude Code、Gemini CLI、Codex 等）
- 三种授权策略 + 手持机/手机双端 kill switch，破坏性命令一律拒绝

## 适用场景

- 用手持机远程让 AI 检查 CI 结果并重启失败的 worker
- 让 agent 在我的 Mac mini 上查看屏幕、点击输入执行操作
- 把消息转给桌面上的 Claude Code 处理并取回结果
- 通过手机应用实时观看并审批 agent 的每一步

## 场景标签

`GUI 自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L16: **Lapis-Zero is one of the first custom firmwares for it, and an agentic one.** It replaces the stock
> L17: software with a single-purpose operating system. You give it a task in plain words. An AI agent then
> L151: 2. The agent asks the model for the next step, given the latest screenshot.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `8df62773ebbb` · [字段定义](../../DATASET.md)*
