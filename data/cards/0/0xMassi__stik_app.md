# 0xMassi/stik_app

⭐ 268 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/0xMassi/stik_app) · [官网](https://www.stik.ink) · 个人维护 · 中文 README

**macOS 快速笔记捕获应用：快捷键唤出便签即写即存**

面向 macOS 用户的本地优先笔记应用：全局快捷键唤出浮动便签，笔记以纯 markdown 文件保存到 ~/Documents/Stik/，支持语音转录（WhisperKit 跑在 Neural Engine）、选中文本剪辑、文件夹与命令面板搜索、AES-256 加密与 Touch ID 解锁、iCloud/Dropbox/Syncthing 同步。AI 部分（语义搜索、文件夹建议、笔记嵌入）通过 Apple NaturalLanguage 框架在设备端运行，无云端与 API key。技术栈为 React 19 + Tauri 2.0 (Rust)，要求 macOS 14+，提供 dmg 下载与 Homebrew 安装，也可从源码构建（需 Xcode CLI、Rust、Node.js 20+、Bun）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全局快捷键唤出便签，笔记为纯 markdown 文件存于本地
- WhisperKit 在 Neural Engine 上做离线语音转录，音频不离开设备
- 设备端语义搜索与笔记嵌入（Apple NaturalLanguage 框架），无云端
- AES-256 加密笔记，Touch ID/设备密码解锁

## 适用场景

- 工作中快速捕获灵感，不打断当前流程
- 用语音输入把口述内容转成文字笔记
- 在多台 Mac 间通过 iCloud 同步 markdown 笔记
- 对敏感笔记加密封存

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L79: **Voice.** `Cmd+Shift+D` transcribes speech straight into the note you're editing. `Cmd+Shift+V` opens a fresh post
> L91: **On-device AI.** Semantic search, folder suggestions, and note embeddings through Apple's NaturalLanguage framewor
> L124: - All AI runs **on-device** via Apple frameworks -- nothing is sent anywhere

## 星数曲线

```mermaid
xychart-beta
    title "0xMassi/stik_app 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 267 --> 270
    line [268, 269, 268]
```

2026-10-18 268 → 2026-10-22 268（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `717fba1ce8b9` · [字段定义](../../DATASET.md)*
