# karem505/rusty-inbox

⭐ 13 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/karem505/rusty-inbox) · [官网](https://aboelmakarem.pro/apps/rusty-inbox) · 个人维护

**跨平台原生桌面邮件客户端，带可选 AI 助手**

用 Rust 编写邮件引擎、Qt 6/QML 界面的开源桌面邮件客户端，支持 Linux/Windows/macOS，连接 IMAP/SMTP 账户（Gmail 应用密码、Fastmail、iCloud 等）。功能含 Smart Inbox 分组、IMAP IDLE 即时收信、统一收件箱、撤销发送、键盘操作与 Thunderbird 导入。0.2.0 起提供可选 AI 助手：可选 ChatGPT 订阅登录（免 API key）、OpenAI、Anthropic、OpenRouter、Ollama 或任意 OpenAI 兼容服务器，支持校对、改写、翻译、摘要、草拟回复、钓鱼检测等；默认关闭。数据本地 SQLite 缓存，无遥测。Linux 推荐 Flatpak 安装，也可源码构建（需 Rust 1.85+ 与 Qt 6.8+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 邮件引擎为原生 Rust，界面 Qt Quick，启动与内存开销低
- 可选 AI 助手支持 ChatGPT 订阅/OpenAI/Anthropic/OpenRouter/Ollama/OpenAI 兼容服务器
- Smart Inbox 按人员/通知/通讯分组，IMAP IDLE 即时收信
- 本地 SQLite 缓存邮件，无遥测、无自有服务器

## 适用场景

- 在桌面用一个轻量客户端收发多个 IMAP/SMTP 账户的邮件
- 让 AI 助手校对、翻译、摘要邮件或草拟回复
- 用本地 Ollama 运行 AI 功能以保持邮件数据不出本机
- 从 Thunderbird 一键迁移账户与密码

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L10: **A fast, native email client for Linux, Windows and macOS.**
> L32: - **Optional AI assistant (new in 0.2.0).** Choose the provider and the model: sign in with your
> L196: **AI assistant.** It is off until you turn it on in Settings → AI and choose a provider. Then the

## 星数曲线

```mermaid
xychart-beta
    title "karem505/rusty-inbox 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-30 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `39c5ef574d5e` · [字段定义](../../DATASET.md)*
