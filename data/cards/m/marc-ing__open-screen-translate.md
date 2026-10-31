# marc-ing/open-screen-translate

⭐ 29 · Rust · MIT · 推送 2026-08-17 · [GitHub](https://github.com/marc-ing/open-screen-translate) · 个人维护 · 中文 README

**macOS 菜单栏截图取词翻译工具：本地 OCR + 自带 API key 的 AI 翻译**

基于 Tauri 2、Rust、ScreenCaptureKit 与 Apple Vision 构建的 macOS 菜单栏应用：通过全局快捷键截取屏幕区域，用 Apple Vision 在本地完成多语言 OCR（合并换行、保留段落结构），可编辑识别文本后调用用户配置的 AI 服务（DeepSeek、OpenAI、Anthropic Claude、Google Gemini 或自定义兼容端点）流式输出翻译，支持手动翻译窗口。API key 仅存于 macOS Keychain。要求 macOS 14+、屏幕录制权限与至少一个 AI 服务 API key；提供 DMG 安装包，也可从源码（Node.js 20+/Rust/Xcode CLI）运行。

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

- Apple Vision 本地 OCR，仅将待翻译文本发送至 AI 服务
- 支持 DeepSeek/OpenAI/Anthropic Claude/Google Gemini 及自定义兼容端点
- OCR 结果自动合并视觉换行并保留段落结构，识别文本可编辑后重译
- API key 仅存于 macOS Keychain，支持登录自启与首跑引导

## 适用场景

- 阅读外文内容时截图快速取词翻译
- 手动输入文本并选择源/目标语言进行翻译
- 在只信任本地 OCR 的前提下使用自带 API key 的云端翻译

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L7:  An open-source, AI-powered macOS menu bar app for capturing, recognizing, and translating on-screen text.
> L13: OpenScreenTranslate is built with Tauri 2, Rust, ScreenCaptureKit, and Apple Vision. It runs in the menu bar withou
> L29: - Use DeepSeek, OpenAI, Anthropic Claude, Google Gemini, or a custom compatible service

## 星数曲线

```mermaid
xychart-beta
    title "marc-ing/open-screen-translate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2bb53f87e63b` · [字段定义](../../DATASET.md)*
