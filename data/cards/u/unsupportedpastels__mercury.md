# unsupportedpastels/mercury

⭐ 56 · Kotlin · MIT · 推送 2026-10-24 · [GitHub](https://github.com/unsupportedpastels/mercury) · 个人维护

**Hermes Agent 的非官方开源移动客户端（Android + iOS）**

基于 Kotlin Multiplatform 共享核心的移动端伴侣应用，连接官方兼容的 Hermes Agent 后端（Hermes Cloud 或自托管 hermes dashboard/hermes serve）：逐 token 流式回复、内联渲染工具活动与推理块、远程处理工具审批/澄清/密钥提示、浏览产物与主机文件、系统分享导入附件、Nous OAuth（PKCE）与 basic auth 登录、可选 Relay 二维码端到端加密配对、依托服务端 /api/audio 路由的语音对话。适配折叠屏与平板多窗格布局。Android 提供官方接口直接下载 APK，iOS 从源码构建。非官方、MIT 许可，不隶属 Nous Research。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐 token WebSocket 流式回复，内联渲染工具活动、代码块与推理过程
- 手机端远程处理工具审批、澄清问题与密钥提示
- Nous OAuth（系统浏览器 PKCE）与 cookie-backed basic auth 双认证模式
- Relay 二维码配对实现端到端加密 Noise XK 通道

## 适用场景

- 在手机上随时随地访问并控制自己运行的 Hermes Agent 会话
- 长任务挂后台跑完通过通知回到会话继续操作
- 在折叠屏或平板上以多窗格布局浏览项目、会话与实时工作区

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L13: - Connects to an unchanged, officially compatible Hermes Agent backend supplied by `hermes dashboard` or headless `
> L74: Mercury is a client, not an agent host. Install and configure Hermes Agent on a machine you control (or deploy an a

## 星数曲线

```mermaid
xychart-beta
    title "unsupportedpastels/mercury 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-27 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `de8586116e97` · [字段定义](../../DATASET.md)*
