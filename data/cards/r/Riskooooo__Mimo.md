# Riskooooo/Mimo

⭐ 18 · Rust · MIT · 推送 2026-10-05 · [GitHub](https://github.com/Riskooooo/Mimo) · [官网](https://riskooooo.github.io/Mimo/) · 个人维护

**Windows 桌面悬浮 AI 助手：理解指令、提建议、自动执行小任务**

以屏幕顶部悬浮胶囊形式运行的 Windows 桌面助手，受 iOS 灵动岛启发：理解键入（F9）与语音（Hey Mimo，Vosk 离线识别，英/法语）请求，可打开应用与网站、平台搜索、系统控制、提醒/待办、截屏录屏、翻译、PC 体检，并基于本机活动记录（仅存本地 30 天）主动给出建议。本地 AI 为可选项（默认关闭）：开启后下载 Qwen3 4B Instruct 模型与 llama.cpp 引擎，在 Vulkan 上离线运行。项目处于早期开发阶段，仅支持 Windows。技术栈为 Tauri 2 + Rust + Svelte 5。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 悬浮胶囊 UI 与表情角色，支持键入和离线语音两种召唤方式
- 可选本地 AI：下载 Qwen3 4B（约 2.5 GB）与 llama.cpp 引擎，完全离线运行（Vulkan）
- 基于本机活动学习并主动提出建议（打开常用应用、关掉拖慢电脑的程序等）
- 无遥测，数据仅存本机，网络请求仅限打开 URL、天气与翻译

## 适用场景

- 用语音或快捷键在桌面直接打开应用、搜索平台、控制音量亮度
- 设置提醒、闹钟和待办，用一句话完成截屏录屏
- 让助手基于使用习惯提醒休息、关闭占用资源的程序
- 离线提问、总结或改写剪贴板文本（可选本地模型）

## 场景标签

`AI 助手` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Mimo is a desktop companion for Windows that lives in a small floating pill at the top of the screen, inspired by th
> L33: - **Local AI (optional, off by default)** - turn it on in the settings and Mimo downloads, once and in the backgrou
> L7: The project is in early development. Mimo already understands typed and spoken requests (French and English), learns

## 星数曲线

```mermaid
xychart-beta
    title "Riskooooo/Mimo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `363440d5efc9` · [字段定义](../../DATASET.md)*
