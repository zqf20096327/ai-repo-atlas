# tornikegomareli/pi-remote-ios

⭐ 14 · Swift · MIT · 推送 2026-08-06 · [GitHub](https://github.com/tornikegomareli/pi-remote-ios) · 个人维护

**用 iPhone 远程控制 Pi coding-agent 会话的原生 iOS 应用与扩展**

由两部分组成：TypeScript Pi 扩展在主机上暴露配对 WebSocket 端点，SwiftUI iOS 应用通过六位配对码或 QR 深链接入，可发送提示词、排队跟进、中断与压缩会话、切换模型与思考级别、调用 Pi 技能、原生渲染 diff、应答阻塞问题并流式显示输出。仅控制当前交互式会话，不运行后台守护进程；iOS 应用为源码构建，需 Xcode 26.2+；要求手机与主机在同一可信局域网，WebSocket 未加密。项目为早期预览版，独立社区项目，与 Earendil Inc 无关联。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 六位配对码/QR 深链配对，令牌存 iOS Keychain，两分钟过期且单次有效
- 发送提示词、排队跟进、转向、中断与压缩活动会话，切换模型与思考级别
- 通过斜杠补全发现并调用主机端 Pi 技能，原生渲染编辑与写入 diff
- iOS 26 continued-processing 后台尽力监控，通知不含提示词/响应/凭证内容

## 适用场景

- 离开键盘时用手机继续操控本机的 Pi coding-agent 会话
- Pi 需要输入或完成时在手机上收到提醒并应答
- 在手机上查看 diff、命令执行与文件变更汇总

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: Control an active Pi coding-agent session from a native iPhone app.
> L12: - a TypeScript Pi extension that exposes a paired WebSocket endpoint;
> L13: - a SwiftUI iOS app that connects, authenticates, and controls the active session.

## 星数曲线

```mermaid
xychart-beta
    title "tornikegomareli/pi-remote-ios 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [14, 13, 14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c71f9600e506` · [字段定义](../../DATASET.md)*
