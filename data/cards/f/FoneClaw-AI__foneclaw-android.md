# FoneClaw-AI/foneclaw-android

⭐ 19 · Kotlin · MIT · 推送 2026-10-29 · [GitHub](https://github.com/FoneClaw-AI/foneclaw-android) · [官网](https://www.foneclaw.ai) · 组织维护

**Android 手机 AI 语音代理：一句话执行 120+ 设备操作**

面向 Android 用户的设备端 AI agent 应用：通过自然语言指令驱动 Accessibility Service 读取 UI 树、点击、滑动、填表，跨应用串联多步操作，内置 120+ 工具覆盖邮件、地图、电话、短信、日历与系统设置等 16 类，无需 root。动作前有风险分级审批：只读操作直接执行，发送数据或删除内容类操作需用户确认；密码与 API key 不经过 LLM，邮件凭据以 AES-256-GCM 加密。支持社区 Skills、无代码 Workflow 模板（回放无需 LLM）与 Plugin APK 扩展。要求 Android 9（API 28）及以上，从 Releases 页下载 APK 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Accessibility Service 实现跨应用多步自动化，无需 root
- 120+ 内置工具、16 个类别、14 种语言
- 风险分级审批：高危操作需用户确认，凭据 AES-256-GCM 加密
- 可扩展 Community Skills、Workflow 模板（回放不调用 LLM）与 Plugin APK

## 适用场景

- 用语音让手机代查邮件并汇总紧急事项
- 一句话完成找餐厅并发送给联系人等跨应用流程
- 录制无代码工作流实现日常自动化（如到家自动连 Wi-Fi）

## 场景标签

`语音 Agent` `GUI 自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L17: > **FoneClaw doesn't just answer questions — it does things.** Tell it *"check my work email and summarize the urge
> L21: Most "AI assistants" live in a chat bubble and can't touch your phone. FoneClaw is different — it acts as a **real 

## 星数曲线

```mermaid
xychart-beta
    title "FoneClaw-AI/foneclaw-android 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-29", "2026-10-30"]
    y-axis "stars" 15 --> 20
    line [16, 17, 18, 19, 19]
```

2026-10-18 16 → 2026-10-30 19（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `906be286a0f2` · [字段定义](../../DATASET.md)*
