# jackwener/DSH-Android

⭐ 617 · Kotlin · Apache-2.0 · 推送 2026-10-31 · [GitHub](https://github.com/jackwener/DSH-Android) · 个人维护 · 中文 README

**免 ROOT 免 Termux 的安卓 DeepSeek Harness 手机 Agent 应用**

以单个 APK 在安卓手机上运行 DeepSeek Harness（dsh）：Agent 通过无障碍服务读屏、点按、输入，可操作各类 App、整理文件（读 PDF/Word/Excel/PPT）、修改系统设置，并支持定时/条件触发的自动化。引擎为内嵌 App 进程的 Node 24 共享库（JNI 启动），无需 proot/Termux/root，Shizuku 可选。除 DeepSeek 外可添加 OpenAI、Claude、Gemini、Kimi 等第三方模型（仅 OpenAI 兼容接口），也可经 SSH/DSH Remote 连接电脑上的 DSH。限制：锁屏后不能操作其他 App、第三方模型联网搜索需另配 DeepSeek key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 APK 免 ROOT/免 Termux 在安卓运行 dsh，引擎内嵌 App 进程（Node 24 经 JNI 启动）
- 基于无障碍服务读屏/点按/输入，可操作系统设置与通知，支持定时/条件自动化
- 支持 DeepSeek 账号登录及多种第三方 OpenAI 兼容模型服务
- Android 14 及以上可配 Shizuku/ADB 用不打扰模式在虚拟屏幕操作

## 适用场景

- 让 Agent 替我在微信发消息、淘宝下单、投递简历
- 整理手机文件并读取文档内容
- 设置定时或在连 Wi-Fi/充电等条件下自动执行任务
- 出门时通过 SSH 连接电脑上的 DSH 继续派活

## 场景标签

`GUI 自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L3: 不要 root，不用电脑，直接跑在你的安卓手机上。真正的手机 Agent，替你把手机上的事干完。
> L18: - **手机上的 App 都能操作**：用微信发消息、总结群聊，抓取小红书上的内容，在 BOSS 直聘上直接投递、打招呼，去淘宝帮你下单，等等。


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8093b19985f3` · [字段定义](../../DATASET.md)*
