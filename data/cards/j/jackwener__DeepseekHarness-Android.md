# jackwener/DeepseekHarness-Android

⭐ 182 · Kotlin · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/jackwener/DeepseekHarness-Android) · 个人维护 · 中文 README

**安卓手机免 ROOT 运行 DeepSeek Harness 的手机 Agent 应用**

单个 APK 在安卓上内嵌运行 DeepSeek Harness（dsh）引擎：用户以自然语言指令让 agent 整理文件、读屏操作 App、修改系统设置，并支持定时/条件触发的自动化任务。引擎为 Node 24 编译的安卓原生库，经 JNI 在前台服务启动，不需 root、Termux 或 proot；Shizuku 可选解锁更多系统开关。除 DeepSeek 外可添加 OpenAI、Claude、Gemini、Kimi 等任意 OpenAI 兼容接口。限制：锁屏下不能操作其他 App，第三方模型仅支持 OpenAI 兼容 Chat Completions（HTTPS），冷启动约 5 秒。

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

- dsh 原样内嵌运行（不 fork），技能、MCP、子 agent、网页搜索可用
- 基于无障碍服务的读屏、点击、滑动、输入等设备操作
- 定时与条件触发（Wi-Fi/蓝牙/充电/地理位置/通知）的自动化
- 免 ROOT 免 Termux，单个 APK 安装，Shizuku 可选

## 适用场景

- 用一句话让手机整理文件、改系统设置或操作 App
- 设置定时任务或到达某地、连上 Wi-Fi 等条件触发的自动执行
- 在手机上本地运行 dsh agent 并回看每轮操作轨迹

## 场景标签

`GUI 自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: 在安卓手机上运行 DeepSeek Harness（dsh）：用一句话让它整理文件、操作 App、修改系统设置，或者设置自动执行的任务。
> L40: - **完整的 dsh**：dsh 原样运行（没有 fork），技能、MCP、子 agent、网页搜索都能用。


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0d894f93c1b3` · [字段定义](../../DATASET.md)*
